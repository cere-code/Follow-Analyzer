import pandas as pd
import json
from datetime import datetime

with open("followers_1.json") as file:
    ferdata = json.load(file)
with open("following.json") as file:
    fingdata = json.load(file)

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
# print(following_df)

fer_rows = []
for person in ferdata:
    username = person['string_list_data'][0]['value']
    link = person['string_list_data'][0]['href']
    timestamp = datetime.fromtimestamp(person['string_list_data'][0]['timestamp']
                                   ).strftime("%B %d, %Y %I:%M %p")

    row2 = {'username': username, 'timestamp': timestamp, 'link': link}
    fer_rows.append(row2)

follower_df = pd.DataFrame(fer_rows)
# print(follower_df.to_string())

compared_df = following_df[
    ~ following_df['username'].isin(follower_df['username'])
]


print(
    "\n".join(
        f"{r.username} | {r.link}\n - does not follow you back\n"
        for r in compared_df.itertuples()
    )
)