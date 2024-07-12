inp = input("Enter grade here: press 'q' when done: ").lower()
while not inp.isdigit() and not inp == 'q':
        print("Not a number friend")
        inp = input("Enter grade here: press 'q' when done: ").lower()
sol = []
while True:
    if int(inp) < 0:
         inp = '0'
    sol.append(int(inp))
    inp = input("Enter grade here: press 'q' when done: ").lower()
    while not inp.isdigit() and not inp == 'q':
        print("Not a number friend, we can't handle negative numbers here")
        inp = input("Enter grade here: press 'q' when done: ").lower()
    if inp == 'q':
        break
    
        
so = 0
for i in sol:
    so += i
dada = 0
if len(sol) != 0:
    dada = so / len(sol)
print(dada)