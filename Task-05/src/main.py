# main file to run timetickquiz-2 pro
import requests
from user_profile import UserProfile
from quiz_engine import QuizEngine
from rich.console import Console
from utils import get_categories,get_profile,load_profiles,new_prof



console = Console()

def main():
    users = load_profiles().get("users", []) 
    console.print("[bold blue]welcome to timetickquiz pro![/bold blue]")
    username = None
    opt = input("Use existing Username (y or n) : ").strip().lower()
    user = None
    if  opt == "y":

        username = input("please enter your user name: ")
        for i in users:
            
            if i.get("username") == username:
                user = get_profile(username)
            
            else:
                continue
        if user == None:
            print("There is no such username")
    else:
        username = new_prof()
    
    profile = UserProfile(username)

    category_id = get_categories()
    q_num = int(input("How many questions would you like?"))
    q_hard = input("Hard\nMedium\tEasy").strip().lower()
    q_type = input("Multiple type\tTrue or False (m or t)").strip().lower()
    time1 = input("please enter time limit in seconds")
    qtype = 0
    if q_type == "m":
        qtype = "multiple"
    else:
        qtype = "boolean"
    
    mhmm = QuizEngine(profile=profile ,num_questions=q_num ,difficulty=q_hard ,time_limit = time1, category_id = category_id,type = qtype)
    score = mhmm.run()


           
if __name__ == "__main__":
    main()