import json

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
    return [x["name"] for x in available if x["mbti"] in mbti_compatibility[person["mbti"]]]

finished_pairing = set()
for person in data:
    if person["mbti"] == "na" or person["name"] in finished_pairing:
        continue
    already_paired = parseAlreadyPaired(person["paired"])
    # available people are those who haven't been previously paired with and haven't been finished pairing
    available = [x for x in data if x["name"] != person["name"] and x["name"] not in already_paired and x["name"] not in finished_pairing] 
    if len(available) == 0:
        continue
    
    # 2. filter by intj, if possible
    intj_filtered = returnCompatible(person, available)
    
    print(person["name"], ":", intj_filtered)

    # updates json file to prevent repeat pairings 
f.close()





