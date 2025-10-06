import numpy as np
from sklearn.model_selection import cross_val_score, KFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification

# 1. Gerando um dataset de exemplo
# 1000 amostras, 20 features, 2 classes
X, y = make_classification(n_samples=1000, n_features=20, n_informative=5, n_redundant=0, random_state=42)

# 2. Criando o modelo
modelo = DecisionTreeClassifier(random_state=42)

# 3. Configurando a Validação Cruzada (k-fold CV)
# Dados em 5 'folds' (k=5)
# shuffle=True garante que os dados sejam embaralhados antes da divisão
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# 4. Executando a Validação Cruzada
# A função 'cross_val_score' cuida de todo o processo iterativo 
# treina, testa e armazena os scores de acurácia para cada um dos 5 folds
scores = cross_val_score(modelo, X, y, cv=kf, scoring='accuracy')

# 5. Analisando os Resultados
print(f"Scores de acurácia para cada um dos 5 folds: \n{scores}")
print(f"\n- Acurácia Média: {np.mean(scores):.4f}")
print(f"- Desvio Padrão da Acurácia: {np.std(scores):.4f}")
