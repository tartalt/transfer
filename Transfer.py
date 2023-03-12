import os
import pandas
import shutil

# Lire les données du fichier Excel
df = pandas.read_excel('D:/tilapia_archeo/otolithes_inventaire_scan.xlsx')

# Filtrer les lignes pour ne conserver que les photos avec une valeur 'M'
df = df[df['A\nM'] == 'M']

# Récupérer la liste des identifiants uniques des photos
photo_ids = df['n°'].tolist()

src_folder = 'D:/tilapia_archeo/images_brutes'
dst_folder = 'D:/tilapia_archeo/images_brutes_archeo'

# Pour chaque photo dans la liste d'identifiants uniques
for photo_id in photo_ids:
    # Pour chaque fichier dans le dossier source
    for filename in os.listdir(src_folder):
        # Si l'identifiant unique se trouve dans le nom du fichier
        if str(photo_id) in filename:
            # Construire le chemin complet pour la photo source
            src_path = os.path.join(src_folder, filename)

            # Construire le chemin complet pour la photo de destination
            dst_path = os.path.join(dst_folder, filename)

            # Copier la photo depuis le dossier source vers le dossier de destination
            shutil.copy2(src_path, dst_path)
