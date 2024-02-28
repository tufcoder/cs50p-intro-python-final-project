import os
import sys
import csv
import json
import inflect
import requests
from pyfiglet import Figlet
from datetime import datetime
from tabulate import tabulate


def main():
    try:
        get_champions()
        figlet = Figlet()
        figlet.setFont(font="slant")
        print(figlet.renderText("LoL Draft SIM"))
        bans = []
        picks = []
        blue_bans = []
        red_bans = []
        blue_picks = []
        red_picks = []
        table_bans = []
        table_picks = []
        draft = []
        header_bans = ["Blue Bans", "Red Bans"]
        header_picks = ["Blue Picks", "Red Picks", "Blue Bans", "Red Bans"]
        print(get_round(1, "bans"))
        first_round_bans(1, 7, bans, picks)
        append_table_bans(bans, blue_bans, red_bans, table_bans)
        print("\n", tabulate(table_bans, headers=header_bans, tablefmt="pretty"))
        print(get_round(1, "picks"))
        first_round_picks(1, 7, bans, picks)
        append_table_picks(picks, blue_picks, red_picks, table_picks)
        append_draf(table_picks, table_bans, draft)
        print("\n", tabulate(draft, headers=header_picks, tablefmt="pretty"))
        print(get_round(2, "bans"))
        second_round_bans(7, 11, bans, picks)
        final_table_bans(bans, blue_bans, red_bans, table_bans)
        print("\n", tabulate(table_bans, headers=header_bans, tablefmt="pretty"))
        print(get_round(2, "picks"))
        second_round_picks(7, 11, bans, picks)
        final_table_picks(picks, blue_picks, red_picks, table_picks)
        final_draf(table_picks, table_bans, draft)
        print("\n", tabulate(draft, headers=header_picks, tablefmt="pretty"))
        write_draft_csv("temp", header_picks, draft)
    except KeyboardInterrupt:
        print()
        pass
    except EOFError:
        print()
        pass


def final_draf(table_picks, table_bans, draft):
    for i in range(len(table_picks)):
        if i > 2:
            draft.append(
                [
                    table_picks[i][0],
                    table_picks[i][1],
                    table_bans[i][0],
                    table_bans[i][1],
                ]
            )
    return draft


def final_table_picks(picks, blue_picks, red_picks, table_picks):
    for i, pick in enumerate(picks, start=1):
        if i == 8 or i == 9:
            blue_picks.append(pick)
        elif i == 7 or i == 10:
            red_picks.append(pick)
    for i, p in enumerate(blue_picks):
        if i > 2:
            table_picks.append([p, red_picks[i]])
    return table_picks


def final_table_bans(bans, blue_bans, red_bans, table_bans):
    for i, ban in enumerate(bans, start=1):
        if i == 8 or i == 10:
            blue_bans.append(ban)
        elif i == 7 or i == 9:
            red_bans.append(ban)
    for i, b in enumerate(blue_bans):
        if i > 2:
            table_bans.append([b, red_bans[i]])
    return table_bans


def append_draf(table_picks, table_bans, draft):
    for i in range(len(table_picks)):
        draft.append(
            [
                table_picks[i][0],
                table_picks[i][1],
                table_bans[i][0],
                table_bans[i][1],
            ]
        )
    return draft


def append_table_picks(picks, blue_picks, red_picks, table_picks):
    for i, pick in enumerate(picks, start=1):
        if i == 1 or i == 4 or i == 5:
            blue_picks.append(pick)
        else:
            red_picks.append(pick)
    for i, p in enumerate(blue_picks):
        table_picks.append([p, red_picks[i]])
    return table_picks


def append_table_bans(bans, blue_bans, red_bans, table_bans):
    for i, ban in enumerate(bans, start=1):
        if i == 1 or i == 3 or i == 5:
            blue_bans.append(ban)
        else:
            red_bans.append(ban)
    for i, b in enumerate(blue_bans):
        table_bans.append([b, red_bans[i]])
    return table_bans


