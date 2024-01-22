import random
import string

# Function to generate a random letter
def random_letter():
    return random.choice(string.ascii_lowercase)

# Generate a list of random dictionaries
list_of_dicts = []
for _ in range(random.randint(2, 10)):  # Random number of dictionaries (2 to 10)
    new_dict = {}
    num_keys = random.randint(1, 5)  # Random number of keys per dictionary (1 to 5)
    for _ in range(num_keys):
        new_key = random_letter()
        new_value = random.randint(0, 100)  # Random value (0 to 100)
        new_dict[new_key] = new_value
    list_of_dicts.append(new_dict)

dictionary_keys = []
for dictionary in list_of_dicts:
    for key in dictionary.keys():
     dictionary_keys.append(key)

index = 0
merged_dict = {}

for dictionary in list_of_dicts:
    for key in dictionary_keys:
        if key in merged_dict.keys() and key in dictionary.keys():
            value_of_repeated_key = dictionary.pop(key)
            new_key = str(key) + '_' + str(index)
            dictionary.setdefault(new_key, value_of_repeated_key)
    merged_dict.update(dictionary)
    index += 1

print(merged_dict)