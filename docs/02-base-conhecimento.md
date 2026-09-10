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

Essas informações ajudam o Poco a adaptar a linguagem e os exemplos ao contexto do cliente.

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
- Acompanhar metas de economia.

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

O aplicativo em Python carregará os arquivos CSV e JSON.

Antes de responder uma pergunta, o sistema enviará ao modelo:

1. As regras de comportamento do Poco.
2. O perfil fictício do cliente.
3. As transações disponíveis.
4. O histórico de atendimento.
5. As informações educativas sobre produtos financeiros.
6. A pergunta feita pelo usuário.

Dessa forma, o modelo terá contexto para responder de forma personalizada, educativa e segura.