def write_draft_csv(path, header, table):
    mkdir(path)
    time = datetime.now().strftime("%Y%m%d%H%M%S%f")
    with open(f"{path}/draft_sim_{time}.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(table)
        print(f"\nDraft saved in the file {file.name}")


def mkdir(path):
    try:
        os.makedirs(path, exist_ok=True)
    except OSError:
        raise


def side(s, mode):
    if s == "blue" and mode == "pick":
        return "🔵 Blue side 🔵"
    elif s == "blue" and mode == "ban":
        return "🟦 Blue side 🟦"
    elif s == "red" and mode == "pick":
        return "🔴 Red side 🔴"
    elif s == "red" and mode == "ban":
        return "🟥 Red side 🟥"


def get_round(n, mode):
    if mode == "bans":
        return f"\n### Bans {ordinal(n)} Round ###\n"
    else:
        return f"\n### Picks {ordinal(n)} Round ###\n"


def ordinal(n):
    p = inflect.engine()
    return p.ordinal(n)


def first_round_bans(x, y, bans, picks):
    for i in range(x, y):
        if i == 1 or i == 3 or i == 5:
            print(side("blue", "ban"))
        else:
            print(side("red", "ban"))
        bans.append(sinput(f"{ordinal(i)} ban: ", bans, picks))
    return bans


def first_round_picks(x, y, bans, picks):
    for i in range(x, y):
        if i == 1 or i == 4 or i == 5:
            print(side("blue", "pick"))
        else:
            print(side("red", "pick"))
        picks.append(sinput(f"{ordinal(i)} pick: ", bans, picks))
    return picks


def second_round_bans(x, y, bans, picks):
    for i in range(x, y):
        if i == 8 or i == 10:
            print(side("blue", "ban"))
        else:
            print(side("red", "ban"))
        bans.append(sinput(f"{ordinal(i)} ban: ", bans, picks))
    return bans


def second_round_picks(x, y, bans, picks):
    for i in range(x, y):
        if i == 8 or i == 9:
            print(side("blue", "pick"))
        else:
            print(side("red", "pick"))
        picks.append(sinput(f"{ordinal(i)} pick: ", bans, picks))
    return picks


def sinput(s, bans, picks, path="champions.json"):
    while True:
        try:
            name = input(s).strip()
            check_valid_name(name)
            check_bans(name, bans)
            check_picks(name, picks)
            return check_names(name, bans, picks, path)
        except ValueError:
            pass


def check_valid_name(name):
    if not name.isalpha():
        print("Enter a valid champion name")
        raise ValueError


def check_bans(name, bans):
    if name in bans:
        print("Champion already banned, try again")
        raise ValueError


def check_picks(name, picks):
    if name in picks:
        print("Champion already picked, try again")
        raise ValueError


def check_names(name, bans, picks, path="champions.json"):
    champions = read_file(path)
    if name not in champions["data"]:
        lower = check_lower_names(champions, name, bans, picks)
        if lower:
            return lower
        options = list_options(champions, name)
        if options:
            for option in options:
                print(option)
            raise ValueError
        else:
            print("Retry: champion not found")
            raise ValueError
    return champions["data"][name]["id"]


def list_options(champions, name):
    options = []
    for item in champions["data"]:
        if name.casefold() in item.casefold():
            options.append(f"Are you are trying to choose: {item} ?")
    return options


def check_lower_names(champions, name, bans, picks):
    lower_names = get_lower_names(champions)
    for item in lower_names:
        if item["lower"] == name.casefold():
            check_bans(item["name"], bans)
            check_picks(item["name"], picks)
            return champions["data"][item["name"]]["id"]
    return None


def get_lower_names(champions):
    lowers = []
    for item in champions["data"]:
        lowers.append({"name": item, "lower": item.casefold()})
    return lowers


def write_champions_file(filename="champions.json"):
    if not exists(filename):
        response = request_champions()
        write_file(filename, response)
    else:
        missings = []
        champions = read_file(filename)
        response = request_champions()
        champion_data = set(champions["data"])
        response_data = set(response["data"])
        missings = sorted(set(response_data).difference(set(champion_data)))
        for champion in missings:
            champions["data"][champion] = response["data"][champion]
        if len(missings) > 0 and champions:
            write_file(filename, champions)
    return filename


def exists(filename):
    try:
        return os.path.exists(filename) and os.path.getsize(filename) > 0
    except:
        sys.exit(filename, "Error: checking file exists")


def request_champions():
    url = "https://ddragon.leagueoflegends.com/cdn/14.3.1/data/en_US/champion.json"
    try:
        return requests.get(url).json()
    except:
        sys.exit("Error: Load champions url")


def write_file(filename, data):
    try:
        with open(filename, "w") as file:
            file.write(json.dumps(data, indent=2))
    except OSError:
        sys.exit(f"Error: write file {filename}")


def read_file(filename="champions.json"):
    try:
        with open(filename) as file:
            return json.load(file)
    except FileNotFoundError:
        raise
    except OSError:
        sys.exit(f"Error: read file {filename}")


def get_champions(path="champions.json"):
    return read_file(write_champions_file(path))


if __name__ == "__main__":
    main()
