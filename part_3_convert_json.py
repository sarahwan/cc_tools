import json
import cc_dat_utils
import cc_data

#Part 3
#Load your custom JSON file
#Convert JSON data to cc_data
#Save converted data to DAT file

def make_cc_file_from_json( json_data ):
    # Initializing CCDataFile
    data_file = cc_data.CCDataFile()

    # Iterating through level dictionaries in JSON file
    for lvl in json_data:
        # Initializing CCLevel
        level = cc_data.CCLevel()
        print("######### LEVEL #########")
        print(lvl)
        print("#########################")

        # Iterating through optional fields in level
        for fld in lvl["optional_fields"]:
            print("%%%%%%%% FIELD %%%%%%%%")
            print(fld)
            print("%%%%%%%%%%%%%%%%%%%%%%%")

#Part 2
input_json_file = "data/cc_level_data.json"

with open(input_json_file, "r") as reader:
    game_json = json.load(reader)

print("JSON data:")
print(game_json)

print("Function output:")
print(make_cc_file_from_json(game_json))