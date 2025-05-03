
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

def load_youtube_data(file_path):
    return pd.read_csv(file_path)

def load_mood_data(file_path):
    return pd.read_csv(file_path)

def merge_datasets(yt_df, mood_df):
    return yt_df.merge(mood_df, on="date")

def preprocess_data(df):
    df = df.dropna()
    df["watch_late"] = df["hour"] >= 0  # e.g., watched after midnight
    df["class"] = df["mood_score"] >= 4
    return df

def run_classifiers(df, features, label):
    X = df[features]
    y = df[label]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    knn_preds = knn.predict(X_test)

    tree = DecisionTreeClassifier(random_state=42)
    tree.fit(X_train, y_train)
    tree_preds = tree.predict(X_test)

    return {
        "knn_acc": accuracy_score(y_test, knn_preds),
        "knn_cm": confusion_matrix(y_test, knn_preds).tolist(),
        "tree_acc": accuracy_score(y_test, tree_preds),
        "tree_cm": confusion_matrix(y_test, tree_preds).tolist()
    }
