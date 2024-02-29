import csv
import pandas as pd

data = []

with open('extraction-2021-2022-anonyme.csv', newline='', encoding='latin-1') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')
    for row in csv_reader:
        data.append(row)  # Ajouter chaque ligne du CSV à la liste data

# Créer un DataFrame à partir des données
df = pd.DataFrame(data, columns=['Reservation au nom de', 'Domaines ', 'Ressource ', 'Description ', 'Heure-Durée ', 'Type ', 'Dernière mise à jour '])

print(df)



