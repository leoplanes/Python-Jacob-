import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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

breed_name_counts = joint_license_bite['BreedName'].value_counts()
print(breed_name_counts.head(10))
# affiche dans l'ordre décroissant les 10 races de chiens ayant le nombre de morsures le plus élevé  

#---------------------------------------------------------------------------------------------#


#------------------- Nombre de morsures par mois (quanti/quali) -----------------------------# 

joint_license_bite_split = joint_license_bite.DateOfBite.str.split(" ", expand = True)
joint_license_bite[['MonthsOfBite', 'DaysOfBite', 'YearsOfBite']] = joint_license_bite_split
# dans le dataframe des morsures on divise la colonne 'DateOfBite' en 3 colonnes : mois, jours et années 

joint_license_bite_split.set_index(0, inplace=True)
# On définit la colonne 0 comme colonne d'index

monthly_counts = joint_license_bite_split.index.value_counts()
# On compte le nombre d'occurrences de chaque mois

"""print("Nombre d'occurrences de chaque mois :\n", monthly_counts)"""

#---------------------------------------------------------------------------------------------#





