from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Charger le modèle et l'encodeur
model = joblib.load("app/model.joblib")
label_encoder = joblib.load("app/label_encoder.joblib")

@app.get("/")
def home():
    return {"message": "API de prédiction des prix immobiliers 🚀"}

@app.post("/predict")
def predict(surface_m2: float, nb_pieces: int, quartier: str):
    # Transformer le quartier en format numérique
    quartier_encoded = label_encoder.transform([quartier])[0]

    # Créer un DataFrame pour la prédiction
    input_data = pd.DataFrame([[surface_m2, nb_pieces, quartier_encoded]],
                              columns=["surface_m2", "nb_pieces", "quartier"])

    # Prédire le prix
    prediction = model.predict(input_data)[0]
    
    return {"prix_prédit": round(prediction, 2)}
