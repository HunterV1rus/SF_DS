import pandas as pd
import os
import sys


melb_data = pd.read_csv(sys.path[0] + '/data/melb_data.csv', sep = ',')
ufo_data = pd.read_csv(sys.path[0] + '/data/ufo.csv', sep = ',')

melb_df = melb_data.copy()

melb_df['Date'] = pd.to_datetime(melb_df['Date'], dayfirst=True)
ufo_data['Time'] = pd.to_datetime(ufo_data['Time'], dayfirst=True)

melb_df['WeekDaySale'] = melb_df[(melb_df['Date'].dt.dayofweek == 5) | (melb_df['Date'].dt.dayofweek == 6)]['Date']
#print(melb_df['WeekDaySale'].count())


#ufo_data = pd.read_csv(sys.path[0] + '/data/ufo.csv', sep = ',')

max_year = ufo_data['Time'].dt.year.value_counts(normalize=True)
ufo_data['NV_occasions'] = ufo_data[ufo_data['State'] == 'NV']['Time']
#ufo_data['NV_occasions'].diff()
#print("3.5:", ufo_data[ufo_data['State'] == 'NV']['Date'].diff().dt.days.mean())

ufo_data['Date'] = ufo_data['Time'].dt.date
#print("3.5:", ufo_data[ufo_data['State'] == 'NV']['Date'].diff().dt.days.mean())

#-------------------------------------------------------------
df = pd.read_csv(sys.path[0] + '/data/ufo.csv', sep = ',')
df['Time'] = pd.to_datetime(df.Time)

df['Date'] = df['Time'].dt.date
#print(df[df['State']=='NV']['Date'].diff().dt.days.mean())

#-------------------------------------------------------------

def get_street_type(address):
# Создаём список географических пометок exclude_list.
    exclude_list = ['N', 'S', 'W', 'E']
# Метод split() разбивает строку на слова по пробелу.
# В результате получаем список слов в строке и заносим его в переменную address_list.
    address_list = address.split(' ')
    
# Обрезаем список, оставляя в нём только последний элемент,
# потенциальный подтип улицы, и заносим в переменную street_type.
    #if address_list[-1] in exclude_list:
    #    address_list = address_list[:-1] 
        
    street_type = address_list[-1]
    #print(street_type)
# Делаем проверку на то, что полученный подтип является географической пометкой.
# Для этого проверяем его на наличие в списке exclude_list.
    if street_type in exclude_list:
# Если переменная street_type является географической пометкой,
# переопределяем её на второй элемент с конца списка address_list.
        street_type = address_list[-2]
    #street_type = address_list[-1]
# Возвращаем переменную street_type, в которой хранится подтип улицы.
    return street_type


street_types = melb_df['Address'].apply(get_street_type)
#print(street_types)

def get_weekend(weekday):
    if weekday == 5 | weekday == 6:
        return 1
    else:
        return 0
    

melb_df['Weekend'] = melb_df['Date'].dt.dayofweek.apply(get_weekend)
