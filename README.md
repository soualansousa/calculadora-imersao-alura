# 🧮 Calculadora Simples em Python

Uma aplicação simples e funcional desenvolvida em Python para executar as quatro operações aritméticas básicas: **soma**, **subtração**, **multiplicação** e **divisão**.

---

### ⚠️ Aviso Importante

> Este projeto foi desenvolvido como parte dos desafios práticos da **Imersão Engenharia de Software na era dos agentes de IA**, promovida pela **Alura** (Grupo Alura) em parceria com o **Google for Startups**.
> 
> A proposta da imersão é construir e evoluir projetos reais de software utilizando agentes de inteligência artificial em cada etapa do ciclo de desenvolvimento, com ferramentas como o **Google AI Studio** e ecossistema Google. Afinal, com o crescimento acelerado dos agentes de IA, a Engenharia de Software está sendo ativamente reescrita — e essas transformações estão apenas no começo!

---

## ⚙️ Principais Componentes do Código

Os elementos centrais do projeto são as **funções**, que atuam como blocos modulares responsáveis por tarefas bem definidas. A calculadora possui:

- `somar(a, b)`: Retorna a soma de dois números.
- `subtrair(a, b)`: Retorna a diferença entre dois números.
- `multiplicar(a, b)`: Retorna o produto da multiplicação de dois valores.
- `dividir(a, b)`: Retorna a divisão, incluindo validação contra divisão por zero.

Cada função recebe dois parâmetros numéricos e devolve o resultado da respectiva operação matemática.

---

## 📥 Entrada de Dados e Seleção da Operação

A interação com o usuário ocorre por meio da função nativa `input()`:
1. **Escolha da Operação:** O usuário digita a opção numérica referente à operação matemática ou ao encerramento do programa.
2. **Coleta de Números:** Os valores informados são armazenados em variáveis e, em seguida, passados como parâmetros para a função matemática correspondente.

---

## 🧠 Lógica de Programação e Fluxo

A execução do programa é orientada pelas seguintes estruturas de controle:

- **Laço de Repetição (`while`):** Mantém o menu ativo para que o usuário possa realizar múltiplos cálculos consecutivamente sem precisar reiniciar a aplicação. O loop só é interrompido quando a opção de saída (`0`) é selecionada (`break`).
- **Tratamento de Exceções (`try / except`):** Valida se as entradas informadas pelo usuário são realmente números (`float`). Se letras ou caracteres inválidos forem inseridos, o programa captura o erro amigavelmente (`ValueError`), impedindo que o script feche abruptamente.
- **Estruturas Condicionais (`if / elif / else`):**
  - Checam se a opção escolhida no menu é válida (entre 0 e 4).
  - Direcionam o fluxo para acionar a operação matemática correspondente e exibir o resultado final na tela.

---

## 🚀 Como Executar

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Abra o terminal na pasta do projeto e execute:

```bash
python calculadora.py