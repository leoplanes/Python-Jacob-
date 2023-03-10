import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

# import des bibliothèques


#------------------- Ouverture des fichiers CSV nécessaires -----------------------------# 

dog_license_df = pd.read_csv(r"D:\Utilisateurs\Léo\Bureau\M2 MSI\Cours python - Jacob\VSC python\Datasets\NYC_Dog_Licensing_Dataset.csv", sep=";")
# ouverture de notre fichier csv Dog Licensing dataset

dog_bite_df = pd.read_csv(r"D:\Utilisateurs\Léo\Bureau\M2 MSI\Cours python - Jacob\VSC python\Datasets\DOHMH_Dog_Bite_Data.csv", sep=";")
# ouverture de notre fichier csv Dog Bite data 

#----------------------------------------------------------------------------------------#





#------------------- Races de chiens qui mordent le plus (quanti/quali) -----------------------------# 

bite_per_id = dog_bite_df.groupby(['Unique Dog ID'])['UniqueID'].count().reset_index(name='Count').sort_values(['Count'], ascending=False)
# On comptabilise le nombre de morsures par Unique Dog ID  

dog_license_df.drop(dog_license_df[dog_license_df['BreedName']=='Unknown'].index, inplace=True)
# on supprime les lignes qui contiennent "Unknwown" dans la colonne BreedName (colonne des races)

joint_license_bite = pd.merge(dog_license_df, dog_bite_df, on = 'Unique Dog ID')
# permet de faire la jointure entre les 2 dataframes grâce à la colonne Unique Dog ID qui est présente dans les deux 

breed_name_counts = joint_license_bite['BreedName'].value_counts().reset_index(name='count').nlargest(10, 'count')
"""print(breed_name_counts)
print(joint_license_bite.columns)"""
# affiche dans l'ordre décroissant les 10 races de chiens ayant le nombre de morsures le plus élevé  

#---------------------------------------------------------------------------------------------#





#------------------- Nombre de morsures par mois (quanti/quali) -----------------------------# 

joint_license_bite_split = joint_license_bite.DateOfBite.str.split(" ", expand = True)
joint_license_bite[['MonthsOfBite', 'DaysOfBite', 'YearsOfBite']] = joint_license_bite_split
# dans le dataframe des morsures on divise la colonne 'DateOfBite' en 3 colonnes : mois, jours et années 

joint_license_bite_split.set_index(0, inplace=True)
# On définit la colonne 0 comme colonne d'index

monthly_counts = joint_license_bite_split.index.value_counts().reset_index(name='count')
# On compte le nombre d'occurrences de chaque mois

monthly_counts['index'] = pd.to_datetime(monthly_counts['index'], format='%B')
monthly_counts = monthly_counts.sort_values(by='index')

"""print("Nombre d'occurrences de chaque mois :\n", monthly_counts)"""

#---------------------------------------------------------------------------------------------#





#-----------------------------  Taux de stérilisation des races mordant le plus (/)  -------------------------------#
races_selectionnees = ['Yorkshire Terrier','Shih Tzu', 'Chihuahua', 'Maltese', 'Labrador Retriever', 'American Pit Bull Mix / Pit Bull Mix', 'Labrador Retriever Crossbreed', 'American Pit Bull Terrier/Pit Bull', 'Havanese', 'Jack Russell Terrier']
joint_license_bite_selection_10_races = joint_license_bite[joint_license_bite['BreedName'].isin(races_selectionnees)]
# on sélectionne seulement les 10 races qui nous intéressent dans notre dataframe 

taux_sterilisation_top10 = joint_license_bite_selection_10_races.groupby('BreedName')['SpayNeuter'].mean().reset_index(name='count')
"""print(taux_sterilisation_top10)"""
# on fait une moyenne du taux de stérilisation pour nos 10 races sélectionnées 

"""taux_sterilisation_moyenne = joint_license_bite['SpayNeuter'].mean()
print(taux_sterilisation_moyenne)"""

#---------------------------------------------------------------------------------------------#





#----------------------- Répartition des morsures par âge (Quanti/Quanti)  --------------------------------------#

data_filtre = dog_bite_df.query('AnimalBirthMonth not in [17, 217, 1947]')
# Filtrage des valeurs aberrantes du dataframe (chiens nés en 17, 217 et 1947)

annee_actuelle = datetime.datetime.now().year
dog_bite_df['age'] = annee_actuelle - data_filtre['AnimalBirthMonth']
# Calcul de l'âge de chaque chien en utilisant datetime 

morsures_par_age = dog_bite_df.groupby('age')['UniqueID'].count().reset_index(name='count')
# Répartition des morsures par âge de chien

print(morsures_par_age)

#--------------------------------------------------------------------------------------------------# 



