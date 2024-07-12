import time
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
rubles = 0
sociallevel = 0
job = "Unemployed"
suspiciousness = 0
nationality = 0
lovetomatharland = 0
freedom = 0
food = 0
def test():
    time.sleep(5)
    print(colored(0, 0, 0, "A long wait in the hall later..."))
    time.sleep(3)
    print(colored(255, 0, 0, "Hey, you, time for test "))
    time.sleep(3)
    print(colored(0, 0, 0, "It's an oral and written ideology test"))
    print((colored(255, 0, 0, "What is best way to solve world hunger? ")))
    print((colored(255, 0, 0, "1)Stalin  2)Investing in the countries  3)Better economy")))
    n = int(input("Action:   "))
    match n:
        case 1:
            print(colored(255, 0, 0, "Correct"))
        case _:
            print(colored(0, 0, 0, "The officer pulls out a hammer and a sickle and brutally murders you while singing the soviet union anthem"))
            print(colored(255, 0, 0, "You died"))
            exit()
    print((colored(255, 0, 0, "What is your opinion on the united states of america? ")))
    print((colored(255, 0, 0, "1)Just leave them be  2)Just as bad as soviet union  3)they should be destroyed and erased from existence")))
    n = int(input("Action:   "))
    match n:
        case 3:
            print(colored(255, 0, 0, "Correct"))
        case _:
            print(colored(0, 0, 0, "The officer pulls out a hammer and a sickle and brutally murders you while singing the soviet union anthem"))
            print(colored(255, 0, 0, "You died"))
            exit()
    print((colored(255, 0, 0, "What is your opinion on the korean war? ")))
    print((colored(255, 0, 0, "1)Kim il sung is an idiot  2)let's turn korea red with the help of great warrior kim il sung  3)the way people are being treated in the whole area is inhumane")))
    n = int(input("Action:   "))
    match n:
        case 2:
            print(colored(255, 0, 0, "Correct"))
        case _:
            print(colored(0, 0, 0, "The officer pulls out a hammer and a sickle and brutally murders you while singing the soviet union anthem"))
            print(colored(255, 0, 0, "You died"))
            exit()
    time.sleep(3)
    print((colored(255, 0, 0, "Welcome to soviet party comrade")))
    print(colored(0, 255, 0, 'your job is now: "communist party politician"'))
    job = "communist party politician"
print(colored(255, 0, 0, "A social and historical satire created by [REDACTED]"))
print(colored(255, 0, 0, "Around 20 million lives were lost to Joseph Stalin's communist regime\n even though it's been proved that communism is shit, there are still people who believe in it"))
time.sleep(10)
print(colored(255, 0, 0, "⠀⠀⠀⠀⠀⠀⢀⣤⣀⣀⣀⠀⠻⣷⣄\n⠀⠀⠀⠀⢀⣴⣿⣿⣿⡿⠋⠀⠀⠀⠹⣿⣦⡀\n⠀⠀⢀⣴⣿⣿⣿⣿⣏⠀⠀⠀⠀⠀⠀⢹⣿⣧\n⠀⠀⠙⢿⣿⡿⠋⠻⣿⣿⣦⡀⠀⠀⠀⢸⣿⣿⡆\n⠀⠀⠀⠀⠉⠀⠀⠀⠈⠻⣿⣿⣦⡀⠀⢸⣿⣿⡇\n⠀⠀⠀⠀⢀⣀⣄⡀⠀⠀⠈⠻⣿⣿⣶⣿⣿⣿⠁\n⠀⠀⠀⣠⣿⣿⢿⣿⣶⣶⣶⣶⣾⣿⣿⣿⣿⡁\n⢠⣶⣿⣿⠋⠀⠀⠉⠛⠿⠿⠿⠿⠿⠛⠻⣿⣿⣦⡀\n⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⡿"))
print(colored(255, 0, 0, "Welcome to Life in cccp, comrade"))
print(colored(255, 0, 0, "What's your nationality?\n 1)Soviet Union[easy]   2)Other countries[medium]  3)USA/UK[hard]"))
nationality = int(input("Action:    "))
match nationality:
    case 2:
        suspiciousness = 5
    case 3: 
        suspiciousness = 10
print(colored(255, 0, 0, "What's your dream job?\n (1)communist party politician[easy]   (2)A soldier[medium]  (Other):______[hard]"))
n = input("Action:    ")
match n:
    case '1':
        print(colored(255, 0, 0, "ok, let's make test to check if you are comrade enough"))
        test()
    case '2':
        print(colored(255, 0, 0, "Congratulations welcome to red army"))
        job = "soldat"
        time.sleep(3)
        print(colored(0, 255, 0, 'your job is now: "Soldier"'))
    case _:
        print(colored(255, 0, 0, "Actually we can put you on much better job"))
        time.sleep(3)
        print("Which job is it?")
        time.sleep(3)
        print(colored(255, 0, 0, "There is still room for you on tank factory"))
        job = "factory"
        time.sleep(3)
        print(colored(0, 255, 0, 'your job is now: "Factory Worker"'))
def work():
    match job: 
        case "soldat":
            print("you're now in the city of stalingrad, you and your comrades are inside of a building hiding from the enemy")
            time.sleep(5)
            print("when all of the suden")
            time.sleep(2)
            print("BANG")
            time.sleep(1)
            print("A bomb blows half of the building and therefore half of your comrades")
            time.sleep(3)
            print("after seeing some men you considered your brothers reduced to mere puddles of blood and gore\nyou realise the opening revealed your location")
            print("There is a Tiger I starting to rotate it's turret torwards you")
            n = input("you can: 1) hide on the bodies  2) find cover 3) end your suffering 4) throw a grenade at it")
            match n:
                case "3":
                    print(colored(255, 0, 0, "You died"))
                    exit()
                case "1":
                    print("The tank spots you while you're trying to hide inside \nof your friend's corpse and rapidly blows you up")
                    print(colored(255, 0, 0, "You died"))
                    exit()
                case "2":
                    print("The tank is no longer seeing you and you managed to survive, but left your firearm behind")
                    time.sleep(5)
                    print("all you have for self defense is your knife and your weak body \n(weak due to the fact that resources weren't sent properly and you're literally starving)")
                    time.sleep(7)
                    ina = input("You hear nazis climbing the stairs: 1) run torwards them and die for the motherland\n2) end your suffering 3) there's a window, try and jump ")
                    match ina:
                        case "1"|"2":
                            print(colored(255, 0, 0, "You died"))
                            exit()  
                        case "3":
                            print("you fall aproximatelly three floors and break you legs\nyou are now bleeding and dying but your suffering\nends because that Tiger I stomps over your head, blowing it")
                            print(colored(255, 0, 0, "You died"))
                            exit() 
                case "4":
                    print("even though the tank eviscerates the lower half of your body right after you throw the grenade\nthe grenade lands on top of the tank, killing some of the nazis still on it but \nnot coming anywhere near destroying the object since it was not an anti-tank grenade")
                    print(colored(255, 0, 0, "You died"))
                    exit() 
        case "communist party politician":
            print("c")
        case "factory":
            print("f")
def profile():
    print(f"{lovetomatharland} is the amount of love you have to the motherland")
def store():
    print("buy food")
print(" enter w to work ")
print(" enter p to view profile ")
print(" enter s to view store ")
print(" enter q to quit game (    you wouldn't dare :)     ) ")
inp = input("Action:    ")
while inp != "q":
    match inp:
        case "w":
            work()
        case "q":
            break
        case "p":
            profile()
        case "s":
            store()

print(f"you love the motherland {lovetomatharland} <- this much")
print("Do svidanya")