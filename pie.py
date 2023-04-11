import pandas as pd
import matplotlib.pyplot as plt
import glob


# Lire les données à partir d'un fichier CSV
csv_files = glob.glob('./ArchiveCSV/*.csv')
df = pd.concat([pd.read_csv(f) for f in csv_files])

# Compter le nombre de paquets envoyés à chaque adresse
value_counts = df["Destination"].value_counts()
value_counts.pop('192.168.1.24')
value_counts.pop('17.248.148.175')
value_counts.pop('17.248.145.82')
value_counts.pop('17.248.248.79')
# Créer un pie chart à partir des données
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(value_counts.values, labels=value_counts.index, autopct='%1.1f%%')
ax.set_title("Destinations des paquets")

# Afficher le pie chart
print(value_counts)
plt.show()


