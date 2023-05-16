class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
    
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self
    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
        else:
            print("not enough points")
        return self

Anis_user = User("Anis", "Ghadhab", "anisghadhab@utctunisie.com", 30)

Aymen_user = User("Aymen", "Ghadhab", "akay442@hotmail.com", 33)

Atef_user = User("Atef", "Bhouri", "atefbhouri@hotmail.com", 55)

Anis_user.enroll().spend_points(50).display_info()

Aymen_user.enroll().spend_points(80).display_info()

Atef_user.spend_points(40).display_info()

