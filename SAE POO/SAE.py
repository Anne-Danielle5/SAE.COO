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
from datetime import datetime
import locale 

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
# Convertir la colonne 'Date' en format date, en ignorant les erreurs
#df['Date'] = pd.to_datetime(df['Date'], format='%A %d %B %Y %H:%M:%S', errors='coerce')

# Afficher le DataFrame avec la colonne 'Date' convertie en format date

# Afficher le résultat


# Afficher le DataFrame résultant
locale.setlocale(locale.LC_TIME, "fr_FR")
df['Date'] = df.iloc[10:, df.columns.get_loc('Date')]
date_str_list = df['Date'].tolist()
date_obj_list = [datetime.strptime(date_str, '%A %d %B %Y') for date_str in date_str_list]
for date_obj in date_obj_list:
    print(date_obj)
print(df['Date'])
#print(df['Heures'])
#print(df['Durée'])






        




    
