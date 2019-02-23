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

        level.level_number = lvl["level number"]
        level.time = lvl["time"]
        level.num_chips = lvl["num_chips"]
        level.upper_layer = lvl["upper layer"]
        level.lower_layer = lvl["lower layer"]

        # Iterating through optional fields in level
        for fld in lvl["optional_fields"]:
            if fld["id"] == "hint":
                new_field = cc_data.CCMapHintField(fld["hint_text"])
            elif fld["id"] == "title":
                new_field = cc_data.CCMapTitleField(fld["title_text"])
            elif fld["id"] == "password":
                new_field = cc_data.CCPasswordField(fld["password"])
            elif fld["id"] == "monster":
                coords = []
                # Creating list of CCCoordinate objects
                for c in fld["monster_location"]:
                    new_coord = cc_data.CCCoordinate(c[0], c[1])
                    coords.append(new_coord)
                new_field = cc_data.CCMonsterMovementField(coords)
            else:
                print("There was an error... Unexpected field!")

            level.add_field(new_field)
        data_file.add_level(level)
    return data_file

#Part 2
input_json_file = "data/cc_level_data.json"

with open(input_json_file, "r") as reader:
    cc_json = json.load(reader)

print("JSON data:")
print(cc_json)

print("Function output:")
print(make_cc_file_from_json(cc_json))

cc_game_data = make_cc_file_from_json(cc_json)
cc_dat_utils.write_cc_data_to_dat(cc_game_data, "data/cc_game_data.dat")

pfgd_test_data = cc_dat_utils.make_cc_data_from_dat("data/pfgd_test.dat")
cc_dat_utils.write_cc_data_to_dat(pfgd_test_data, "data/copy_of_pfgd_test.dat")