import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Chargement des données fictives
data = {
    "surface_m2": [70, 45, 90, 120, 60],
    "nb_pieces": [3, 2, 4, 5, 2],
    "quartier": ["Montparnasse", "Belleville", "Neuilly", "Bastille", "Montparnasse"],
    "prix_euros": [320000, 230000, 600000, 750000, 280000]
}

df = pd.DataFrame(data)

# Encodage des quartiers
label_encoder = LabelEncoder()
df["quartier"] = label_encoder.fit_transform(df["quartier"])

# Séparation des données
X = df.drop(columns=["prix_euros"])
y = df["prix_euros"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraînement du modèle
model = LinearRegression()
model.fit(X_train, y_train)

# Sauvegarde du modèle
joblib.dump(model, "app/model.joblib")
joblib.dump(label_encoder, "app/label_encoder.joblib")

print("✅ Modèle entraîné et sauvegardé avec succès !")
