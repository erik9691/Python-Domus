from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np

# Es posible predeterminar tags y sus clusters, con el objetivo de agrupar tags relacionados en los mismos grupos 
predetermined_tags = {
    "basketball": 0,
    "football": 0,
    "rock music": 1,
    "pop music": 1,
    "movies": 2,
    "cinema": 2
}

# Todas las tags existentes
tags = ["basketball", "football", "rock music", "pop music", "movies", "cinema"]

# Convertimos los tags a sus variables numericas con los tags predeterminados, vectorizandolos
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(tags)

# Inicializar tags con vector -1 (aquellos que no fueron asignados a los demas por error o excepciones)
labels = np.full(len(tags), -1, dtype=int)

# Asignamos cada tag a su cluster, se forman los clusters a partir de los indices.
for i, tag in enumerate(tags):
    if tag in predetermined_tags:
        labels[i] = predetermined_tags[tag]

# Utiliza K-means (clustering prototipado u aproximado) el cual intenta asignar los tags no definidos a algun cluster de los que tenemos
unassigned_indices = np.where(labels == -1)[0]
if len(unassigned_indices) > 0:
    unassigned_tags = [tags[i] for i in unassigned_indices]
    unassigned_X = X[unassigned_indices]
    
    kmeans = KMeans(n_clusters=3, random_state=0)
    kmeans.fit(unassigned_X)
    unassigned_clusters = kmeans.labels_
    
    for idx, cluster in zip(unassigned_indices, unassigned_clusters):
        labels[idx] = cluster

# Imprime los resultados
for tag, cluster in zip(tags, labels):
    print(f"Tag: {tag}, Cluster: {cluster}")