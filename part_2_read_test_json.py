import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###
    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    ### End Add Code Here ###

    game_library.title = json_data["title"]
    game_library.title = json_data["year"]

    for platform_data in json_data["platform"]:
        platform = json_data.Platform()
        platform.launch_year = platform_data["launch year"]
        platform.name = platform_data["name"]

        game_library.platform = platform

    return game_library


#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###

with open(input_json_file, "r") as reader:
    game_json = json.load(reader)

print("JSON data:")
print(game_json)

game_data = make_game_library_from_json(game_json)
print()
print("Game data:")
print(game_data)
