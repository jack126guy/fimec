#!/usr/bin/env python3

import json

JSON_PATH = "data/episodes/base.json"

dupes_found = False
codes = {}

with open(JSON_PATH, "r") as base_file:
    episodes = json.load(base_file)

for episode in episodes:
    if episode["code"] in codes:
        print("Duplicate found for {}: original {}, new {}" \
            .format(episode["code"], codes[episode["code"]], episode["title"]))
        dupes_found = True
    else:
        codes[episode["code"]] = episode["title"]

if not dupes_found:
    print("No duplicates found")