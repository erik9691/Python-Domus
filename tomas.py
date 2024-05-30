#Recibir una lista/array de tags pertenecientes al usuario y una lista/array de listas de otros usuarios y
#sus tags. Este algoritmo deberá identificar coincidencias entre tags y devolver un valor int el cual
#ayudará a organizar los matcheos.

#pip install pandas
import pandas as pd

def matches_listas(listaUsuarios, user_id):
    # Encontrar el índice del usuario con el id dado
    user_index = -1
    for i, user in enumerate(listaUsuarios):
        if user['id'] == user_id:
            user_index = i
            break
    
    if user_index == -1:
        raise ValueError("El id de usuario no se encontró en la lista de usuarios.")
    
    user_tags = set(listaUsuarios[user_index]['tags'])  # Tags del usuario elegido
    userPriorityPoints = {}
    
    for i, user in enumerate(listaUsuarios):
        if i != user_index:  # Evitar comparar consigo mismo
            other_user_tags = set(user['tags'])
            common_tags = user_tags.intersection(other_user_tags)  # Intersección con otros usuarios
            matches = len(common_tags)
            userPriorityPoints[user['id']] = {
                'match_score': matches,
                'common_tags': list(common_tags)
            }
    
    return userPriorityPoints

# Lee el archivo CSV con las dos columnas: id y tags
df = pd.read_csv("https://raw.githubusercontent.com/erik9691/mock-dataset/main/TAG_DATA.csv", delimiter=',')

# Asegúrate de que los ids son enteros y las tags son listas de strings
df['id'] = df['id'].astype(int)
df['tags'] = df['tags'].apply(lambda x: x.split())

# Convertimos las columnas del DataFrame a listas de diccionarios
user_tag_lists = df.to_dict(orient='records')

# id del usuario elegido (entre 1 y 750)
chosen_user_id = 1  # Reemplaza con el id del usuario que deseas usar

# Calcula los matches y obtiene la información de matches
user_matches = matches_listas(user_tag_lists, chosen_user_id)

# Ordena los resultados por el puntaje de matches en orden descendente
sorted_matches = sorted(user_matches.items(), key=lambda x: x[1]['match_score'], reverse=True)

# Imprime los resultados ordenados
print("Usuarios ordenados por matches:")
for user_id, match_info in sorted_matches:
    print(f"El usuario {user_id} tiene un puntaje de {match_info['match_score']} matches.")
    print(f"Tags en común: {', '.join(match_info['common_tags'])}")