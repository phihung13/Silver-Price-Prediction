import pandas as pd

#Chuẩn bị Data
df = pd.read_csv("SilverHistoricalData.csv")
print(df)

#Khởi tạo biến
E = []
price = []

#Chiều dài df
l = len(df['Price'])
print(l)

#Tạo giá trị cho E[]
for j in range(l):
    E.append(j)

#Chèn E vào df
df['E'] = E
print(df)

#Sắp xếp cột E, ascending = False: giảm dần
df_reverse = df.sort_values(by = ['E'], ascending = False)
print(df_reverse)

#Đưa giá trị từ df_reverse['Price'] vào price[]
for i in df_reverse['Price']:
    price.append(i)
print(price)

#Tạo file data.csv
df=pd.DataFrame()
df['x6']= price[0:(l-6)]
df['x5']= price[1:(l-5)]
df['x4']= price[2:(l-4)]
df['x3']= price[3:(l-3)]
df['x2']= price[4:(l-2)]
df['x1']= price[5:(l-1)]
df['y'] = price[6:l]
df.to_csv('DataSilver.csv',index=False)