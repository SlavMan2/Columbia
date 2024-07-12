def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
import time
class Format:
    end = '\033[0m'
    underline = '\033[4m'
print(colored(0, 255, 0, "   _____ _____        _____ ______   _____  _____   ____   _____ _____            __  __  "))
print(colored(0, 255, 0, "  / ____|  __ \ /\   / ____|  ____| |  __ \|  __ \ / __ \ / ____|  __ \     /\   |  \/  | "))
print(colored(0, 255, 0, " | (___ | |__) /  \ | |    | |__    | |__) | |__) | |  | | |  __| |__) |   /  \  | \  / | "))
print(colored(0, 255, 0, "  \___ \|  ___/ /\ \| |    |  __|   |  ___/|  _  /| |  | | | |_ |  _  /   / /\ \ | |\/| | "))
print(colored(0, 255, 0, "  ____) | |  / ____ \ |____| |____  | |    | | \ \| |__| | |__| | | \ \  / ____ \| |  | | "))
print(colored(0, 255, 0, " |_____/|_| /_/    \_\_____|______| |_|    |_|  \_\\\____/ \_____|_|  \_\/_/    \_\_|  |_| "))
print("                                                             ")
print(colored(0, 0, 255, "                         type 'profile' to view your program's profile                    "))
print(colored(0, 255, 0, "                    type 'launch' to assemble and launch a rocket satelite                "))
print(colored(255, 255, 0, "                               type 'sell' to sell your research                          "))
print(colored(255, 255, 0, "                           type 'sell science' to sell your science                       "))
print(colored(0, 255, 255, "               type 'upgrade' to upgrade your hangar by ten modules for 10000 cash        "))
print(colored(0, 255, 0, "                       type 'mission' to make a mission to another planet                 "))
print(colored(255, 0, 0, "                      type 'exit' to quit the program and lose your progres               "))

cash = 10000
launches = 0
research = 0
science = 0
satelites = 0
heightofangar = 20
radars = [0, 0, 0, 0]
def profile():  
    print('you have $' + str(cash))
    print('your hangar is ' + str(heightofangar) + ' modules high')
    print('you flown ' + str(launches) + ' rockets')
    print('you have ' + str(research) + ' research')
    print('you have ' + str(science) + ' science')
    print('you have launched ' + str(satelites) + ' satelites')
    print('you have made ' + str(radars[0]) + ' missions to Mars')
    print('you have made ' + str(radars[1]) + ' missions to the Moon')
    print('you have made ' + str(radars[2]) + ' missions to Hoth')
    print('you have made ' + str(radars[3]) + ' missions to Dagobah')
def mission():
    print("you can have a maximum of " + str(heightofangar) + " modules")
    print("which destiny do you want to make a mission to  [planet:amount of booster modules needed]")
    print("0) Mars:20      1) Moon:10      2)Hoth:35     3)Dagobah:50")
    planet = "Starwars"
    while planet != "1" and planet != "2" and planet != "3" and planet != "0":
        planet = input("Action:     ")
    planet = int(planet)
    hhh = [20, 10, 35, 50]
    if hhh[planet] - 1 > heightofangar:
        print('your hangar is not big enought for this mission')
        return [False, 0, 0, 5]
    b = 0
    lifepods = 0
    cost = 100 
    hoh = heightofangar
    r = -1
    while r < 0 or r > hoh - 2:
        r = int(input("how many research facilities do you want (min 0, max " + str(hoh - 2) + "): "))
    d = (hoh - r) - 1
    while b < r or b > d:
        b = int(input("how many detacahble boosters do you want (min " + str(r) + ", max " + str(d) + "): "))
    p = b
    while lifepods < 1 or lifepods > hoh - (r + b):
        lifepods = int(input("how many lifepods do you want (min 1, max " + str(hoh - (r + b)) + "): "))
    asssssda = input("how many seconds till launch: ")
    h = int(float(asssssda) - (float(asssssda) % 1))
    f = h
    for i in range(h):
        print(f)
        f -= 1
        time.sleep(1)
    print(colored(255, 255, 0, '  /\  '))
    print(colored(255, 255, 0, ' /' + Format.underline + '  ' + Format.end + colored(255, 255, 0, '\ ')))
    for i in range(lifepods):
        print(colored(0, 255, 0, " |0=| "))
        cost += 500
    for i in range(r):
        print(colored(0, 0, 255, " |#-| "))
        cost += 600
    while p != 0:
        if p < 10:
            print(colored(255, 255, 0, ' |' + Format.underline + str(p) + ' ' + Format.end + colored(255, 255, 0, '| ')))
        if p >= 10:
            print(colored(255, 255, 0, ' |' + Format.underline + str(p) + Format.end + colored(255, 255, 0, '| ')))
        p -= 1
        cost += 200
    print(colored(255, 255, 0, '/____\ '))
    for i in range(b):
        print("  ||  ")
    print(" d||b ")
    print("dd||bb")
    r *= lifepods
    if hhh[planet] > b:
        time.sleep(3)
        print('your rocket crashed, mission failed')
        return [False, cost, 0, 5]
    print("you've made " + str(r) + " science")
    return [True, cost, r, planet]
