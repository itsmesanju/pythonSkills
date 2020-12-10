class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power,email):
#        User.__init__(self, email)
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power: {self.power}")

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    def attack(self):
        print(f"Attacking with arrows: left {self.num_arrows}")

wizard1=Wizard('WizardName', 60, 'itsmesanju@gmail.com')
archer1=Archer('Sanju',30)

print(dir(wizard1))
#check if its instance
print(isinstance(wizard1,Wizard))
#print(isinstance(wizard2,Wizard))

'''Function below'''

def player_attack(character):
    character.attack()

player_attack(wizard1)
player_attack(archer1)

for characters in [wizard1, archer1]:
    characters.attack()
