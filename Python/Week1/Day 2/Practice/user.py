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
    
    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
        else:
            print("not enough points")

Anis_user = User("Anis", "Ghadhab", "anisghadhab@utctunisie.com", 30)

Aymen_user = User("Aymen", "Ghadhab", "akay442@hotmail.com", 33)

Atef_user = User("Atef", "Bhouri", "atefbhouri@hotmail.com", 55)

Anis_user.display_info()
Anis_user.enroll()
Anis_user.spend_points(50)
Aymen_user.enroll()
Aymen_user.spend_points(80)

# Anis_user.display_info()
# Aymen_user.display_info()
# Atef_user.display_info()

Atef_user.spend_points(40)




