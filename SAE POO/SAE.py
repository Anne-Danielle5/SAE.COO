#import csv
#import pandas as pd

#data = []

#with open('extraction-2021-2022-anonyme.csv', newline='', encoding='latin-1') as csvfile:
    #csv_reader = csv.reader(csvfile, delimiter=';')
    #for row in csv_reader:
      #  data.append(row)  # Ajouter chaque ligne du CSV à la liste data

# Créer un DataFrame à partir des données
#df = pd.DataFrame(data, columns=['Reservation au nom de', 'Domaines ', 'Ressource ', 'Description ', 'Heure-Durée ', 'Type ', 'Dernière mise à jour '])
#df['Heure-Durée '] = df['Heure-Durée '].str.split('-')

import csv
import pandas as pd

# Fonction personnalisée pour fractionner les valeurs de la colonne "Heure-Durée"
def split_heure_duree(value):
    parts = value.split(' - ')
    if len(parts) == 3:
        return parts
    elif len(parts) == 2:
        # Si seulement deux parties sont présentes, nous pouvons supposer que la durée n'est pas spécifiée
        return [parts[0], parts[1], '']
    else:
        # Si le format n'est pas conforme, nous retournons trois parties vides
        return ['', '', '']

# Charger les données depuis le fichier CSV
data = []

with open('extraction-2021-2022-anonyme.csv', newline='', encoding='latin-1') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')
    for row in csv_reader:
        data.append(row)  

# Créer un DataFrame à partir des données
df = pd.DataFrame(data, columns=['Reservation au nom de', 'Domaines', 'Ressource', 'Description', 'Heure-Durée', 'Type', 'Dernière mise à jour'])

# Appliquer la fonction personnalisée pour fractionner la colonne 'Heure-Durée'
df[['Date', 'Durée', 'Durées']] = pd.DataFrame(df['Heure-Durée'].apply(split_heure_duree).tolist(), index=df.index)

# Supprimer la colonne 'Heure-Durée' originale
df.drop(columns=['Heure-Durée'], inplace=True)




# Afficher toutes les lignes et colonnes du DataFrame
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Fractionner la colonne 'Date' en deux colonnes 'Date' et 'Heure'
df[['Date', 'Heures']] = df['Date'].str.split(r'\s(?=[^\s]*$)', expand=True)

# Afficher le résultat



# Afficher le DataFrame résultant
print(df['Date'])
print(df['Heures'])
print(df['Durée'])

        




    
