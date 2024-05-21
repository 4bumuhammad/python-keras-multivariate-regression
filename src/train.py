import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(BASE_DIR, 'data', 'boston_housing.csv')
data = pd.read_csv(data_path)

X = data.drop('MEDV', axis=1)
y = data['MEDV']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(64, activation='relu'))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')

checkpoint_path = os.path.join(BASE_DIR, 'models', 'multivariate_regression_model.keras')
checkpoint_dir = os.path.dirname(checkpoint_path)
cp_callback = ModelCheckpoint(filepath=checkpoint_path, save_best_only=True, verbose=1, save_weights_only=False)

model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2, callbacks=[cp_callback])

loss = model.evaluate(X_test, y_test)
print(f'Test loss: {loss}')