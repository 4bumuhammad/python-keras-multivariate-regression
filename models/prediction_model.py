# prediction_model.py
from sklearn.linear_model import LinearRegression

# Kode untuk definisi dan pelatihan model prediksi
def train_model(data):
    # Mengambil fitur dari data
    features = ['usia', 'jenis_kelamin', 'berat_badan', 'tinggi_badan']
    X = data[features]
    
    # Mengambil target dari data
    target = ['warna_kesukaan', 'hobi', 'makanan_kesukaan', 'belajar_di_sekolah', 'emosi']
    y = data[target]
    
    # Membuat dan melatih model
    model = LinearRegression()
    model.fit(X, y)
    
    return model

def predict(model):
    # Contoh prediksi
    # Anda dapat menyediakan input secara dinamis
    input_data = [[12, 'L', 33, 128]]
    prediction = model.predict(input_data)
    return prediction
