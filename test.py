import pandas as pd

# pd.DataFrame({ "anshika": 24, "monika": 23, "mohit": 25"})

data = {
    "name": ["Ram" , "sita" , "gita"],
    "age": [23,30,12]
}

df = pd.DataFrame(data)
print(df)

