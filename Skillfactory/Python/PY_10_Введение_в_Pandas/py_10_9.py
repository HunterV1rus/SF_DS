import pandas as pd
import sys

students_perf = pd.read_csv(sys.path[0] + '/data/students_performance.csv', sep = ',')

print(students_perf.count())
print("155 student writing:", students_perf['writing score'][155])
print(students_perf.info())
print(students_perf['math score'].mean())
print(students_perf['race/ethnicity'].mode())
print("math zeros: ",students_perf[(students_perf['math score'] == 0)]['math score'].count())
free_lunch = students_perf[(students_perf['lunch'] == 'free/reduced')]['math score'].mean()
standard_lunch = students_perf[(students_perf['lunch'] == 'standard')]['math score'].mean()
print("9.10:", standard_lunch - free_lunch, "free:", free_lunch, "standard:", standard_lunch)
#print("bechelor parents: ", students_perf[(students_perf['parental level of education'] == "bachelor's degree")].value_counts(normalize=True))
print("bechelor parents: ", students_perf['parental level of education'].value_counts(normalize=True)["bachelor's degree"])

group_a_median = students_perf[(students_perf['race/ethnicity'] == 'group A')]['writing score'].median()
group_c_median = students_perf[(students_perf['race/ethnicity'] == 'group C')]['writing score'].median()
print("9.12:", abs(round(group_a_median - group_c_median, 0)))
print(students_perf.describe())