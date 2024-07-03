from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np

# Predetermined tags and their clusters
predetermined_tags = {
    "basketball": 0,
    "football": 0,
    "rock music": 1,
    "pop music": 1,
    "movies": 2,
    "cinema": 2
}

# All tags (including those not predetermined)
tags = ["basketball", "football", "rock music", "pop music", "movies", "cinema"]

# Convert tags to numerical vectors using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(tags)

# Initialize labels with -1 (unassigned)
labels = np.full(len(tags), -1, dtype=int)

# Assign predetermined clusters
for i, tag in enumerate(tags):
    if tag in predetermined_tags:
        labels[i] = predetermined_tags[tag]

# Apply K-means clustering to remaining unassigned tags
unassigned_indices = np.where(labels == -1)[0]
if len(unassigned_indices) > 0:
    unassigned_tags = [tags[i] for i in unassigned_indices]
    unassigned_X = X[unassigned_indices]
    
    kmeans = KMeans(n_clusters=3, random_state=0)
    kmeans.fit(unassigned_X)
    unassigned_clusters = kmeans.labels_
    
    # Update labels with clusters for unassigned tags
    for idx, cluster in zip(unassigned_indices, unassigned_clusters):
        labels[idx] = cluster

# Print tags with assigned clusters
for tag, cluster in zip(tags, labels):
    print(f"Tag: {tag}, Cluster: {cluster}")