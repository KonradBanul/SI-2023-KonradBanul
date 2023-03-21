import pandas as pd

data = pd.read_csv("australian.txt", header=None, sep=" ")

list = ["s", "n", "n", "s", "s", "s", "n", "s", "s", "n", "s", "s", "n", "n", "15"]
data.columns = list
print("DataFrame:")
print(data)
print("Powyzej ilosc obiektow i atrybutow:")
print("=================================================")
symbols = data["15"].value_counts()
print("Symbole klas decyzyjnych i ich ilosc:")
print(symbols)
print("=================================================")

max = data["n"].max(skipna=False)
min = data["n"].min(skipna=False)
std = data["n"].std()

print("Max wartości poszczególnych atrybutów numerycznych:")
print(max)
print("=================================================")
print("Min wartości poszczególnych atrybutów numerycznych:")
print(min)
print("=================================================")
print("Odchylenie standardowe poszczególnych atrybutów numerycznych:")
print(std)
print("=================================================")

list = ["s1", "n2", "n3", "s4", "s5", "s6", "n7", "s8", "s9", "n10", "s11", "s12", "n13", "n14", "15"]
data.columns = list

for x in list:
    uni = len(pd.unique(data[x]))
    print(x, "\n", "rozne:", uni, "\n", "lista:", pd.unique(data[x]))

for x in list[: -1]:
    random_rows = data.sample(frac=0.1).index
    data.loc[random_rows, x] = '?'
print(data)

model = pd.read_csv("Churn_Modelling.csv")
print(model)

dummy = pd.get_dummies(model['Geography'])
print(dummy)

drop = dummy.drop("Spain", axis=1)
print(drop)
