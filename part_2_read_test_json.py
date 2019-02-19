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

    # Iterates through each game within json_data
    for key in json_data:
        # Establish the data for the current game
        game_data = json_data[key]

        # Getting game information
        new_game = test_data.Game()
        new_game.title = game_data["title"]
        new_game.year = game_data["Year"]

        # Getting platform information
        new_platform = test_data.Platform()
        platform_data = game_data["platform"]
        new_platform.launch_year = platform_data["launch year"]
        new_platform.name = platform_data["name"]
        new_game.platform = new_platform
    
        game_library.add_game(new_game)

        

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
