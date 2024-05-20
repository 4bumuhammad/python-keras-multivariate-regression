# predict.py
import joblib
from models.prediction_model import predict

# Memuat model yang sudah dilatih
model = joblib.load('trained_model.pkl')

# Membuat prediksi menggunakan model
prediction = predict(model)

print(prediction)
