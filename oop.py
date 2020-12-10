class User(object):
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power):
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

wizard1=Wizard('WizardName', 60)
wizard2=Wizard('Wizard2', 60)
archer1=Archer('Sanju',30)

print(len(wizard1.name))
#check if its instance
print(isinstance(wizard1,Wizard))
print(isinstance(wizard2,Wizard))

'''Function below'''

def player_attack(character):
    character.attack()

player_attack(wizard1)
player_attack(archer1)

for characters in [wizard1, archer1]:
    characters.attack()
