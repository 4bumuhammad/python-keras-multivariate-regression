import pandas as pd
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, 'data', 'boston_housing.csv')
data = pd.read_csv(data_path)

X = data.drop('MEDV', axis=1)
y = data['MEDV']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(X.shape[1],)))
model.add(Dense(64, activation='relu'))
model.add(Dense(1))

model.load_weights(os.path.join(BASE_DIR, 'models', 'multivariate_regression_model.keras'))

model.compile(optimizer='adam', loss='mean_squared_error')

predictions = model.predict(X_scaled)

print(predictions)
