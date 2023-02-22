from tabulate import tabulate

data = [["ken",22,"apple"],
        ["sharon",20,"passion"],
        ["melloz",18,"kiwi"],
        ["ezekiel",16,"mango"],
        ["gabriel",17,"orange"]]

col_names=["name","age","fav_fruit"]
print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))

