import json

def count_male_cats(data):
    male_count = 0
    for cat in data:
        kittens = cat['kittens']
        for kitten in kittens:
            if kitten['gender'] == 'm':
                male_count += 1
    return male_count

# Given data
data = [
    {
        "name": "Lindy",
        "breed": "Cymric",
        "color": "white",
        "kittens": [
            {"name": "Percy", "gender": "m"},
            {"name": "Thea", "gender": "f"},
            {"name": "Annis", "gender": "f"}
        ]
    },
    {
        "name": "Mina",
        "breed": "Aphrodite Giant",
        "color": "ginger",
        "kittens": [
            {"name": "Doris", "gender": "f"},
            {"name": "Pickle", "gender": "f"},
            {"name": "Max", "gender": "m"}
        ]
    },
    {
        "name": "Antonia",
        "breed": "Ocicat",
        "color": "leopard spotted",
        "kittens": [
            {"name": "Bridget", "gender": "f"},
            {"name": "Randolph", "gender": "m"}
        ]
    }
]

print(count_male_cats(data))
