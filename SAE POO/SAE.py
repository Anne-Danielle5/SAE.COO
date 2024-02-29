#import csv
#with open('extraction-2021-2022-anonyme.csv', newline='', encoding='latin-1') as csvfile:
    #csv_reader = csv.reader(csvfile, delimiter=';')
    #a=[]
    #df={}
    #for row in csv_reader:
        #print(row)

import csv

# Ouvrir le fichier CSV
with open('extraction-2021-2022-anonyme.csv', newline='', encoding='latin-1') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')
    
    # Lire la première ligne pour obtenir les noms des colonnes
    columns = next(csv_reader)
    
    # Initialiser le dictionnaire pour stocker les données
    data_dict = {col: [] for col in columns}
    
    # Parcourir les lignes restantes du fichier CSV
    for row in csv_reader:
        # Ajouter chaque élément de la ligne à la liste correspondante dans le dictionnaire
        for col, value in zip(columns, row):
            data_dict[col].append(value)

# Afficher le dictionnaire
print(data_dict)

        

        
#for value in row:
#a.append(value)
#print(a)



    
