import csv

archivo =open("bgg_db_1806.csv","r", encoding="utf8")
csvreader = csv.reader(archivo, delimiter =',')

encabezado = next(csvreader)
print(encabezado)
print(20*"="+"Nombres"+20*"=")

for linea in csvreader:
    if (int(linea[5]) < 3) and (linea[17] == "Card Game"):
        print(f"{linea[3]}")
archivo.close()
