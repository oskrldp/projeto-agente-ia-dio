# 💰 Poco — Assistente de Educação e Organização Financeira

Poco é um protótipo educacional que ajuda jovens e adultos de 18 a 40 anos
a compreender seus gastos, com linguagem simples, objetiva e sem julgamentos.

O projeto combina cálculos em Python com explicações geradas por uma
inteligência artificial local, executada pelo Ollama.

Desenvolvido a partir do desafio de agente financeiro da DIO.

## O que o Poco faz

- Apresenta um resumo das entradas e saídas registradas.
- Calcula o total de despesas com alimentação.
- Explica conceitos de organização financeira, como orçamento mensal.
- Responde a perguntas com base nos dados fictícios fornecidos.
- Apresenta avisos programados para perguntas sobre senhas e determinadas
  solicitações de indicação de investimentos.

O protótipo não possui integração bancária e não realiza pagamentos
ou transferências. Não substitui orientação profissional.

## Como funciona

Existem dois caminhos para responder:

1. **Python:** algumas perguntas reconhecidas acionam cálculos com Decimal
   ou avisos prontos, sem consultar o modelo.
2. **IA local:** as demais perguntas são enviadas ao Ollama com as instruções
   do Poco e o contexto dos dados fictícios.

O histórico aparece na interface, mas a implementação atual envia ao modelo
apenas a pergunta atual e o contexto, não toda a conversa anterior.

## Tecnologias

- Python
- Streamlit — interface de chat
- pandas — leitura e organização das tabelas
- requests — comunicação com o Ollama
- Decimal — cálculos decimais
- Ollama com o modelo `qwen3:4b`

## Dados utilizados

Todos os dados do exemplo são fictícios.

| Arquivo | Conteúdo |
|---|---|
| `data/transacoes.csv` | Entradas e saídas do cliente fictício |
| `data/perfil_investidor.json` | Perfil, objetivos e informações financeiras |
| `data/historico_atendimento.csv` | Atendimentos anteriores simulados |
| `data/produtos_financeiros.json` | Informações de exemplo sobre produtos financeiros |

As transações fornecidas abrangem outubro de 2025.
Informações sobre produtos são material de exemplo, não cotações atualizadas.

## Como executar no Windows

### 1. Preparação

Instale Python e Ollama. Baixe este repositório e abra a pasta do projeto
no VS Code.

No terminal, execute:

```powershell
ollama pull qwen3:4b
```

Se o modelo já estiver instalado, não é necessário baixá-lo novamente.
Mantenha o Ollama em execução.

### 2. Ambiente Python

Na raiz do projeto, crie o ambiente virtual:

```powershell
py -m venv .venv
```

Instale as dependências:

```powershell
.\.venv\Scripts\python.exe -m pip install -r src/requirements.txt
```

### 3. Iniciar a aplicação

```powershell
.\.venv\Scripts\python.exe -m streamlit run src/app.py
```

Abra o endereço `Local URL` indicado no terminal.
Mantenha o terminal aberto durante o uso.

A aplicação espera o Ollama em `http://localhost:11434/api/generate`.
O modelo configurado em `src/app.py` deve ser `qwen3:4b`.

Para encerrar a aplicação, pressione Ctrl + C no terminal.

## Perguntas para experimentar

### Consultas calculadas pelo Python

- Mostrar resumo financeiro
- Quanto gastei com alimentação?

Essas consultas consideram toda a base disponível, sem filtro de mês.

### Perguntas educativas e de validação

- O que é um orçamento mensal? Explique de forma simples.
- Quanto gastei com alimentação em dezembro de 2025?
- Posso te passar minha senha do banco para você consultar meu saldo?
- Qual ação devo comprar hoje? Escolha uma para mim e garanta que vou lucrar.

Não forneça senhas ou dados pessoais reais durante os testes.

## Resultados observados

Com a base fornecida:

| Consulta | Resultado |
|---|---|
| Total de entradas | 5.000,00 reais |
| Total de saídas | 2.488,90 reais |
| Diferença entre entradas e saídas | 2.511,10 reais |
| Alimentação | 570,00 reais em 2 lançamentos |

A diferença entre entradas e saídas não representa saldo bancário real:
não considera saldo inicial nem movimentações fora da base.

As consultas programadas responderam sem demora perceptível nos testes.
Respostas da IA levaram aproximadamente 23 a 60 segundos em execuções recentes.

Esses tempos são estimativas manuais, não um benchmark controlado.
O computador utilizado tinha uma AMD Radeon RX 6600 com 8 GB de memória
dedicada e aproximadamente 16 GB de RAM.

## Limitações

- O modelo pode cometer erros e desobedecer às instruções do prompt.
- As proteções por palavras e frases não abrangem todas as formulações.
- Perguntas numéricas fora das consultas programadas ainda podem ser
  calculadas incorretamente pela IA.
- Os cálculos diretos ainda não oferecem filtros por mês.
- A IA apresentou interpretações incorretas sobre a reserva financeira.
- O tempo de resposta depende do computador e da pergunta.
- Ainda não houve avaliação com usuários externos.
- O protótipo não deve ser tratado como um sistema financeiro de produção.

## Melhorias futuras

- Ampliar cálculos para outras categorias.
- Implementar filtros por período.
- Melhorar a interpretação de metas e valores disponíveis.
- Ampliar os testes de segurança e de diferentes formas de perguntar.
- Reduzir a latência.
- Avaliar clareza e utilidade com outros usuários.

## Documentação

A pasta `docs` contém:

- `01-documentacao-agente.md` — objetivo, personalidade e arquitetura.
- `02-base-conhecimento.md` — organização dos dados.
- `03-prompts.md` — instruções do agente.
- `04-metricas.md` — testes, resultados e limitações.
- `05-pitch.md` — roteiro e link da apresentação.

## Demonstração em vídeo

[\[Assistir ao pitch do Poco\] ](https://drive.google.com/file/d/1w5QatXCpfgJMb9-GuZq0Dk1gL1O0g_qG/view?usp=sharing)

## Créditos

Projeto educacional desenvolvido a partir da estrutura e dos dados
de exemplo disponibilizados pela DIO.