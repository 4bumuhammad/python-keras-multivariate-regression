# helper_functions.py

# Fungsi bantuan tambahan
def some_function():
    pass

# Fungsi untuk plotting hasil
import matplotlib.pyplot as plt

def plot_results(actual, predicted):
    """
    Fungsi ini digunakan untuk memplot hasil prediksi.

    Parameters:
    actual (list): Daftar nilai aktual.
    predicted (list): Daftar nilai prediksi.

    Returns:
    None
    """
    plt.figure(figsize=(10, 6))
    plt.plot(actual, label='Actual', color='blue')
    plt.plot(predicted, label='Predicted', color='red')
    plt.title('Comparison of Actual vs Predicted')
    plt.xlabel('Data Points')
    plt.ylabel('Values')
    plt.legend()
    plt.show()
