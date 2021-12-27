import pandas as pd

# data input
data = pd.read_csv("data_frame.csv", delimiter=";").iloc[ : , 0:2 ]

# variable name
name_index = "index_date"
name_variable = "igpm"

#rename columns
data.columns=[name_index, name_variable]

# replace
data["index_date"] = data["index_date"].astype(str)
data["index_date"] = data["index_date"].str.replace(".","-")

data["index_date"] = data["index_date"].astype(str)
data["index_date"] = data["index_date"].str.replace("-1","-10")


data["index_date"] = data["index_date"].astype(str)
data["index_date"] = data["index_date"].str.replace("-101","-11")
data["index_date"] = data["index_date"].str.replace("-102","-12")
data["igpm"] = data["igpm"].str.replace(",", ".")

data.to_csv("data_frame2.csv", index=False)
