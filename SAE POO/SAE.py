
import pandas as pd
import csv
import re
# Charger les données depuis le fichier CSV
data = []

with open('extraction-2021-2022-anonyme.csv', newline='', encoding='latin-1') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')
    for i, row in enumerate(csv_reader):
        if i == 0:  # Ignore la première ligne
            columns = row  # Stocke les noms de colonnes
        else:
            data.append(row)

# Créer un DataFrame à partir des données
df = pd.DataFrame(data, columns=columns)
df = df.drop(0)  # Supprime la première ligne

# Diviser la colonne "Heure-Durée" en deux colonnes
df[['Date', 'Durée']] = df['Heure - Durée :'].str.split('-', expand=True)

# Supprimer la colonne "Heure-Durée"
df = df.drop(columns=['Heure - Durée :'])

# Afficher le DataFrame après les modifications
#print(df)

# Fonction pour convertir le format de la colonne "Date"
# Fonction pour convertir le format de la colonne "Date"
def convert_date_format(date_str):
    pattern = r"(?P<jour>\w+) (?P<jour_num>\d+) (?P<mois>\w+) (?P<annee>\d+) (?P<heure>\d+):(?P<minute>\d+):(?P<seconde>\d+)"
    match = re.search(pattern, date_str)
    if match:
        mois_fr_to_en = {
            'janvier': 'January',
            'février': 'February',
            'mars': 'March',
            'avril': 'April',
            'mai': 'May',
            'juin': 'June',
            'juillet': 'July',
            'août': 'August',
            'septembre': 'September',
            'octobre': 'October',
            'novembre': 'November',
            'décembre': 'December'
        }
        return pd.Timestamp(
            int(match.group("annee")), 
            pd.to_datetime(mois_fr_to_en[match.group("mois")], format='%B').month, 
            int(match.group("jour_num")), 
            int(match.group("heure")), 
            int(match.group("minute")), 
            int(match.group("seconde"))
        )

# Appliquer la fonction convert_date_format à la colonne "Date"
df['Date'] = df['Date'].apply(convert_date_format)


# Fractionner la colonne "Date" en deux colonnes "Date" et "Heure"
df[['Dates', 'Heure']] = df['Date'].astype(str).str.split(' ',n= 1,expand=True)

# Supprimer la colonne "Date" précédente
df = df.drop(columns=['Date'])

# Afficher le DataFrame après les modifications
print(df['Domaines :'])










        




    
