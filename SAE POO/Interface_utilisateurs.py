import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import sqlite3

# Fonction pour récupérer les données de la base de données SQLite
def get_reservation_data():
    conn = sqlite3.connect('BDB.db')
    cursor = conn.cursor()
    query = """
        SELECT 'Domaines :', COUNT(*) AS Nombre_Reservation
        FROM Fait_Reservation
        GROUP BY 'Domaines :'
    """
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Créer une fenêtre Tkinter
root = tk.Tk()
root.title("Graphique des réservations par domaine")

# Créer un cadre pour le graphique
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

# Récupérer les données
data = get_reservation_data()
domaines = [row[0] for row in data]
nombre_reservations = [row[1] for row in data]

# Créer un graphique en barre
fig, ax = plt.subplots()
ax.bar(domaines, nombre_reservations, color='skyblue')
ax.set_xlabel('Domaine')
ax.set_ylabel('Nombre de Réservations')
ax.set_title('Nombre de Réservations par Domaine')
plt.xticks(rotation=45, ha='right')

# Insérer le graphique dans Tkinter
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Bouton pour fermer la fenêtre
quit_button = ttk.Button(root, text="Fermer", command=root.quit)
quit_button.pack(side=tk.BOTTOM, padx=10, pady=10)

# Exécuter la boucle principale de Tkinter
root.mainloop()
