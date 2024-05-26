import pandas as pd

# Will replace with real and filtered csv from back-end
df = pd.read_csv("https://raw.githubusercontent.com/erik9691/mock-dataset/main/MOCK_DATA.csv")

# Will replace with real tags from back-end
main_set = {"aliquam", "amet", "consequat", "eget", "elit", "mauris", "morbi", "nisi", "nunc", "sit"}

# Convert strings separated by spaces into list for each row
df['tags'] = df['tags'].apply(lambda x: x.split(' '))

# Convert dataframe into list of lists
list_of_lists = df.apply(lambda row: [row['id']] + row['tags'], axis=1).tolist()


# Main "algorithm"
def tally_coincidences(main_set, list_of_lists):
    
    # Dictionary to store the tally results
    tally_results = {}
    
    # Iterate through each list in the list of lists
    for idx, other_list in enumerate(list_of_lists):
        # Convert the other list to a set
        other_set = set(other_list)
        
        # Find the intersection of the main set and the other set
        coincidence_count = len(main_set & other_set)
        
        # Store the result in the dictionary with the id as the key
        tally_results[other_list[0]] = coincidence_count
    
    return tally_results


id_dict = tally_coincidences(main_set, list_of_lists)

# Sorting the dictionary by values in descending order
sorted_dict = dict(sorted(id_dict.items(), key=lambda item: item[1], reverse=True))

# List of just the ids to give to back-end
sorted_ids = list(sorted_dict.keys())