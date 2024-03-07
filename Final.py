from tensorflow.keras.models import load_model
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt
#Load model
model = load_model('silver')
data = pd.read_csv('DataSilver.csv')

n = len(data['y'])
k =int (n*0.7852)
#Còn lại để test
X_test = data.iloc[k:,:6].values
Y_test = data.iloc[k:,6:].values

K = model.predict(X_test)
print(K)
#Tạo bảng
plt.plot(Y_test,color = 'green', label = 'Thực tế')
plt.plot(K,color = 'red', label = 'Dự đoán')
plt.title('Dự đoán giá Bạc')
plt.ylabel('Giá trị (USD)')
plt.grid()
plt.legend()
plt.show()