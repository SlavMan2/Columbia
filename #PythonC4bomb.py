#Python C4 bomb
#FOLIUM
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
import random
pincode = [] 
hman = int(input("How many numbers: "))
for i in range(hman):
    pincode.append(str(random.randint(0, 9)))
pin = ""
for i in pincode:
    pin += i

tries = int(input("How many tries: "))
inp = 23112332123
while int(inp) != int(pin):
    inp = input("")
    while inp.isdigit() == False or len(inp) != len(pin): 
        inp = input("put it right dumbass ")
    for i in range(len(pin)):
        if i != len(pin) - 1:
            if inp[i] == pin[i]:
                print(colored(0, 255, 0, "C"), end="")
            elif inp[i] in pin:
                print(colored(255, 255, 0, "E"), end="")
            else:
                print(colored(255, 0, 0, "E"), end="")
        if i == len(pin) - 1:
            if inp[i] == pin[i]:
                print(colored(0, 255, 0, "C"))
            elif inp[i] in pin:
                print(colored(255, 255, 0, "E"))
            else:
                print(colored(255, 0, 0, "E"))
    tries -= 1
    if tries > -1 and int(inp) != int(pin):
        print(tries)
    if tries < 0 and int(inp) != int(pin):
        print(colored(255, 0, 0, "EVERYONE IN THE BUILDING (INCLUDING YOU) ENDED UP DEAD DUE TO YOUR MISERABLE INCOMPETENCE "))
        print(pin)
        exit()
print(colored(0, 255, 0, "DONE"))