def launch():
    print("you can have a maximum of " + str(int(heightofangar)) + " modules")
    b = 0
    cost = 100 
    hoh = heightofangar
    r = -1
    while r < 0 or r > hoh / 2:
        r = int(input("how many research facilities do you want (min 0, max " + str(int(hoh / 2)) + "): "))
    d = hoh - r
    while b < 1 or b > d:
        b = int(input("how many detacahble boosters do you want (min 1, max " + str(d) + "): "))
    p = b
    h = int(input("how many seconds till launch: "))
    f = h
    for i in range(h):
        print(f)
        f -= 1
        time.sleep(1)
    print(colored(255, 255, 0, '  /\  '))
    print(colored(255, 255, 0, ' /' + Format.underline + '  ' + Format.end + colored(255, 255, 0, '\ ')))
    for i in range(r):
        print(colored(0, 0, 255, " |#-| "))
        cost += 50
    while p != 0:
        if p < 10:
            print(colored(255, 255, 0, ' |' + Format.underline + str(p) + ' ' + Format.end + colored(255, 255, 0, '| ')))
        if p >= 10:
            print(colored(255, 255, 0, ' |' + Format.underline + str(p) + Format.end + colored(255, 255, 0, '| ')))
        p -= 1
        cost += 30
    print(colored(255, 255, 0, '/____\ '))
    for i in range(b):
        print("  ||  ")
    print(" d||b ")
    print("dd||bb")
    r += b // 4
    print("you've made " + str(r) + " research")
    return [True, cost, r]
inpu = input("Action:   ")
while inpu != 'exit':
    if inpu == 'profile':
        profile()
    if inpu == 'launch':
        t = launch()
        cash -= t[1]
        research += t[2]
        if t[0]:
            launches += 1
            satelites += 1
    if inpu == 'mission':
        t = mission()
        cash -= t[1]
        science += t[2]
        if t[0]:
            launches += 1
            radars[t[3]] += 1
    if inpu == 'sell':
        cash += research * 100
        research = 0
    if inpu == 'sell science':
        cash += science * 500
        science = 0
    if inpu == 'upgrade':
        if cash >= 10000:
            heightofangar += 10
            cash -= 10000
    print(colored(0, 0, 255, "                         type 'profile' to view your program's profile                    "))
    print(colored(0, 255, 0, "                    type 'launch' to assemble and launch a rocket satelite                "))
    print(colored(255, 255, 0, "                               type 'sell' to sell your research                          "))
    print(colored(255, 255, 0, "                           type 'sell science' to sell your science                       "))
    print(colored(0, 255, 255, "               type 'upgrade' to upgrade your hangar by ten modules for 10000 cash        "))
    print(colored(0, 255, 0, "                       type 'mission' to make a mission to another planet                 "))
    print(colored(255, 0, 0, "                      type 'exit' to quit the program and lose your progres               "))
    inpu = input("Action:   ")
print("Goodbye")