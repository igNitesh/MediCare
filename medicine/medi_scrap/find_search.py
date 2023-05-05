import os
import json
import random

def search_medi_in_folder(search_arg):

    directory = "/Users/apple/Desktop/MediCare/medicine/medi_scrap/medi_data"
    files = os.listdir(directory)

    similar_files = []

    # Loop through each file in the directory
    for file in files:
        # Check if the search argument is a complete file name
        # if search_arg == file:
        #     # If found, print the file path and exit the script
        #     print(os.path.join(file))
        #     break
        # # If the search argument is not a complete file name
        if search_arg in file:
            # Add the file name to the list of similar file names
            similar_files.append(file)

    # If any similar files were found
    if similar_files:
        random_file = random.choice(similar_files)
        return random_file
        # return os.path.join(directory, random_file)
    else:
        return None


def return_searched_medi_dict(medicine_name):
    with open(f"/Users/apple/Desktop/MediCare/medicine/medi_scrap/medi_data/{medicine_name}", "r") as f:
        json_string = f.read()

    my_dict = json.loads(json_string)
    return my_dict
