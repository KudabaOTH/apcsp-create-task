import random;
true = True;
false = False;

class charType():
    attack = 1;
    healer = 2;
    tank = 3;

class character:
    aggro = 0;
    name = ""
    Ctype = charType.attack;
    maxhp = 0;  #The maximum health points that can be possessed by the given character
    hp = 0; #The current health points
    strength = 0; #The attack value of the given character
    resistance = 0; #The resistance value of the given character, not less than one
    accuracy = 0; #The accuracy of a given character, not used in healers, usually between 100 and 75
    evasion = 0; #The evasion level of a given character, usually between 1 and 1.5
    isConscious = true;
    def __init__(self, m_name, m_maxhp, m_strength, m_resistance, m_accuracy, m_evasion, m_type):
        self.name = m_name;
        self.maxhp = m_maxhp;
        self.hp = self.maxhp;
        self.strength = m_strength;
        self.resistance = m_resistance;
        self.accuracy = m_accuracy;
        self.evasion = m_evasion;
        self.Ctype = m_type;
    def attack(self, target):
        if(self.Ctype == charType.attack or self.Ctype == charType.tank):
            self.aggro += 13;
            if(self.Ctype == charType.tank):
                self.aggro += 2;
            print(self.name + " attacks " + target.name + ".")
            accuracyCheck = random.randrange(0,100,1); #Generates a random integer between 0 and 100
            accuracyVal = self.accuracy/target.evasion; #Generates the value of accuracy RNG needed for a hit
            if(accuracyCheck <= accuracyVal):
                print("The attack hit and dealt " + str((self.strength/target.resistance))  + " Points of damage.");
                target.getHit(self.strength/target.resistance);
                
            else:
                print("But it missed!");
        elif(self.Ctype == charType.healer):
            target.getHealed(self.strength);
            self.aggro += 10;
            print(self.name + " Healed " + target.name + " for " + str(self.strength) + " Points.")
                   
    def getHit(self, amount):
        self.hp -= amount;
        if(self.hp <= 0):
            self.hp = 0;
            self.isConscious = false;
            print(self.name + " passed out.");
    def getHealed(self, healAmount):
        self.hp += int(healAmount);
        if(self.hp > self.maxhp):
           self.hp = self.maxhp;
    def getFullHealed(self):
        self.hp = self.maxhp;
    def getRevived(self):
        self.hp += (self.maxhp * 0.3);
        if(self.hp > self.maxhp):
            self.hp = self.maxhp;
        self.isConscious = true;
