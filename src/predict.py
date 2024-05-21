import pandas as pd
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
import os

# Define base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Load dataset
data_path = os.path.join(BASE_DIR, 'data', 'boston_housing.csv')
data = pd.read_csv(data_path)

# Split features and target variable
X = data.drop('MEDV', axis=1)
y = data['MEDV']

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Load the model architecture
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(X.shape[1],)))
model.add(Dense(64, activation='relu'))
model.add(Dense(1))

# Load the trained weights
model.load_weights(os.path.join(BASE_DIR, 'models', 'multivariate_regression_model.keras'))

# Compile the model (necessary for prediction)
model.compile(optimizer='adam', loss='mean_squared_error')

# Make predictions
predictions = model.predict(X_scaled)

# Print predictions
print(predictions)
