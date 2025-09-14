# manages user profiles
from utils import get_profile, update_profile

class UserProfile():
    def __init__(self, username):
        self.user = get_profile(username)
        self.highest_score = self.user.get("high")
        self.score = self.user.get("score")

    def increase_score(self):
        self.score += 1
        if self.score > self.highest_score:
            self.highest_score = self.score
        if self.score > 50:
            self.adapt_difficulty()
        self.save()

    def adapt_difficulty(self):
        if self.score > 50:
            return True
        else:
            return False
        

    def save(self):
        update_profile({"username":self.username,"high":self.highest_score,"score":self.score})
