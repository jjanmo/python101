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

country = input()
lowercase_countries = list(map(str.lower, d.keys()))
lowercase_input = country.lower()

lower_dict = {k.lower(): v for k, v in d.items()}  # kick!!

if lowercase_input in lowercase_countries:
    print(lower_dict[lowercase_input])
else:
    print("No results were found for your search")
