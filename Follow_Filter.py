import pandas as pd
import json
from datetime import datetime

with open("followers_1.json") as file:
    ferdata = json.load(file)
with open("following.json") as file:
    fingdata = json.load(file)

# Creates a list, iterates through the json file,
# adds formated rows into the list as nested dictionary's
# turns list into dataframe
fing_rows = []
for relations in fingdata['relationships_following']:
    username = relations['title']
    link = relations['string_list_data'][0]['href']
    timestamp = datetime.fromtimestamp(
        relations["string_list_data"][0]["timestamp"]
    ).strftime("%B %d, %Y %I:%M %p")

    row = {'username': username, 'timestamp': timestamp, 'link': link}
    fing_rows.append(row)
following_df = pd.DataFrame(fing_rows)

fer_rows = []
for person in ferdata:
    username = person['string_list_data'][0]['value']
    link = person['string_list_data'][0]['href']
    timestamp = datetime.fromtimestamp(person['string_list_data'][0]['timestamp']
                                   ).strftime("%B %d, %Y %I:%M %p")

    row2 = {'username': username, 'timestamp': timestamp, 'link': link}
    fer_rows.append(row2)
follower_df = pd.DataFrame(fer_rows)

# compares dataframes
found_fers = following_df[
    following_df['username'].isin(follower_df['username'])]
found_non = following_df[
    ~ following_df['username'].isin(follower_df['username'])]

#prints code in selected format
def fers():
    print(
        "\n".join(
            f"{r.username} | {r.link}\n - follows you back\n"
            for r in found_fers.itertuples()
        )
    )
def non_fers():
    print(
        "\n".join(
            f"{r.username} | {r.link}\n - does not follow you back\n"
            for r in found_non.itertuples()
        )
    )
def menu():
    select = {
        "1": ("Followers List", fers),
        "2": ("Non Followers List", non_fers)
    }

    print(f"|Follow Analyzer|")
    print("\n".join(
        f"| {key}. {label}"
        for key, (label, func) in select.items()
        )
    )
    choice = input("Choose: ")
    if choice in select:
        action = select[choice][1]
    else:
        action = lambda: print("Invalid option")
    action()


menu()