import pandas as pd
import os
import sys

#path = os.path.dirname(os.path.realpath('10_5.py')) + "/SkillFactory/PY_10_Введение в Pandas"
#print(sys.path[0])
#os.mkdir(path + '/data')

countries_df = pd.DataFrame({
    'country': ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Казахстан'],
    'population': [56.29, 38.05, 322.28, 146.24, 45.5, 9.5, 17.04],
    'square': [133396, 9984670, 9826630, 17125191, 603628, 207600, 2724902]
})

countries_df.to_csv(sys.path[0] + '/data/countries.csv', index=False, sep=';')

melb_data = pd.read_csv(sys.path[0] + '/data/melb_data.csv', sep = ',')

#print(round(melb_data.loc[3521, 'Landsize'] / melb_data.loc[1690, 'Landsize'], 0))
melb_data['Car'] = melb_data['Car'].astype('int64')
melb_data['Bedroom'] = melb_data['Bedroom'].astype('int64')
melb_data['Bathroom'] = melb_data['Bathroom'].astype('int64')
melb_data['Propertycount'] = melb_data['Propertycount'].astype('int64')
melb_data['YearBuilt'] = melb_data['YearBuilt'].astype('int64')
print(melb_data['Type'].value_counts(normalize=True))
building_area_median = melb_data['BuildingArea'].quantile(0.5)
building_area_mean = melb_data['BuildingArea'].mean()
print(abs(building_area_median - building_area_mean)/building_area_mean)
print(melb_data['BuildingArea'].std())