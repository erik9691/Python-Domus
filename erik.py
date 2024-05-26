import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Read the data
df = pd.read_csv("https://raw.githubusercontent.com/erik9691/mock-dataset/main/TAG_DATA.csv")

# Convert strings separated by spaces into list for each row
df['tags'] = df['tags'].apply(lambda x: x.split(' '))

# Convert dataframe into list of lists
list_of_lists = df.apply(lambda row: [row['id']] + row['tags'], axis=1).tolist()

# Extract tags from each user
user_tags = [' '.join(row[1:]) for row in list_of_lists]

# Calculate TF-IDF scores
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(user_tags)

# Compute cosine similarity between main user and all other users
main_user_index = 4  # Assuming the main user is the first user in the list
main_user_tfidf = tfidf_matrix[main_user_index]
cosine_sim_with_main_user = cosine_similarity(main_user_tfidf, tfidf_matrix).flatten()

# Sort users by cosine similarity with the main user
sorted_users = sorted(zip(cosine_sim_with_main_user, list_of_lists), reverse=True)

# Narrow the result to just the ids
sorted_user_ids = [((user)[1])[0] for user in sorted_users]

print(sorted_users)
