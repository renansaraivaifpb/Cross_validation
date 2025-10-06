1. Dividir: O conjunto de dados original é dividido em k subconjuntos de tamanho (geralmente) igual. Um valor comum para k é 5 ou 10.

2. Iterar: O processo é repetido k vezes. A cada iteração:

- Um dos subconjuntos é separado para ser o conjunto de validação (ou teste).

- Os outros k-1 subconjuntos são combinados para formar o conjunto de treinamento.

- Um novo modelo é treinado com os dados de treinamento e avaliado com os dados de validação.

3. Calcular a Média: Ao final das k iterações, teremos k scores de desempenho (como a acurácia). A métrica de performance final do modelo é a média desses k scores.

---

Isso garante que cada amostra de dados foi usada tanto para treinamento quanto para validação, resultando em uma estimativa de desempenho muito mais confiável e menos dependente da sorte na divisão dos dados.

---

Scores de acurácia para cada um dos 5 folds: 
[0.89  0.915 0.88  0.86  0.86 ]

- Acurácia Média: 0.8810
- Desvio Padrão da Acurácia: 0.0206
