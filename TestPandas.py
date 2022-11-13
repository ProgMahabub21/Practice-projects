import pandas as pd

#df = pd.read_csv('test1/student.csv')
df = pd.read_csv('test1/hotel_bookings.csv')
print(df)

#print first 5 rows
#print(df.head())
#print last 5 rows
#print(df.tail())

# print first 10 rows
#print(df.head(10))
# print last 10 rows
#print(df.tail(10))

#print(df.info())
# print insight of data
#print(df.describe())

# print column names
#print(df.columns)

# print index
#print(df.index)

#cleaning up the messy data

# print the number of missing values in each column
#print(df.isnull().sum())

# drop the missing values
df = df.dropna()

# modify wrong data format


#remove duplicate data
df = df.drop_duplicates()

#correct the wrong data

for  x in df.index:
    if df.loc[x, 'is_canceled'] == 0:
        df.loc[x, 'is_canceled'] = 'No'
    else:
        df.loc[x, 'is_canceled'] = 'Yes'

for x in df.index:
    if df.loc[x, 'hotel'] == 'Resort Hotel':
        df.loc[x, 'hotel'] = 'Resort'
    else:
        df.loc[x, 'hotel'] = 'City'

for x in df.index:
    if df.loc[x, 'lead_time'] > 300:
        df.loc[x, 'lead_time'] = 'Very Long'
    else:
        df.loc[x, 'lead_time'] = 'Ok'


print(df)
