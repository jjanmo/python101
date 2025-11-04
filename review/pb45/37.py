# Dictionary Search By Value

d = {
    "USA": 36,
    "Germany": 17,
    "France": 32,
    "Australia": 77,
    "South Africa": 99,
    "India": 108,
    "South Korea": 200,
}


def search_country(text):
    try:
        lower_dict = {k.lower(): v for k, v in d.items()}  # kick!!
        lower_text = text.lower()
        return lower_dict[lower_text]
    except:
        print("No results were found for your search")


text = input()

search_country(text)
