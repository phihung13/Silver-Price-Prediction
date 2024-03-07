import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

#Chuẩn bị Data
data = pd.read_csv("DataSilver.csv")
print(data)
n = len(data['y'])
print(n)

#Lấy 78,52% để train
k =int (n*0.7852)
print(k)

#Data train
X_train = data.iloc[:k,:6].values #từ 1 đến 2200
Y_train = data.iloc[:k,6:].values
print(X_train.shape)

#chuẩn bị mô hình AI
model = Sequential()
model.add(Dense(50, input_shape = (6,), activation='tanh'))
model.add(Dense(50, activation ='tanh'))
model.add(Dense(1, activation = "linear"))
print(model.summary()) #thông tin mô hình

#biên dịch model, loss function = mse, opt = adam
model.compile(loss='mse', optimizer='Adam')

#huấn luyện mô hình, train 100 lần, bs = 22
model.fit(X_train, Y_train, epochs=100, batch_size=22)
#Lưu file
model.save('Silver')