class liquid:
    air = 0;
    healthPotion = 1;
    water = 2;

class potion:
    name = ''
    liquid = 0;
    def __init__(self, m_liquid):

        if(m_liquid == liquid.air):
            self.name = 'Potion of Air';
        elif(m_liquid == liquid.healthPotion):
            self.name = 'Health Potion'
        elif(m_liquid == liquid.water):
            self.name = 'Water Potion'
        self.liquid = m_liquid;
        

        
    def use(self, target):
        print('used')
        if(self.liquid == liquid.healthPotion):
            target.getFullHealed();
            self.liquid = liquid.air;
            print(target.name + " was fully healed.");
            self.name = 'Potion of Air';
        elif(self.liquid == liquid.water):
            target.getRevived();
            self.liquid = liquid.air;
            print(target.name + " was revived and healed 30 percent.");
            self.name = 'Potion of Air'
        elif(self.liquid == liquid.air):
            print("You fill the potion with water from a nearby river.");
            self.liquid = liquid.water;
            self.name = 'Potion of Water';
