import time, random, os
print "You wake up in a forest. Use the commands W,A,S,D,to move."
print "Use I to check your inventory, HP to check your health points."
cordx = 3
cordy = 3
a = 1
inv=["a cat"]
HP=100
something=(1,2,3,4,5,6,7,8,9,10,13)
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
        playerinvcheck = 0
        cordx = 0
        cordy = 0
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
                        speech = raw_input(('What do you do? \n 1. Ask for a story \n 2. Kill him \n'))
                        if speech == "2":
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
                        if speech == "1":
                                print " He says: Two vast and trunkless legs of stone \n Stand in the desart. Near them, on the sand, \n Half sunk, a shattered visage lies, whose frown, \n And wrinkled lip, and sneer of cold command,\n Tell that its sculptor well those passions read\n Which yet survive, stamped on these lifeless things,\n The hand that mocked them and the heart that fed:\n And on the pedestal these words appear:\n My name is Ozymandias, king of kings:\n Look on my works, ye Mighty, and despair!\n Nothing beside remains. Round the decay\n Of that colossal wreck, boundless and bare\n The lone and level sands stretch far away"
                
                if popup ==(2):
                        print "You come upon a ruined castle."
                        action = input(("What you do? \n1.Search it \n2.Leave\n"))
                        if action == 1:
                                result = random.randint(1, 3)
                        if result == (1):
                                print "You find nothing of interest."
                        if result == (2):
                                print "You find a bronze talisman."
                        if result == (3):
                                print "You find a large rat."
                                speech = raw_input(('What do you do? \n 1. Run \n 2. Kill it \n'))
                                if speech == "2":
                                        print "Pick a number from 1 to 10."
                                        numb = random.randint(1,10)
                                        comb = input((''))
                                if comb != numb:
                                        print "You stand over it's bloody body. It carries nothing of value. "
                                        time.sleep(2)
                                if comb == numb:
                                        print "It carries a rare type of rabies. You die instantly."
                                        time.sleep(5)
                                        exit()
        
                        
move()
 

