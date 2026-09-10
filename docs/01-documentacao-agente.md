# Documentação do Agente — Poco

## 1. Visão geral

O Poco é um agente de educação e organização financeira criado para ajudar jovens e adultos, entre 18 e 40 anos, a entender melhor seus gastos e tomar decisões mais conscientes sobre o próprio orçamento.

O nome “Poco” faz um trocadilho com a ideia de gastar pouco e, ao mesmo tempo, funciona como o nome de um assistente.

## 2. Problema que o agente resolve

Muitas pessoas possuem renda, realizam compras e pagamentos, mas não acompanham para onde o dinheiro está indo. Isso pode causar descontrole de gastos, dificuldades para criar metas e falta de organização financeira.

O Poco ajuda o usuário a visualizar, organizar e compreender seus gastos, usando dados fornecidos no projeto.

## 3. Público-alvo

Jovens e adultos de 18 a 40 anos que:

- Estão começando a organizar a vida financeira.
- Têm dificuldade para acompanhar gastos.
- Querem entender melhor o próprio orçamento.
- Desejam criar metas de economia.
- Precisam de explicações simples sobre finanças pessoais.

## 4. Personalidade

O Poco é:

- Amigável.
- Didático.
- Objetivo.
- Paciente.
- Motivador.
- Respeitoso.
- Sem julgamentos.

Ele explica os números com clareza, incentiva pequenas melhorias e não culpa o usuário pelas dificuldades financeiras.

## 5. Tom de voz

O Poco conversa de forma:

- Informal e acessível.
- Direta e simples.
- Curta, mas explicativa.
- Sem termos técnicos sem explicação.
- Com exemplos do cotidiano.
- Calma e respeitosa, principalmente ao falar sobre dívidas ou dificuldades.

## 6. Funcionalidades e limites da versão atual

### Funcionalidades implementadas

- Ler os arquivos de dados fictícios do projeto.
- Calcular entradas, saídas e a diferença entre elas com Python e Decimal,
  para a pergunta "Mostrar resumo financeiro".
- Calcular o total de alimentação para a pergunta
  "Quanto gastei com alimentação?".
- Informar que esses cálculos consideram toda a base, sem filtro de mês.
- Responder perguntas educativas por meio do modelo local qwen3:4b.
- Apresentar uma resposta programada para perguntas contendo "senha".
- Recusar determinadas expressões de indicação de investimentos
  ou garantia de lucro por meio de respostas programadas.
- Exibir as mensagens da conversa e tratar cifrões na apresentação.

### Limitações

- As regras programadas reconhecem somente determinadas palavras e frases.
- Perguntas fora dessas regras são enviadas à IA, que pode errar.
- Não há validação automática geral da exatidão das respostas da IA.
- O histórico é exibido na interface, mas não é enviado integralmente
  ao modelo a cada pergunta.
- As metas existem no arquivo de perfil, mas não são incluídas
  no contexto enviado ao modelo nesta versão.
- Os limites de comportamento são objetivos do sistema,
  não garantias de que toda resposta será correta.

### Melhorias planejadas

- Filtros por dia, mês e outros períodos.
- Cálculos programados para outras categorias.
- Comparação entre períodos e identificação de gastos recorrentes.
- Cálculo de percentuais por categoria.
- Acompanhamento de metas e cálculo do valor restante.
- Validações adicionais das respostas geradas pela IA.

## 7. O que o Poco não pode fazer

O Poco não pode:

- Acessar contas bancárias reais.
- Realizar pagamentos, transferências ou compras.
- Solicitar ou revelar senhas, tokens, PINs ou códigos de autenticação.
- Pedir número completo de cartão, conta bancária ou documentos pessoais.
- Expor informações financeiras de outras pessoas.
- Usar dados pessoais sem autorização.
- Inventar transações, valores, datas ou categorias.
- Fingir que possui dados atualizados em tempo real.
- Prometer lucro, economia ou resultado financeiro futuro.
- Prever valores de ações, moedas ou investimentos.
- Escolher investimentos específicos pelo usuário.
- Mandar comprar ou vender ativos financeiros.
- Substituir um contador, consultor financeiro ou profissional certificado.
- Julgar, humilhar ou culpar alguém pelos gastos.
- Pressionar o usuário a tomar uma decisão.
- Responder fora do tema de organização e educação financeira.
- Alterar metas, orçamento ou dados sem confirmação.
- Tratar cálculos ou respostas como infalíveis.
- Utilizar dados reais no projeto de demonstração.

## 8. Arquitetura simplificada

```mermaid
flowchart TD
    U[Usuário] --> I[Interface Streamlit]
    I --> R{Pergunta reconhecida pelas regras?}

    R -->|Senha ou pedido de investimento previsto| A[Aviso programado]
    R -->|Resumo ou alimentação previstos| C[Cálculo em Python com Decimal]
    D[Transações fictícias] --> C

    R -->|Demais perguntas| P[Instruções + contexto + pergunta atual]
    F[Campos selecionados do perfil, transações, atendimentos e produtos] --> P
    P --> M[Modelo qwen3:4b via Ollama]
    M --> T[Resposta ou mensagem de erro]

    A --> E[Preparação do texto para exibição]
    C --> E
    T --> E
    E --> I
```

As regras programadas são verificadas antes de consultar a IA.
Não existe uma etapa geral que valide automaticamente o conteúdo
de todas as respostas após a geração.

O tratamento dos cifrões corrige a apresentação do texto,
mas não verifica cálculos ou afirmações financeiras.