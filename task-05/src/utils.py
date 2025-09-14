# utility functions for quiz
import json
import os
import requests

PROFILE_FILE = os.path.join(os.path.dirname(__file__), "../profiles.json")
CATEGORY_URL = "https://opentdb.com/api_category.php"

def load_profiles():
    
    with open(PROFILE_FILE,"r") as f:
        names = json.load(f)
    
    return names

def save_profiles(profiles):

    with open(PROFILE_FILE,"w") as f:                                #for each time this fn is called the whole json is re written.
        
        json.dump({"users":profiles } ,f ,indent = 4)

def get_profile(username):
    data = load_profiles()
    users = data.get("users", [])   # users is a list of dicts
    for user in users:
        if user["username"] == username:
            return user
    return None
        
def update_profile(new_profile):
    with open(PROFILE_FILE,"r") as f:

        profile = json.load(f)
    users = profile.get("users",[])
    find = False
    for user in users:                                                                      
        if user["username"] == new_profile["username"]:                             #this uses the save_profiles fn
            user["score"] = new_profile["score"]
            user["high"] = new_profile["high"]
            find =True
            break
    if not find:    
        profile.append(new_profile)
    save_profiles(profile)

def get_categories():
        response = requests.get("https://opentdb.com/api_category.php" ,timeout = 5)
        response.raise_for_status()
        data = response.json()
        cats = data.get("trivia_categories", [])
        for i in cats:
            print(i.get("id"),"-",i.get("name"))
        id = int(input("please enter the respective id number :"))
        for i in cats:
            if id == i["id"]:
                return id
            else:
                continue
        print("pleasr try again")    
        return get_categories()
            
def new_prof():
    username = input("please enter a unique username: ")
    profiles = load_profiles()
    users = profiles.get("user",[])
    for i in users:
        
        if i.get("username") == username:
            print("username exists")
            return new_prof()
    users.append({"username":username,"high":0,"score":0})
    save_profiles(users) 
    return username


