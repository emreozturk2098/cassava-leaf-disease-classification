"""New portfolio illustration of the reported CS523 baseline recipe.
Not the missing original CS523 training code; no fitting or score reproduction.
"""
def make_classical_baseline():
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    from sklearn.linear_model import LogisticRegression
    return Pipeline([
        ("scaler", StandardScaler()),
        ("pca", PCA(n_components=0.95)),
        ("classifier", LogisticRegression(max_iter=1000)),
    ])
