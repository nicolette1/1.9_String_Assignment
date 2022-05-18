# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#UEFA Euro 1988 Final
scorer_1 = "Ruud Gullit"
scorer_2 = "Marco van Basten"
goal_0 = 32
goal_1 = 54

scorers = scorer_1 + " " + str(goal_0) + ", " + scorer_2 + " " + str(goal_1)
print (scorers)
#print(f'{scorer_1} scored in the {str(goal_0)}nd minute\n{scorer_2} scored in the {str(goal_1)}th minute')
report = f'{scorer_1} scored in the {goal_0}nd minute\n{scorer_2} scored in the {goal_1}th minute'
print (report)

#OPDRACHT 2.1
player = "Adri van Tiggelen"
# player = "Erwin Koeman"            # andere optie, checken meerder spelers
# player = "Arnold Mühren"           # andere optie, checken meerder spelers
# player = "Hans van Breukelen"      # andere optie, checken meerder spelers
# player = "Berry van Aerle"         # andere optie, checken meerder spelers

#OPDRACHT 2.2 Players first name
#first_space = player.find(" ")      # vindt de plaats van de eerste spatie
#print (first_space)                 # print de plaats van de eerste spatie
#first_name_slice = slice(first_space)  # first_name begin 0 tot eerste spatie
#print (player[first_name_slice])             # controle print
#print (player[slice(first_space)])  # hoe naar 1 regel, stapjes
#print (player[slice(player.find(" "))])    # hoe naar 1 regel, stapjes
first_name = (player[slice(player.find(" "))])  # uiteindelijke 1 regel!!smiley
print(first_name)                      # controle print
#test of de verkorte schrijfwijze ook werkt, dat is inderdaad het geval:
#first_name = (player[:(player.find(" "))])  # uiteindelijke 1 regel!!smiley
#print(first_name)                      # controle print

#OPDRACHT 2.3 Length Players last name
#first_space = player.find(" ")      # vindt de plaats van de eerste spatie
#print (first_space)                 # print de plaats van de eerste spatie
#last_name_slice = slice((first_space +1),len(player))    # last_name begin 1 plaats na spatie tot einde
#print (player[last_name_slice])             # controle print
#print (player[slice((first_space +1),len(player))]) # hoe naar 1 regel, stapjes
#print (player[slice(((player.find(" ")) +1),len(player))])  # hoe naar 1 regel, stapjes
last_name = (player[slice(((player.find(" ")) +1),len(player))]) # uiteindelijke 1 regel!!smiley
#last_name_len = len(last_name)
print(last_name)                      # controle print
#print (len(last_name))                  # controle print
#print(last_name_len)                    # controle print

last_name_len = len((player[slice(((player.find(" ")) +1),len(player))]))
print(last_name_len)

#OPDRACHT 2.4 Players name in this format: G. von Examplestein
#x = slice(1)
#first_name_short = (first_name[x])
#print(first_name_short)
#punt = ". "
#name_short = first_name_short + punt + last_name
#print(name_short)
# nu is de vraag hoe ik dit in één regel ga krijgen
# stapje voor stapje aanpakken, steeds terugwerken, componenten vervangen
#name_short = first_name_short + ". " + last_name
#name_short = (first_name[slice(1)]) + ". " + last_name  #last_name nog gebruikt, mag niet
#print (name_short)              # controle print

#Eigenlijk is last_name hier nu extra gebruikt als lijn code.....misschien later naar kijken. Het is nu niet "single line of code" meer....?
#Oplossing:
name_short = (first_name[slice(1)]) + ". " + (player[slice(((player.find(" ")) +1),len(player))])
print (name_short)

# YES Gelukt om het "single line of code" te krijgen JOEPIE

#OPDRACHT 2.5 Uitroep naam met uitroepteken * aantal letters voornaam
# Wat we nodig hebben: (voornaam + !)* (len van voornaam)
#number_of_repeats = len(first_name) # aantal letters in voornaam
#print (len(first_name))             # controle print
#chant_1 = (first_name + "! ")*(len(first_name))    #doet t met spatie
#print (chant_1)                                    #controle print
#Nu is het laatste karakter nog een spatie. Deze moet er dus vanaf. Daarvoor chant printen van begin tot -1, dan wordt het laatste karakter niet meegenomen.
#print (chant_1[:-1])        #controle print
#Dit heeft een goede uitkomst, maar is nog niet wat er gevraagt wordt. Daarbij moet er bij chant zelf al een spatie af zijn.
#Dus nu nog niet alles in één regel, weet even niet hoe ik dat kan doen:
# Misschien als ik er een spatie aftrek, nee:lukt niet.
# Dan maar uitroep * len (-1)  + uitroep * 1
#chant_2 = (first_name + "! ")*((len(first_name))-1)+ (first_name + "!") #doet t maar niet mooi
#print(chant_2)     #controle print
# Dit is echter niet mooi. Een andere optie is slicen
#chant_3 = (first_name + "! ")*(len(first_name)) #lukt,meerder regels nodig
#x = slice(0,-1)                               #lukt, maar meerder regels nodig
#print (chant_3[x])                            #lukt, maar meerder regels nodig
#Dit heeft goede uitkomst. Kan dit ook in één regel?:
#chant_4 = (str(first_name + "! ")* (len(first_name)))[slice(0,-1)]
#print(chant_4)             #controle print
# Dit werkt dus alleen als je er een string van maakt!
# anders opmerking: 'int' object is not subscriptable

# nog n andere poging die ook werkt, nog kortere schrijfwijze:
#chant_5 = str((first_name + "! ")* ((len(first_name))))[0:-1]
#print(chant_5)              #controle print
# Dit werkt dus alleen als je er een string van maakt!
# anders opmerking: 'int' object is not subscriptable
# Gelukkig het werkt nu! dus nu even voor de opdracht:
chant = str((first_name + "! ")* ((len(first_name))))[0:-1]
print(chant)

#OPDRACHT 2.6 
# Ik heb hier de oude chant (chant_1) vergeleken met de nieuwe chant (chant)
#good_chant = chant_1 != chant
#print(good_chant)
# Ik krijg een goede uitkomst (namelijk True), maar het staat nog niet in één regel....ik gebruik chant_1 en chant. Er is waarschijnlijk een andere oplossing.
# Iets anders verzinnen dus:
good_chant = "Adri! Adri! Adri! Adri! " != chant
print (good_chant)
