# handles quiz logic and api calls
import requests
import random
import html
import threading
import time
from rich.console import Console
from user_profile import UserProfile
console = Console()
CATEGORY_URL = "https://opentdb.com/api_category.php"
QUESTION_URL = "https://opentdb.com/api.php"

class QuizEngine(object):
    def __init__(self, profile, num_questions, difficulty, time_limit, category_id,type):
        
        self.profile = profile
        self.num_questions = num_questions
        self.difficulty = difficulty

        if self.profile.adapt_difficulty():
            self.difficulty = "hard"
        self.time_limit = time_limit
        self.category_id = category_id
        self.questions = []
        self.score = profile.score
        self.type = type
        
    def fetch_questions(self):
        params = {
                    "amount": self.num_questions ,       
                    "difficulty": self.difficulty , 
                    "type": self.type,
                    "category": self.category_id 
                }
        response = requests.get(QUESTION_URL,params = params)
        data = response.json()

        for k in data["results"]:
            pos = random.randint(0, 3)  
            lst = k["incorrect_answers"]
            lst.insert(pos, k["correct_answer"])
            (self.questions).append({"question":k["question"],"options":lst,"answer":k["correct_answer"]})

    def ask_question(self, question_data):

        bruh = self.questions[question_data]
        
        print("Q:",bruh.get("question"))
        print("Options: ",[bruh.get("options")])
        check = input("please mind the spelling of answer").strip().lower()
        if check == bruh.get("answer").strip().lower(): 
            return True,None
        else:
            return False,bruh.get("answer")

    def run(self):
        self.fetch_questions()
        k = 0
        start_time = time.time()
        time1 = 0
        print(self.questions)
        for i in range(len(self.questions)):
            check,right = self.ask_question(i)
            if check:
                
                console.print("[bold green]Right Answer!!![/bold green]")
                if time1 :
                    print("time has exeeded hence no score was rewarded")
                
                else:
                    self.profile.increase_score()
                    k+=1

            else:
                
                console.print("[bold red]Wrong answer!!![/bold red]")
                print(right,"was the correct answer")
            end_time = time.time()
            if int(self.time_limit) >= (end_time - start_time):
                time1 = 1 
            else:
                time1 = 0
        print("Your score was",k)       
        return k
            
        