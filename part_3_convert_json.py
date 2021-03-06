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
                new_field = cc_data.CCEncodedPasswordField(fld["password"])
            elif fld["id"] == "monster":
                coords = []
                # Creating list of CCCoordinate objects
                for c in fld["monster_location"]:
                    new_coord = cc_data.CCCoordinate(c[0], c[1])
                    coords.append(new_coord)
                new_field = cc_data.CCMonsterMovementField(coords)
            elif fld["id"] == "trap":
                traps = []
                b_lst = fld["trap_button"]
                l_lst = fld["trap_location"]

                # bc = cc_data.CCCoordinate(b_lst[0], b_lst[1])
                # tc = cc_data.CCCoordinate(l_lst[0], l_lst[1])

                # Initializing trap information
                traps.append(cc_data.CCTrapControl(b_lst[0], b_lst[1], l_lst[0], l_lst[1]))
                new_field = cc_data.CCTrapControlsField(traps)
            else:
                print("There was an error... Unexpected field!")

            # Adding newly made field to level
            level.add_field(new_field)

        # Adding level to game data file
        data_file.add_level(level)
    return data_file

#Part 2
input_json_file = "data/sarahwan_cc1.json"

with open(input_json_file, "r") as reader:
    cc_json = json.load(reader)

print("JSON data:")
print(cc_json)

print("Function output:")
print(make_cc_file_from_json(cc_json))

cc_game_data = make_cc_file_from_json(cc_json)
cc_dat_utils.write_cc_data_to_dat(cc_game_data, "data/sarahwan_cc1.dat")