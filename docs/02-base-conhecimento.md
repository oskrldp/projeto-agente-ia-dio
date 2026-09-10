# Base de Conhecimento — Poco

## 1. Visão geral

A base de conhecimento do Poco é composta por dados financeiros fictícios. Esses dados são usados para personalizar as respostas, analisar gastos e explicar conceitos de organização financeira.

Nenhum dado bancário real, senha, cartão ou informação pessoal sensível é utilizado neste projeto.

## 2. Arquivos utilizados

| Arquivo | Conteúdo | Utilidade para o Poco |
|---|---|---|
| `data/perfil_investidor.json` | Perfil, renda, objetivos, patrimônio, reserva e metas do cliente fictício | Personalizar explicações e entender o contexto financeiro |
| `data/transacoes.csv` | Entradas e saídas financeiras, com data, descrição, categoria e valor | Analisar gastos, categorias e orçamento |
| `data/historico_atendimento.csv` | Atendimentos fictícios anteriores, com temas e resumos | Considerar assuntos já tratados anteriormente |
| `data/produtos_financeiros.json` | Informações gerais sobre produtos financeiros | Explicar conceitos e características de produtos sem recomendar investimentos |

## 3. Dados do perfil

O arquivo `perfil_investidor.json` apresenta o perfil fictício do cliente.

Ele contém informações como:

- Nome.
- Idade.
- Profissão.
- Renda mensal.
- Perfil de investidor.
- Objetivo principal.
- Patrimônio total.
- Reserva de emergência.
- Aceitação de risco.
- Metas financeiras.

Nem todos esses campos são enviados ao modelo na versão atual.

O contexto inclui nome, idade, perfil de investidor, objetivo principal,
patrimônio total e reserva de emergência atual.

Profissão, renda mensal, aceitação de risco e a lista de metas
existem no JSON, mas não são incluídas diretamente no contexto.

A renda pode aparecer também nas transações, como um lançamento
de salário. Isso não significa que o campo renda_mensal do perfil
esteja sendo enviado.

A versão atual não implementa acompanhamento de metas.

## 4. Dados de transações

O arquivo `transacoes.csv` registra movimentações financeiras fictícias.

Cada transação possui:

- Data.
- Descrição.
- Categoria.
- Valor.
- Tipo: entrada ou saída.

O Poco utiliza essas informações para:

- Somar gastos.
- Identificar categorias com maior despesa.
- Comparar entradas e saídas.
- Criar resumos financeiros.
- Apoiar o planejamento de orçamento.
- Fornecer dados para explicações educativas; o acompanhamento
de metas é uma melhoria planejada.

Exemplo de teste esperado: os gastos com alimentação somam R$ 570,00, considerando supermercado e restaurante.

## 5. Histórico de atendimento

O arquivo `historico_atendimento.csv` registra conversas fictícias anteriores.

Ele possui:

- Data do atendimento.
- Canal utilizado.
- Tema.
- Resumo.
- Status de resolução.

Esses dados permitem que o Poco considere quais assuntos já foram explicados e mantenha uma conversa mais coerente.

## 6. Produtos financeiros

O arquivo `produtos_financeiros.json` contém informações educativas sobre produtos financeiros.

O Poco pode explicar características como:

- Categoria.
- Risco.
- Liquidez.
- Valor mínimo.
- Forma de rentabilidade.
- Indicação geral.

O Poco não recomenda a compra de produtos específicos. Ele apenas explica conceitos e fatores que o usuário deve compreender antes de tomar uma decisão.

## 7. Privacidade e segurança

A base foi criada apenas para fins educacionais e utiliza dados fictícios.

O Poco deve:

- Usar os dados fornecidos apenas para responder perguntas relacionadas ao projeto.
- Não solicitar dados bancários reais.
- Não solicitar senhas, códigos ou documentos.
- Não inventar informações que não estejam disponíveis.
- Informar quando os dados forem insuficientes.
- Não compartilhar informações de um cliente com outro.
- Não utilizar os dados para realizar operações financeiras.

## 8. Estratégia de uso no aplicativo

O aplicativo carrega os arquivos CSV e JSON, mas o conteúdo enviado
à IA depende do contexto montado no código.

### Perguntas respondidas sem consultar a IA

- Resumo financeiro: cálculo das entradas, saídas e diferença em Python.
- Alimentação: cálculo das despesas dessa categoria em Python.
- Senhas: aviso programado quando a palavra é identificada.
- Investimentos: recusa programada para determinadas expressões.

Os cálculos diretos utilizam todas as transações disponíveis,
sem filtro de mês.

### Perguntas encaminhadas ao modelo

Para as demais perguntas, o aplicativo envia:

1. As instruções de comportamento do Poco.
2. Campos selecionados do perfil: nome, idade, perfil de investidor,
   objetivo principal, patrimônio total e reserva atual.
3. A tabela de transações.
4. O histórico fictício de atendimentos.
5. As informações de exemplo sobre produtos financeiros.
6. A pergunta atual do usuário.

A lista de metas do JSON não é enviada nesta versão.
Portanto, o agente não deve afirmar que uma meta foi atingida
sem informações suficientes.

O histórico fictício de atendimentos é diferente do histórico
do chat: as mensagens anteriores da sessão aparecem na interface,
mas não são enviadas integralmente ao modelo.

O contexto auxilia a geração das respostas, mas não garante
sua exatidão. A IA ainda pode interpretar dados incorretamente.

### Evolução planejada

- Incluir metas de forma explícita no contexto.
- Calcular o progresso das metas em Python.
- Implementar filtros de categoria e período.
- Selecionar somente os dados necessários para cada pergunta.