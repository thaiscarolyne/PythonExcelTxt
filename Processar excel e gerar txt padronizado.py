import pandas as pd

df = pd.read_excel('clientes.xlsx')

size = df["cpf"].size

lista = ""

for cpf in df["cpf"]:
    lista = lista + ("\""+str(cpf)+"\"")
    if(cpf != df["cpf"][size-1]):
        lista = lista + (",")
        
file2 = open("MyFile2.txt","w+")

file2.write(lista)

file2.close()
