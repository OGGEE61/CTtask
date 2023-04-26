import json
import os

alcohols = (
    "Johnnie-Walker",
    "Jack-Daniels",
    "Jameson",
    "Hennessy",
    "Smirnoff",
    "Grey-Goose",
    "Absolut",
    "Belvedere",
    "Bacardi",
    "Captain-Morgan",
    "Malibu",
    "Jose-Cuervo",
    "Patron",
    "Don-Julio",
    "Martini-Rossi",
    "Campari",
    "Aperol",
    "Baileys",
    "Kahlua",
    "Cointreau",
    "Bombay",
    "Tanqueray",
    "Hendricks",
    "Moet",
    "Dom-Perignon",
    "Chivas-Regal",
    "Glenfiddich",
    "Macallan",
    "Makers-Mark",
    "Crown-Royal",
    "Jim-Beam",
    "Bulleit",
    "Dewars",
    "Glenlivet",
    "Titos",
    "Stolichnaya",
    "Ketel-One",
    "Sailor-Jerry",
    "Kraken",
    "Mount-Gay",
    "Havana-Club",
    "Sauza",
    "Herradura",
    "Casamigos",
    "Noilly-Prat",
    "Lillet",
    "Pimms",
    "St-Germain",
    "Chambord"
)


def create_alcohol_json(alcohol):
    entry = {
        "required": [
            {"keyword": alcohol.lower(), "mode": "m"},
        ],
    }
    return  entry


dir_name = "folder4files"
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

for alcohol in alcohols:
    alcohol_json = create_alcohol_json(alcohol)
    
    with open(f'{dir_name}/{alcohol.lower().replace("-", "_")}.json', 'w') as outfile:
        json.dump(alcohol_json, outfile, indent=2)


dir_name = "folder4files"
for file_name in os.listdir(dir_name):
    if file_name.endswith(".json"):
        # modify curl command with file name and alcohol name
        curl_command = f'curl --data "@{dir_name}/{file_name}" "https://urlkeywords.cloudtechnologies.dev/keywordURLs" -o output_{file_name}'
        # execute curl command
        os.system(curl_command)