import pandas as pd
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, SpectralClustering, MeanShift, DBSCAN, Birch
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score, silhouette_score, homogeneity_score, completeness_score, v_measure_score

# Загрузка данных
wine_data = fetch_openml(name="wine", version=1, as_frame=True)
X = wine_data.data
y = wine_data.target.astype('int')

scaler = StandardScaler()
X = scaler.fit_transform(X)

models = {
    "KMeans": KMeans(n_clusters=3, random_state=42),
    "Agglomerative": AgglomerativeClustering(n_clusters=3),
    "Spectral": SpectralClustering(n_clusters=3, random_state=42, assign_labels='discretize'),
    "Birch": Birch(n_clusters=3),
    "MeanShift": MeanShift(),
    "DBSCAN": DBSCAN(eps=1.5, min_samples=5)
}

results = {}


for model_name, model in models.items():
    if model_name in ["MeanShift", "DBSCAN"]:  
        labels = model.fit_predict(X)
    else:  
        labels = model.fit_predict(X)

    silhouette = silhouette_score(X, labels) if len(set(labels)) > 1 else -1
    ari = adjusted_rand_score(y, labels)
    nmi = normalized_mutual_info_score(y, labels)
    homogeneity = homogeneity_score(y, labels)
    completeness = completeness_score(y, labels)
    v_measure = v_measure_score(y, labels)

    results[model_name] = {
        "Silhouette": silhouette,
        "Adjusted Rand Index (ARI)": ari,
        "Normalized Mutual Information (NMI)": nmi,
        "Homogeneity": homogeneity,
        "Completeness": completeness,
        "V-Measure": v_measure,
    }

for model_name, metrics in results.items():
    print(f"Metrics for {model_name}:")
    for metric_name, value in metrics.items():
        print(f"  {metric_name}: {value:.3f}")
    print()