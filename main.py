import json

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


def create_alcohol_json(alcohols):
    results = []

    for alcohol in alcohols:
        id = alcohol.lower().replace(" ", "_")
        entry = {
            "id": id,
            "required": [
                {"keyword": alcohol.lower(), "mode": "m"},
              
            ],

        }
        results.append(entry)
        #with open(id+'.json', 'w') as outfile:
        #    json.dump(entry, outfile, indent=2)

    return {"results": results}

alcohol_json = create_alcohol_json(alcohols)

with open('alcohols.json', 'w') as outfile:
    json.dump(alcohol_json, outfile, indent=2)