import pandas as pd

# mydataset = {
#     "cars": ["bmw","xuv","ferrari"],
#     "passings": [3,6,7]
# }

# myvar = pd.DataFrame(mydataset)

# print(myvar)
# print(pd.__version__)

# a= ["virat","kohli","ABD","FAF","RAJAT"]

# pushup = {"day1": 21, "day2": 18 , "day3":20}
#The key of dictionary become the labels
# a =[1,4,3]
# myvar = pd.Series(pushup, index=["day2","day1"])
# print(myvar)

data = {
    "calories": [400,380,390],
    "duration": [50,45,46]
}
# myvar = pd.DataFrame(data,index=["day1","day2","day3"])
myvar = pd.read_csv('todo.txt')
# print(myvar.to_string())
# print(pd.options.display.max_rows)
print(myvar.info())