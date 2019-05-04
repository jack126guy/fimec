#!/usr/bin/env python3

import json

def load_json(filename):
    with open(filename, "r") as f:
        return json.load(f)

dupes_found = False
codes = {}

episodes = load_json("data/episodes.json")
others = load_json("data/others.json")

all_media = episodes + others

for media in all_media:
    if media["code"] in codes:
        print("Duplicate found for {}: original {}, new {}" \
            .format(media["code"], codes[media["code"]], media["title"]))
        dupes_found = True
    else:
        codes[media["code"]] = media["title"]

if not dupes_found:
    print("No duplicates found")