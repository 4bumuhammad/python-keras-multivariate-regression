# train.py
from data.data_loader import load_data
from models.prediction_model import train_model

# Memuat dan memproses data
data = load_data()

# Melatih model prediksi
trained_model = train_model(data)

# Menyimpan model yang sudah dilatih
import joblib
joblib.dump(trained_model, 'trained_model.pkl')
