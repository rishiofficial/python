import pandas as pd
# import numpy as np

# mydataset = {
#     "cars": ["bmw","xuv","ferrari"],
#     "passings": [3,6,7]
# }

# myvar = pd.DataFrame(mydataset)

# print(myvar)
# print(pd.__version__)

# a= ["virat","kohli","ABD","FAF","RAJAT"]

# pushup = {"day1": 21, "day2": 18 , "day3":20}
# # The key of dictionary become the labels
# a =[1,4,3]
# myvar = pd.Series(pushup, index=["day2","day1"])
# print(myvar)

data = {
    "calories": [400,380,390],
    "duration": [50,45,46]
}
# myvar = pd.DataFrame(data,index=["day1","day2","day3"])
# myvar = pd.read_csv('todo.txt')

# print(myvar.to_string())
# print(pd.options.display.max_rows)
# print(myvar.info())


cricdata = ["Rohit", "KOHLI", "Dhoni","Pant"]

cric = pd.Series(cricdata, index=["opener","captain","keeper","batsman"])
# print(cric)

# mydataset = np.array({
#     "name": ["Rishi", "Ranveer","Akshat","Priyanshu","Saurabh"],
#     "age": [20,21,20,22,21]
# })

# mydataset = {
#     "name": ["Rishi", "Ranveer","Akshat","Priyanshu","Saurabh"],
#     "age": [20,21,20,22,21]
# }
# myvar = pd.Series(mydataset)
# myvar= pd.DataFrame(mydataset)
# print(myvar)
# print(type(myvar))
# print(myvar.loc[[0,3]])


df = pd.read_csv('data.csv')
# print(df.tail(2))
# print(df.to_string())
# print(df.loc[7:13])
# new_df = df.dropna()
# print(new_df.to_string())
df.dropna(inplace = True)
# print(df.to_string())

print(df.duplicated().head(50))
df.drop_duplicates(inplace =True)
print(df.duplicated().head(50))