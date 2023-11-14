import pandas as pd

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
# myvar = pd.DataFrame(mydataset)

# print(myvar)


# a=[1,4,6,7,3,2,0]
# b=pd.Series(a)
# print(b)

# c=pd.Series(a,index=['a','b','c','d','e','f','g'])
# print(c)


# calories = {"day1":400,"day2":230,"day3":450}
# d=pd.Series(calories)
# print(d)
# e=pd.Series(calories,index=["day1","day2"])
# print(e)


# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# myvar = pd.DataFrame(data)
# print(myvar)
# print(myvar.loc[2])




# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# myvar = pd.DataFrame(data,index=["data1","data2","data3"])
# print(myvar)



# file_path = r"C:\Users\abhisheksu\Downloads\SBN_UK_Status.xlsx"
# sample = pd.read_excel(file_path)
# print(sample)




# file=r"C:\Users\abhisheksu\Downloads\data.csv"
# sa= pd.read_csv(file)
# pd.options.display.max_rows = 2
# print(sa)
# print(sa.to_string())
# print(sa)





# file=r"C:\Users\abhisheksu\Downloads\data.csv"
# sa= pd.read_csv(file)
# print(sa.head(16))
# print(sa.head())
# print(sa.tail(16))
# print(sa.tail())
# print(sa.info()) 


# file=r"C:\Users\abhisheksu\Downloads\data.csv"    
# sa= pd.read_csv(file)
# va=sa.dropna()
# print(va.to_string())



# file=r"C:\Users\abhisheksu\Downloads\data.csv"
# sa= pd.read_csv(file)
# sa.dropna(inplace = True)
# print(sa.to_string())


# file=r"C:\Users\abhisheksu\Downloads\data.csv"
# sa= pd.read_csv(file)
# # sa.fillna(130,inplace = True)
# # print(sa.to_string())
# sa["Calories"].fillna(130, inplace = True)
# print(sa.to_string())





# Mean Median and Mode 

# file=r"C:\Users\abhisheksu\Downloads\data.csv"
# sa= pd.read_csv(file)
# x= sa["Calories"].mean()
# sa["Calories"].fillna(x, inplace= True)
# print(sa.to_string())


# file=r"C:\Users\abhisheksu\Downloads\data.csv"
# sa= pd.read_csv(file)
# x= sa["Calories"].median()
# sa["Calories"].fillna(x, inplace= True)
# print(sa.to_string())



# file=r"C:\Users\abhisheksu\Downloads\data.csv"
# sa= pd.read_csv(file)
# x= sa["Calories"].mode()
# sa["Calories"].fillna(x, inplace= True)
# print(sa.to_string())



file=r"C:\Users\abhisheksu\Downloads\data.csv"
sa= pd.read_csv(file)
sa['Calories'] = pd.DataFrame(sa['Calories'])
sa.dropna(subset=["Calories"], inplace = True)
print(sa.to_string())






