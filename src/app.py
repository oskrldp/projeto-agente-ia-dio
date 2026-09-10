#TRADUÇÃO: “Prepare as ferramentas necessárias para criar o Poco. Encontre a pasta principal do projeto e a pasta onde estão os dados fictícios. Depois, deixe definido que o Poco usará o modelo gpt-oss, instalado no Ollama deste computador.”

from pathlib import Path
import json 

import pandas as pd
import requests
import streamlit as st

#caminhos das pastas de projetos
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

#configuração do modelo local
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "qwen3:4b"

#carregamento de dados ficticios
#TRADUÇÃO: “Abra os dados fictícios do cliente, das transações, dos atendimentos anteriores e dos produtos financeiros. Deixe tudo pronto para o Poco usar ao responder.”
#Aqui está dando o compando de abrir

def carregar_json(nome_arquivo):
    caminho = DATA_DIR / nome_arquivo

    with caminho.open("r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

perfil = carregar_json("perfil_investidor.json")
transacoes = pd.read_csv(DATA_DIR / "transacoes.csv")
historico = pd.read_csv(DATA_DIR / "historico_atendimento.csv")
produtos = carregar_json("produtos_financeiros.json") 

#TRADUÇÃO: “Poco, aqui estão as informações fictícias do cliente: quem ele é, suas transações, atendimentos anteriores e produtos financeiros. Use isso quando precisar responder.”
#contexto financeiro disponivel para POCO
#Aqui está informando a localização dos dados que irá abrir

contexto = f"""
PERFIL DO CLIENTE:
nome: {perfil['nome']}
idade: {perfil['idade']} anos
perfil de investidor: {perfil['perfil_investidor']}
objetivo principal: {perfil['objetivo_principal']}
patrimonio total: R$ {perfil['patrimonio_total']}
reserva de emergencia: R$ {perfil['reserva_emergencia_atual']}

TRANSACOES:
{transacoes.to_string(index=False)}

HISTORICO DE ATENDIMENTOS:
{historico.to_string(index=False)}

PRODUTOS FINANCEIROS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

#Regras de comportamento do Poco

SYSTEM_PROMPT = """
Você é o Poco, um agente de educação e organização financeira.

OBJETIVO:
Ajudar jovens e adultos, entre 18 e 40 anos, a entender e organizar seus gastos de forma simples, objetiva, respeitosa e sem julgamentos.

PERSONALIDADE:
Você é amigável, didático, paciente, objetivo e motivador.
Fala como um amigo que entende de organização financeira.
Use linguagem informal, acessível e direta.
Explique termos técnicos quando forem necessários.
Use exemplos cotidianos e respostas curtas.

VOCÊ PODE:
- Ler e explicar os dados fictícios fornecidos.
- Organizar entradas e saídas.
- Somar gastos por categoria ou período.
- Identificar categorias com maiores gastos.
- Criar resumos financeiros.
- Ajudar a entender orçamento e metas.
- Explicar conceitos financeiros básicos.
- Explicar características gerais de produtos financeiros.
- Admitir quando não possuir dados suficientes.

VOCÊ NÃO PODE:
- Acessar contas bancárias reais.
- Realizar pagamentos, transferências ou compras.
- Pedir ou revelar senhas, cartões, tokens, PINs ou documentos.
- Inventar valores, transações, datas, categorias ou saldos.
- Prometer lucro, economia ou resultado futuro.
- Prever o valor de ações, moedas ou investimentos.
- Escolher investimentos específicos para o usuário.
- Mandar comprar ou vender ativos.
- Julgar, culpar, pressionar ou constranger o usuário.
- Responder fora do tema de organização e educação financeira.

REGRAS:
- Use os dados fornecidos quando a pergunta depender do cliente.
- Se a informação não existir, diga claramente que não possui essa informação.
- Explique a origem dos cálculos quando usar valores das transações.
- Apresente opções e informações, mas não tome decisões pelo usuário.
- Mantenha a resposta em até 3 parágrafos.
- Ao finalizar, pergunte se o usuário entendeu ou deseja aprofundar.

REGRAS ESPECÍFICAS PARA EVITAR RESPOSTAS INCORRETAS:

- Se o usuário pedir uma indicação de investimento, escolha de ativo
  ou garantia de lucro, recuse de forma breve.
- Após essa recusa, não recomende produtos alternativos, nem mesmo
  Tesouro Selic, CDB ou qualquer outro investimento.
- Não use expressões como "perfeito para você", "ideal para seu perfil"
  ou "você deveria investir".
- Você pode explicar um produto quando solicitado, mas de forma
  educativa e impessoal, sem recomendar compra ou aplicação.

- Reserva atual e meta da reserva são informações diferentes.
- Não afirme que uma meta foi atingida sem dados que comprovem isso.
- Se o valor da meta não estiver disponível, diga que não pode
  confirmar se a reserva está completa.
- Em perguntas que não exigem valores, não acrescente saldos,
  cálculos ou avaliações da reserva.
- Uma diferença entre entradas e saídas não é o saldo bancário real.

- Escreva valores como "570,00 reais", sem usar o símbolo de cifrão.
- Não use blocos de código nem formatação matemática nas respostas.

EXEMPLO DE LIMITE:

Usuário: Qual ação devo comprar hoje? Escolha uma e garanta lucro.
Poco: Não posso escolher investimentos para você nem garantir lucro.
Posso explicar conceitos e riscos de forma educativa, sem indicar
qual produto você deve comprar.
"""

#Criando Resumo Calculado sem depender da IA para resultados mais rápidos
#O que faz: percorre as transações, soma entradas e saídas separadamente e calcula a diferença. Decimal permite trabalhar com os valores decimais sem os arredondamentos típicos de números float

def resumo_calculado():
    from decimal import Decimal

    entradas = Decimal("0.00")
    saidas = Decimal("0.00")

    for _, transacao in transacoes.iterrows():
        valor = Decimal(str(transacao["valor"]))
        tipo = str(transacao["tipo"]). strip().lower()

        if tipo == "entrada":
            entradas += valor
        elif tipo == "saida":
            saidas += valor

    diferenca = entradas - saidas

    def formatar(valor):
        texto = f"{valor:,.2f}"
        return texto.replace(",", "X").replace(".", ",").replace("X", ".")

    return(
        "Resumo de todas as transações fictícias disponíveis:\n\n"
        f"- Entradas: {formatar(entradas)} reais.\n"
        f"- Saídas: {formatar(saidas)} reais.\n"
        f"- Diferença entre entradas e saídas: {formatar(diferenca)} reais.\n\n"
        "Essa diferença não representa seu saldo bancário real, "
        "pois não inclui um saldo inicial nem movimentações fora desses dados."
    )

#Fazer a pergunta “Quanto gastei com alimentação?” usar o Python para calcular, sem consultar a IA.
#O que faz: seleciona apenas saídas da categoria alimentação e soma os valores usando Decimal.
#Deixando o POCO mais rapido, sem depender da IA

def gastos_alimentacao():
    from decimal import Decimal

    filtro = (
        transacoes["categoria"].astype(str).str.strip().str.casefold().isin([
            "alimentação", "alimentacao"
        ])
    ) & (
        transacoes["tipo"].astype(str).str.strip().str.casefold() == "saida"
    )

    despesas = transacoes.loc[filtro]

    if despesas.empty:
        return(
            "Não encontrei despesas de alimentação nos dados disponíveis. "
            "Isso não significa que você não tenha tido gastos fora desses dados."
        )

    total = sum(
        (Decimal(str(valor)) for valor in despesas["valor"]),
        Decimal("0.00")
    )

    texto_total = f"{total:,.2f}"
    texto_total = (
        texto_total.replace(",", "X").replace(".", ",").replace("X", ".")
    )

    return(
        f"O total de despesas com alimentação é de {texto_total} reais, "
        f"considerando {len(despesas)} lançamentos.\n\n"
        "O cálculo inclui todas as transações de alimentação disponíveis "
        "na base fictícia, sem filtro de mês."
    )

#Comunicação entre o Poco e o Ollama
#TRADUÇÃO: pega a pergunta do usuário + regras do Poco + dados fictícios → envia tudo ao Ollama → recebe uma resposta → devolve a resposta para a página.
#criar a função que envia a pergunta para o OLLAMA e recebe a resposta sendo o POCO

def perguntar_ao_poco(pergunta):
    pergunta_normalizada = pergunta.casefold()

    if "senha" in pergunta_normalizada:
        return (
            "Não compartilhe sua senha bancária aqui nem com outras pessoas. "
            "Eu não acesso contas bancárias nem consulto seu saldo real. "
            "Posso ajudar a entender os dados fictícios deste projeto."
        )

    if pergunta_normalizada.strip().rstrip("?.!") == "mostrar resumo financeiro":
        return resumo_calculado()

    if pergunta_normalizada.strip().rstrip("?.!") in (
        "quanto gastei com alimentação",
        "quanto gastei com alimentacao",
    ):
        return gastos_alimentacao()

    pedidos_investimento = (
        "qual ação devo comprar",
        "qual acao devo comprar",
        "qual investimento devo escolher",
        "onde devo investir",
        "escolha um investimento",
        "escolha uma ação",
        "escolha uma acao",
        "garanta que vou lucrar",
        "garanta lucro",
        "me indique um investimento",
        "me indique uma ação",
        "me indique uma acao",
        "me indique um ativo",
    )

    if any(
        trecho in pergunta_normalizada 
        for trecho in pedidos_investimento
    ):
        return (
            "Não posso escolher investimentos para você nem garantir lucro. "
            "Posso explicar conceitos e riscos de forma educativa, "
            "sem indicar qual produto você deve comprar."
        )

    prompt = f""" 
{SYSTEM_PROMPT}

DADOS DISPONIVEIS: 
{contexto}

PERGUNTA DO USUARIO:
{pergunta}
"""

    try:
        resposta_http = requests.post(
            OLLAMA_URL,
            json={
                "model": MODELO,
                "prompt": prompt,
                "stream": False
            },
            timeout=180
        )   

        resposta_http.raise_for_status()
        resposta_json = resposta_http.json()

        return resposta_json.get(
            "response",
            "Não consegui receber uma resposta do modelo."
        )
    except requests.exceptions.ConnectionError:
        return "Não foi possível conectar ao modelo Ollama. Verifique se o Ollama está em execução."

    except requests.exceptions.Timeout:
        return "O modelo demorou muito para responder. Tente novamente."

    except requests.exceptions.RequestException as erro:
        return f"Ocorreu um erro ao consultar o OLLAMA: {erro}"

# Interface visual do Poco
#TADUÇÃO: “Crie uma página chamada Poco. Mostre uma caixa para o usuário fazer perguntas. Quando ele enviar uma pergunta, mostre-a na tela, peça uma resposta ao Ollama e exiba a resposta do Poco.”

def preparar_texto(texto):
     return texto.replace(r"\$", "$").replace("$", r"\$")

st.set_page_config(
    page_title="Poco - Assistente Financeiro",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="auto"
)

st.title("💰 Poco - Assistente Financeiro")
st.caption( 
    "Poco é um assistente de educação e organização financeira. "
    "Faça perguntas sobre gastos, orçamento e produtos financeiros. "
    "Projeto educacional com dados fictícios; não substitui orientação profissional."
    )    

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["papel"]):
        st.markdown(preparar_texto(mensagem["conteudo"]))

pergunta_ao_usuario = st.chat_input(
    "Faça ao Poco sobre seus gastos ou organização financeira..."
    )

if pergunta_ao_usuario:
    st.session_state.mensagens.append(
        {"papel": "user", 
         "conteudo": pergunta_ao_usuario}
    )

    with st.chat_message("user"):
        st.markdown(preparar_texto(pergunta_ao_usuario))

    with st.chat_message("assistant"):
         with st.spinner("Poco está pensando..."):
            resposta = perguntar_ao_poco(pergunta_ao_usuario)
            st.markdown(preparar_texto(resposta))

    st.session_state.mensagens.append({ 
        "papel": "assistant",
        "conteudo": resposta
    })