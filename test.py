import json

input_json_file = "data/test_data.json"

with open(input_json_file, "r") as reader:
    game_json = json.load(reader)

print("JSON data:")
print(game_json)

print("%%%%%%%%%%%%%%%%%%")
print(game_json.keys())
print(game_json["game 1"])
print("%%%%%%%%%%%%%%%%%%")
