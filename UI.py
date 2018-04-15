import character as ch
import combatHandler
false=False;
true=True;



def getItemNames():
    s = 'Items: ';
    for item in itemList:
        s+=item.name
        s+='  '
    return s;

def isGameOver():
    isOver = true;
    for item in combatHandler.allies:
        if(item.isConscious):
            isOver = false;
    return isOver;

def printValues():
    printString = 'Allies: \n'
    for ally in combatHandler.allies:
        printString += (ally.name + ": aggro=" + str(ally.aggro) + ", hp percent=" + str(100*ally.hp/ally.maxhp) + ", Are they conscious=" + str(ally.isConscious) + "\n")
    printString += 'Enemies: \n'
    for ally in combatHandler.enemies:
        printString += (ally.name + ": hp percent=" + str(100*ally.hp/ally.maxhp) + ", Are they conscious=" + str(ally.isConscious) + "\n")
    print(printString);
def userTurn():
    for ally in combatHandler.allies:
        if(ally.isConscious):
            printValues();
            stringInput='';
            valid=false;
            print('Action for ' + ally.name);
            while(not valid):
                stringInput = input("Actions: 0: attack/heal, 1: item, 2: skip turn\n");
                if(stringInput == '1' or stringInput == '2' or stringInput == '0'):
                    valid = true;
                    if(stringInput=='0'):
                        if(ally.Ctype == ch.charType.healer):
                            printString = 'Targets to heal: ';
                            length = len(combatHandler.allies);
                            for i in list(range(0,length)):
                                printString += (str(i) + ': ' + combatHandler.allies[i].name + ', ');
                            printString = (' '.join(printString.split())[:-1]) + '\n';
                            isValid = false;
                            while(not isValid):
                                stringInput = input(printString);
                                if(int(stringInput) >= 0 and int(stringInput) <= len(combatHandler.allies)):
                                    isValid = true;
                                    ally.attack(combatHandler.allies[int(stringInput)])
                                    print("");
                                else:
                                    print('Invalid input');
                        else:
                            printString = 'Targets to attack: ';
                            length = len(combatHandler.enemies);
                            for i in list(range(0,length)):
                                printString += (str(i) + ': ' + combatHandler.enemies[i].name + ', ');
                            printString = (' '.join(printString.split())[:-1]) + '\n';
                            isValid = false;
                            while(not isValid):
                                stringInput = input(printString);
                                if(int(stringInput) >= 0 and int(stringInput) <= len(combatHandler.allies)):
                                    isValid = true;
                                    ally.attack(combatHandler.enemies[int(stringInput)])
                                    print("");
                                else:
                                    print('Invalid input');
                    elif(stringInput=='1'):
                            printString = 'Items to use: ';
                            length = len(combatHandler.itemList);
                            for i in list(range(0,length)):
                                printString += (str(i) + ': ' + combatHandler.itemList[i].name + ', ');
                            printString = (' '.join(printString.split())[:-1]) + '\n';
                            isValid = false;
                            while(not isValid):
                                stringInput = input(printString)
                                if(int(stringInput) >= 0 and int(stringInput) <= len(combatHandler.itemList)):
                                    isValid = true;
                                    itemToUse = stringInput;
                                    thirdLevelValid = false;
                                    
                                printString = 'Targets to heal: ';
                                length = len(combatHandler.allies);
                                for i in list(range(0,length)):
                                    printString += (str(i) + ': ' + combatHandler.allies[i].name + ', ');
                                printString = (' '.join(printString.split())[:-1]) + '\n';
                                while(not thirdLevelValid):
                                    stringInput = input(printString);
                                    if(int(stringInput) >= 0 and int(stringInput) <= len(combatHandler.allies)):
                                        thirdLevelValid = true;
                                        #ally.attack(combatHandler.allies[int(stringInput)])
                                        combatHandler.itemList[int(itemToUse)].use(combatHandler.allies[int(stringInput)]);
                                        print("");
                                    else:
                                        print('Invalid input');
                    else:
                        ally.aggro -= 5;
                else:   
                    print('Invalid input.')
        else:
            print(ally.name + " is not awake, therefore they cannot perform an action this turn.\n")
while(not isGameOver()):
    userTurn();
    print('---------------------------------')
    combatHandler.enemyAttack();
    print('---------------------------------')
