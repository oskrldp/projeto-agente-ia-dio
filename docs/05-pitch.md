# Pitch do Poco — Assistente Financeiro

## 1. O problema — 30 segundos

Muitas pessoas têm dificuldade para entender para onde o dinheiro
está indo. Pensando em jovens e adultos de 18 a 40 anos que estão
começando a organizar suas finanças, desenvolvi o Poco:
um assistente que explica gastos de maneira simples,
objetiva e sem julgamentos.

## 2. A solução — 1 minuto

O Poco combina Python, uma interface em Streamlit e um modelo
de inteligência artificial executado localmente pelo Ollama.

Neste protótipo, utilizo dados fictícios. O agente não acessa
contas bancárias nem realiza movimentações financeiras.

Durante os testes, percebi que a inteligência artificial podia
errar cálculos. Por isso, passei o resumo financeiro e o total
de alimentação para funções em Python, usando Decimal.

A IA continua responsável por explicações educativas.
Também acrescentei respostas programadas para algumas perguntas
sobre senhas e pedidos de indicação de investimentos.

## 3. Demonstração — 1 minuto

[Mostrar a pergunta “Mostrar resumo financeiro”.]

Aqui, o Poco calcula 5.000 reais de entradas e 2.488 reais
e 90 centavos de saídas. A diferença é de 2.511 reais
e 10 centavos. Ele esclarece que isso não é o saldo bancário real.

[Mostrar “Quanto gastei com alimentação?”.]

Nesta consulta, ele encontra 570 reais em dois lançamentos.

[Mostrar a pergunta sobre compartilhar senha, sem digitar senha real.]

Aqui, ele orienta a não compartilhar senhas e explica que não
acessa contas bancárias.

[Mostrar uma resposta educativa já carregada.]

Esta explicação sobre orçamento foi gerada anteriormente pela IA.
As respostas educativas demoram mais que os cálculos programados.

## 4. Diferencial e impacto — 30 segundos

O diferencial do Poco é combinar explicações em linguagem simples
com cálculos programados e limites explícitos.

O objetivo é apoiar a educação financeira, sem substituir
orientação profissional. Nos testes recentes, a IA levou cerca
de 23 a 60 segundos e ainda apresentou erros.

Os próximos passos são ampliar os filtros por período,
melhorar o desempenho e avaliar o projeto com outros usuários.

## Checklist do pitch

- [ ] Duração máxima de 3 minutos
- [ ] Problema claramente definido
- [ ] Solução demonstrada na prática
- [ ] Diferencial e limitações explicados
- [ ] Áudio compreensível e tela legível
- [ ] Nenhum dado pessoal ou senha exposto
- [ ] Link acessível ao avaliador

## Link do vídeo

https://drive.google.com/file/d/1w5QatXCpfgJMb9-GuZq0Dk1gL1O0g_qG/view?usp=sharing