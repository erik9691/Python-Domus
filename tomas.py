#Recibir una lista/array de tags pertenecientes al usuario y una lista/array de listas de otros usuarios y
#sus tags. Este algoritmo deberá identificar coincidencias entre tags y devolver un valor int el cual
#ayudará a organizar los matcheos.

import pandas as pd

def matches_listas(listaUsuarios):
    userPriorityPoints = []
    user_tags = set(listaUsuarios[0])
    for i, other_user_tags in enumerate(listaUsuarios[1:], start=1):
        matches = len(user_tags.intersection(other_user_tags))
        userPriorityPoints.append((i, matches))  # Guarda el índice del usuario y la cantidad de matches
    return userPriorityPoints

# Lee el archivo CSV con las dos columnas: ID y tags
df = pd.read_csv("https://raw.githubusercontent.com/erik9691/mock-dataset/main/TAG_DATA.csv", delimiter=',')
# Divide las tags separadas por espacios y las convierte en listas
df['tags'] = df['tags'].apply(lambda x: x.split())

# Convertimos las columnas del DataFrame a listas y las almacenamos en una lista de listas
user_tag_lists = df['tags'].tolist()

# Calcula los matches y ordena las listas por la cantidad de matches
matches_sorted = sorted(matches_listas(user_tag_lists), key=lambda x: x[1], reverse=True)

# Imprime los resultados ordenados
for user_index, matches in matches_sorted:
    print(f"El usuario {user_index + 1} tiene {matches} matches.")