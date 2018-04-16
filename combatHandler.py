import character as ch
import random
import Items
        
true = True;
false = False;
debugList=[];
#Format: Name, max hp, strength, resistance, accuracy, evasion, type
Xanu = ch.character("Xanu", 220, 175, 1.2, 90, 1.1, ch.charType.attack);
Sepha = ch.character("Sepha", 150, 80, 1, 80, 1.7, ch.charType.healer);
Kitzurea = ch.character("Kitzurea", 230, 125, 1.5, 85, 0.75, ch.charType.tank);
Xanu.aggro+=25;
Sepha.aggro+=25;
Kitzurea.aggro+=25;

allies = [Xanu, Sepha, Kitzurea];

Fauron = ch.character("Fauron", 250, 145, 1.2, 85, 1.2, ch.charType.attack);
Loranu = ch.character("Loranu", 200, 85, 1, 80, 1.5, ch.charType.healer);
Hisipha = ch.character("Hisipha", 270, 120, 1.4, 90, 0.9, ch.charType.tank);

enemies = [Fauron, Loranu, Hisipha];

itemList = [Items.potion(1), Items.potion(Items.liquid.healthPotion), Items.potion(Items.liquid.water)];


def gameOverCheck():
    isOver = true;
    for ally in allies:
        if(ally.isConscious):
            isOver = false;
    if(isOver):
        print('Game over.')
    return isOver;

def enemyAttack():
    if(not gameOverCheck()):
        aggros = [0];
        for i in allies:
            aggros.append(0);
        health = [];
        enemyHealth = [];
        percentHealth = 0.0;
        counter = 0;
        for enemy in enemies:
            health.append(0);
            enemyHealth.append(enemy.hp / enemy.maxhp);
            counter += 1;
            counter = 0; 
        sum = 0;
        for ally in allies:
            sum = 0;
            if(ally.isConscious):
                sum += ally.aggro;
                health[counter] = ally.hp;
            counter+=1;
        for enemy in enemies:
            if(enemy.Ctype == ch.charType.healer):
               if(enemy.isConscious == true):
                    lowestPercentEnemy = 0;
                    percentOfLowestPercentEnemy = 101;
                    for newEnemy in enemies:
                        if(newEnemy.isConscious):
                            percent = (newEnemy.hp/newEnemy.maxhp);
                            if(percent < percentOfLowestPercentEnemy):
                                lowestPercentEnemy = newEnemy;
                                percentOfLowestPercentEnemy = percent;
                    enemy.attack(lowestPercentEnemy);


                
            elif(enemy.isConscious == true):
                values = [];
                sum = 0;
                for ally in allies:
                    if(ally.isConscious):
                        for num in range(ally.aggro):
                            values.append(ally);
                            sum+=1;
                for i in range(random.randint(1,30)):
                    aggroStrike = random.randint(1, sum);                       #Run lots of times to see if that fixes bug of not random enough
                debugList.append(aggroStrike);
                counter = 0;
                index = 1;
                enemy.attack(values[aggroStrike])

            if(gameOverCheck()):
                break;

    
