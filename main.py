import json
import random

f = open("people.json")
data = json.load(f)

# simplified mbti compatibility matches
mbti_compatibility = {
    "infp": {"infp", "enfp", "infj", "enfj", "intj", "entj", "intp", "entp"},
    "enfp": {"infp", "enfp", "infj", "enfj", "intj", "entj", "intp", "entp"},
    "infj": {"infp", "enfp", "infj", "enfj", "intj", "entj", "intp", "entp"},
    "intj": {"infp", "enfp", "infj", "enfj", "intj", "entj", "intp", "entp"},
    "entj": {"infp", "enfp", "infj", "enfj", "intj", "entj", "intp", "entp"},
    "intp": {"infp", "enfp", "infj", "enfj", "intj", "entj", "intp", "entp"},
    "entp": {"infp", "enfp", "infj", "enfj", "intj", "entj", "intp", "entp"},
    "enfj": {"infp", "enfp", "infj", "enfj", "intj", "entj", "intp", "entp", "isfp"},
    "isfp": {"esfj", "estj", "enfj"},
    "istp": {"esfj", "estj"},
    "esfp": {"isfj", "istj"},
    "estp": {"isfj", "istj"},
    "isfj": {"isfj", "esfj", "istj", "estj", "esfp", "estp"},
    "istj": {"isfj", "esfj", "istj", "estj", "esfp", "estp"},
    "esfj": {"isfj", "esfj", "istj", "estj", "isfp", "istp"},
    "estj": {"isfj", "esfj", "istj", "estj", "intp", "isfp", "istp"},
    "na": {"na"} # some of u bullies didn't fill out my form
}

def parseAlreadyPaired(paired): 
    pairedList = paired.split(",")
    return pairedList

def returnCompatible(person, available):
    # returns people that you're compatible with within a list of avaiable people
    return [x for x in available if x["mbti"] in mbti_compatibility[person["mbti"]]]

finished_pairing = set()
for person in data:
    if person["name"] in finished_pairing:
        continue
    already_paired = parseAlreadyPaired(person["paired"])
    # available people are those who haven't been previously paired with and haven't been finished pairing
    available = [x for x in data if x["name"] != person["name"] and x["name"] not in already_paired and x["name"] not in finished_pairing] 
    if len(available) == 0:
        continue

    # 1. filter by diff teams, if possible
    team_filtered = [x for x in available if x["team"] != person["team"]]
    # if we run out of diff team matches to pair up with, pair with anyone
    if len(team_filtered) == 0:
        team_filtered = available
    
    # 2. filter by intj, if possible
    intj_filtered = returnCompatible(person, team_filtered)
    # if we run out of intj matches to pair up with, pair with anyone
    if len(intj_filtered) == 0:
        intj_filtered = team_filtered

    # 3. filter by status, if possible
    status_filtered = [x for x in intj_filtered if x["status"] != person["status"]]
    # if we run out of status matches to pair up with, pair with anyone
    if len(status_filtered) == 0:
        status_filtered = intj_filtered

    rand_int = random.randint(0, len(status_filtered) - 1) # random person from the list
    print(person['name'], status_filtered[rand_int]["name"])
    finished_pairing.add(person["name"])
    finished_pairing.add(status_filtered[rand_int]["name"])

    # updates json file to prevent repeat pairings 
f.close()





