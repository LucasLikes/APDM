# Sistemas Inteligentes de Pré-Diagnóstico de Diabetes

O diabetes afeta 10,2% da população brasileira, de acordo com dados da pesquisa Vigitel Brasil 2023 (Vigilância de Fatores de Risco e Proteção para Doenças Crônicas por Inquérito Telefônico). Esse índice representa um aumento em relação a 2021, quando era de 9,1%. O último inquérito Vigitel também mostra que o diagnóstico é mais frequente entre as mulheres (11,1%) do que entre os homens (9,1%).

## Objetivo

Este projeto visa criar um sistema capaz de pré-diagnosticar a possibilidade de uma pessoa ser reagente ao diabetes com base em uma série de resultados, como exames de check-up geral. Para isso, utilizamos os seguintes campos: GLICOSE, PRESSÃO SANGUÍNEA, ÍNDICE DE MASSA CORPORAL e IDADE.

## Motivação dos Campos Selecionados

- **GLICOSE**: A glicemia em jejum varia de 70 mg/dl a 100 mg/dl em um estado normal. Uma pessoa é classificada como pré-diabética quando a medição da glicemia em jejum está entre 100 e 125 mg/dl. Aquelas que atingem 126 mg/dl ou mais são consideradas diabéticas.
  
- **PRESSÃO SANGUÍNEA**: O diabetes pode causar o desenvolvimento de hipertensão, já que a resistência à insulina dificulta o acesso das células à glicose circulante. Isso eleva os níveis de açúcar no sangue, contribuindo para o endurecimento das artérias e o aumento da pressão arterial.

- **ÍNDICE DE MASSA CORPORAL (IMC)**: O excesso de peso (sobrepeso e/ou obesidade) está presente em grande parte dos pacientes com DM2. Na população diabética, um IMC acima de 25,0 kg/m² aumenta a probabilidade de desenvolver doenças cardiovasculares.

- **IDADE**: Embora crianças e adolescentes também possam desenvolver o Diabetes Tipo 2, a maior incidência está em pessoas com mais de 40 anos. Além da hereditariedade e da obesidade, o envelhecimento também está associado ao desenvolvimento da doença.

## Escolha do Algoritmo

Para a construção deste sistema de aprendizado de máquina, optamos pelo algoritmo de Regressão Linear. A regressão linear é uma técnica de análise de dados que prevê o valor de dados desconhecidos usando outro valor de dados relacionado e conhecido. Ela modela matematicamente a variável desconhecida ou dependente e a variável conhecida ou independente como uma equação linear. No nosso caso, utiliza os dados conhecidos (GLICOSE, PRESSÃO SANGUÍNEA, ÍNDICE DE MASSA CORPORAL e IDADE) para calcular uma variável que, ao ser calculada, o sistema pode prever a possibilidade de o paciente ter ou não diabetes.

##Desenvolvido por:
- **CRISTIAN LEMES RA: 2020101531
- **JOÃO HENRIQUE DUARTE HEINDYK RA: 2021103830
- **VINICIUS ANDRÉ FROGGEL DE MIRANDA RA: 2021102573
- **LUCAS GABRIEL LIKES RA: 2021206275
