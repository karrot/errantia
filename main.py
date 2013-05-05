import time, random, os
print "You wake up in a forest. Use the commands W,A,S,D,to move."
print "Use I to check your inventory, HP to check your health points."
cordx = 1
cordy = 1
a = 1
def pmap(cordx, cordy):
    os.system('cls')
    tempy = cordy
    while tempy > (1):
        print "x x x x x x x x x "
        tempy = (tempy - 1)
        
    temp = cordx
    while temp > (1):
        print "x",
        temp = (temp - 1)
    print "O",
    left= 10 - cordx
    while left > 1:
        print "x",
        left = left - 1
    print ""
    lefty= 11 - cordy
    while lefty > 1:
        print "x x x x x x x x x "
        lefty = lefty - 1
def move():
    global inv
    inv=[]
    global HP
    HP=100
    global luck
    luck=0
    global gold
    gold=0
    global area
    area=0
    if area == 0:
        something=(1,2,3,4,5,6,7,8,9,10,13)
    if area == 1:
        something=(101,102,103,104,105,106,107,108,109,110,113)
    playerinvcheck = 0
    cordx = 1
    cordy = 1

    while a == (1):

        m = (raw_input("Where to?"))
        if m == ("w"):
            cordy = (cordy - 1)
        if m == ("s"):
            cordy = (cordy + 1)
        if m == ("d"):
            cordx = (cordx + 1)
        if m == ("a"):
            cordx = (cordx - 1)
        if m == ("i"):
            playerinvcheck = 1
        popup = random.choice(something)
            
        print "You are at:"
        print "X"
        print (cordx)
        print "Y"
        print (cordy)
        pmap(cordx, cordy)
        if playerinvcheck == 1:
            playerinvcheck = 0
            print inv
            print "\n"
        if popup ==(1):
            print "You meet a traveler from an antique land"
            command = raw_input(('What do you do? \n 1. Ask for a story \n 2. Kill him \n'))
            if command == "2":
                print "He draws his blade. Pick a number from 1 to 3."
                numb = random.randint(1,3)
                comb = input((''))
                if comb == numb:
                    print "You stand over his bloody body. It carries nothing of value. "
                    time.sleep(2)
                if comb != numb:
                    print "He stabs you in the chest. Your last memory is blood spilling everywhere."
                    time.sleep(5)
                    exit()
            if command == "1":
                print " He says: Two vast and trunkless legs of stone \n Stand in the desart. Near them, on the sand, \n Half sunk, a shattered visage lies, whose frown, \n And wrinkled lip, and sneer of cold command,\n Tell that its sculptor well those passions read\n Which yet survive, stamped on these lifeless things,\n The hand that mocked them and the heart that fed:\n And on the pedestal these words appear:\n My name is Ozymandias, king of kings:\n Look on my works, ye Mighty, and despair!\n Nothing beside remains. Round the decay\n Of that colossal wreck, boundless and bare\n The lone and level sands stretch far away"
            else:
                print ""
        if popup ==(2):
            print "You come upon a ruined castle."
            command = raw_input(("What you do? \n1.Search it \n2.Leave\n"))
            if command == "1":
                dice = random.randint(1, 3)
                if dice == (1):
                    print "You find nothing of interest."
                if dice == (2):
                    print "You find a bronze talisman."
                    inv.append("Bronze Talisman")
                    print inv
                if dice == (3):
                    print "You find a large rat."
                    command = raw_input(('What do you do? \n 1. Run \n 2. Kill it \n'))
                    if command == "1":
                        print "The rat takes no interest in you as you run away."
                    if command == "2":
                        print "Pick a number from 1 to 10."
                        numb = random.randint(1,10)
                        comb = input((''))
                        if comb != numb:
                            print "You stand over it's bloody body. It carries nothing of value."
                            time.sleep(2)
                        if comb == numb:
                            print "It carries a rare type of rabies. You die instantly."
                            time.sleep(5)
                            exit()
            if command=="2":
                print "You leave without taking much notice of the castle."
            else:
                print ""
        if popup ==(3):
            print "You come across a town"
            command = raw_input("What do you do? \n1.Try and steal something \n2.Look for work\n3.Leave\n")
            if command =="1":
                dice = random.randint(1,7)
                if dice == (1):
                    print "You loot 1 Gold and a Steak."
                    gold+=1
                    inv.append("Steak")
                    print inv
                    print "You have",gold,"gold."
                if dice == (2):
                    print "You loot 1 Gold."
                    gold+=1
                    print "You have",gold,"gold."
                if dice ==(3):
                    print "You loot a shovel."
                    inv.append("Shovel")
                    print inv
                if dice == (4):
                    print "You loot an amulet of luck from a priest. +1 to luck power."
                    luck+=1
                    print "You have",luck,"luck."
                if dice== (5):
                    print "The villagers catch you and attack you. You lose 10 HP. You lose 2 Gold."
                    gold-=2
                    HP-=10
                    print "You have",HP,"health points."
                    print "You have",gold,"gold."
                if dice== (6):
                    print "The villagers catch you and attack you. You lose 10 HP. You lose 2 Gold."
                    gold-=2
                    HP-=10
                    print "You have",HP,"health points."
                    print "You have",gold,"gold."
                if dice== (7):
                    print "The villagers catch you and attack you. You lose 10 HP. You lose 2 Gold."
                    gold-=2
                    HP-=10
                    print "You have",HP,"health points."
                    print "You have",gold,"gold."
            if command == "2":
                    print "The villagers tell you of the expedition the desert of Ne'Vada. If you can find the expediton leader, you could join."
            else:
                 print""
        if popup ==(4):
            print "You come upon a small city"
            command = raw_input("What do you do? \n1.Try and steal something \n2.Look for work\n3.Leave\n")
            if command =="1":
                dice = random.randint(1,3)
                if dice == 1:
                    print "You find nothing of value"
                if dice == 2:
                    print "You find a hatchet"
                    inv.append("Hatchet")
                    print inv
                if dice == 3:
                    print "You are chased out of town by guards"
            if command == "2":
                    print "You walk into the local inn. A man offers to take you on his expedition to the desart of Ne'Vada"
                    command = raw_input("What do you do? \n1.Say yes\n2.Say no\n")
                    if command == "1":
                        area =1
                    else:
                        print "You leave the city"
            if command=="3":
                 print"You leave the city unnoticed."
        
            else:
                print ""
while True:
    move()

