# Simulador de Navegação de Submarino

Este é um projeto acadêmico desenvolvido em Python, inspirado no último exercício da minha primeira prova na faculdade. Gostei tanto do desafio proposto que decidi aprimorar o código e documentá-lo aqui. O projeto é focado em lógica de programação, manipulação de matrizes e controle de estados. O objetivo do simulador é navegar com um submarino por uma fossa oceânica até encontrar a caixa-preta, gerenciando o oxigênio e evitando as paredes do mapa.

## Tecnologias e Conceitos Aplicados
* **Python 3**
* **Processamento via CLI (Command Line Interface)**
* **Simulação de ambiente discreto (Matriz 10x10)**
* **Validação de limites (Boundary checking)**
* **Estruturas de Controle (Match-Case, Loops, Condicionais)**

## Como jogar
O mapa é renderizado no terminal, onde:
* `S` = Submarino
* `C` = Caixa-preta (Objetivo)
* `~` = Água livre

**Controles:**
* `W` - Move para Cima
* `S` - Move para Baixo
* `A` - Move para Esquerda
* `D` - Move para Direita
* `emergencia` - Aborta a missão

A cada movimento válido, 1 unidade de oxigênio é consumida. Se você bater nas bordas do mapa, o movimento é bloqueado, mas não gasta oxigênio. Encontre a caixa `C` antes que seu estoque chegue a zero!
