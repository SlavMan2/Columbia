'''name = input("name here: ")
feeling = input("feeling here: ")
candies = input("candies here: ")
print("Hey ", name,", I heard you are ", feeling, " probably because you had ", candies," candies")
print(r"cyka \n")
print(len("me"))
print("hahahahahopachkicykablyaaaaaaaaaaaaaaaaaaaaa".count("a"))'''
#STRING
'''us = input("name: ")
print(len(us))
print(us.count('m'))'''
#STRING
'''d = 0
da = 0
for u in us:
    da += 1
    if u == 'm':
        d += 1
print(d)
print(da)'''
#STRING
'''ino = input("")
print(ino[len(ino) - 1])
ru= 'RASSIA XAXAXA'
print(ru[0:6])
print(ino.upper())
print(ru.lower())
print(ru.title())'''
#STRING
'''phrase = " It's an awful day to learn programming "
phrase = phrase.replace("awful", "wonderful")
phrase = phrase.replace("an", "a")
phrase = phrase.strip()
print(phrase)'''
#FORMATING
'''moni = int(input(""))
print(f"{moni:.2f}")'''
'''moni = int(input(""))
print(f"{moni:.3f}")'''
'''moni = int(input(""))
print(f"{moni:,}")'''
'''moni = int(input(""))
print(f"{moni:,.2f}")'''
'''nomber = 123123
print(f"{nomber:0>8}")'''
'''nomber = 123123
print(f"{nomber:0<8}")'''
'''nomber = 123123
print(f"{nomber:0^8}")'''
#find
'''p = "da da nyet"
print(p.find('nyet'))
'''
#from x to y
'''p="apsdaokdof"
print(p[1:3])'''
#Go to right
'''assignment_n = "plplplp"
print(f"{assignment_n:^225}")'''
#conditionals
'''sshconectionestabilished = True
if sshconectionestabilished:
    print("Time for Privilege escalation")
else:
    print("find or bruteforce passwd")'''
#pets cond
'''
pet = bool(int(input("pet? 1 or 0 ")))
dog = bool(int(input("dog? 1 or 0 ")))
if pet:
    if dog:
        print("doguinho ")
    else: 
        print("no doguinho ")
else:
    print("noanimal cyka nahuy asdnjkafiouabfahfiafiabfaf")
    '''
#long name
'''#name
import time
name = input("name here:  ")
if len(name) > 15:
    print("long name bro")
else:
    print("It's not as big as I imagined")
    time.sleep(3)
    print("that's what she said")'''
#grade
'''g = int(input("what grade   "))
if g < 65:
    print("f")
elif g >= 65 and g < 70:
    print("d")
elif g >= 70 and g < 80:
    print("c")
elif g >= 80 and g < 90:
    print("b")
elif g >= 90:
    print("a")'''
#matchpet
'''pet = input("whatpet")
match pet: 
    case "cat"|"lion":
        print("cat go meow")
    case "dog":
        print("dog go whoof")
    case "n":
        print("no dog i-i")
    case _:
        print("wtf bruh")'''
#matchnumber
'''g = int(input("wat "))
match g:
    case _ if g >= 90:
        print("a")
    case 80|81|82|83|84|85|86|87|88|89:
        print("b")
    case 70|71|72|73|74|75|76|77|78|79:
        print("c")
    case 65|66|67|68|69:
        print("d")
    case _:
        print("f")'''
#TRY EXCEPT
'''
try:
    grade = int(input("int "))
    if grade >90:
        print("a")
except Exception as e:
    print("why")'''
#music
'''amount = 10
l = 0
import random
import time
n = "never gonna give you up"
d = ["never gonna give you up", "to the town of agua fria rode a stranger one fine day", "back in black", "rastvietali iabloni i grushi"]
while amount >= l:
    time.sleep(0.5)
    print(n)
    l += 1
    if l > amount:
        l = 0
        n = d[random.randint(0, 3)]
'''
#fizz rizz
'''n = 0
g = int(input("Number: "))
while n < g:
    n += 1
    if n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz cykablyat")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)'''
#don't press q
'''n = 0
while n != 10:
    n+=1
    da = input("Don't press Q:")
    if da.lower() == 'q':
        break
    print(da)
    print(f"song for the {n}th time ")'''
#random
'''import random
r = random.randint(1, 10)
s = 111
while s != r:
    s = int(input(""))
    if s == r:
        print("davai")
    else:
        print("incorrect")'''
#for loop
'''vowels = "aeiou"
for v in vowels:
    print(f"{v} is vowel hahahah")
for i in range(9,1, -1):
    print("kdao")
for i in range(1,9):
    print("kdao")'''
#factorial
'''n = int(input(""))
z = 1
for i in range(n):
    
    z = z * (i+1)
print(z)'''
#tuples
'''simple_tuple = ("Math", "Chemistry", "Programming", "Global histroy", "Philisophy")
print(len(simple_tuple))
print(simple_tuple[1:3])

tuples = "m","n","s"
a, b, c = tuples
print(a, b, c)'''
'''classes = ("Math", "Chemistry", "programming", "Global History", "Philosophy")
for i in classes:
    if (i != "programming"):
        print(i)'''
#mtuples
'''t = "professot ahmed", ("Python", "9 to 11"), ("Python", "1 to 3")
for i in t:
    if type(i) == tuple:
        for j in i:
            if j != "Python":
                print(j)'''
#list
'''l = ["fa", "es", "ew", "uaaa"]
print(l[0::2])'''
#loop
'''l = [1, 2, 3, "four", 5, 6, 7, "eight", 9]
for i in l:
    match i:  
        case _ if type(i) == str:
            l[l.index(i)] = l.index(i) + 1
print(l)'''
#put value in already existing place
'''
l = [1, 1, 1, 4]
l[1:3] = [2, 3]'''
#appends
'''
l = [2,3]
l.insert(2,4)
print(l)
li = [1, 2, 3, 4]
li.append(5)'''
#extend
'''l = [2,3,4]
l.extend([4, 4])
print(l)'''
#rabotae
'''l = ["Professor Ahmed", "Grace Hopper", "Ada Lovelace"]
while True:
    inp = input("NAME (q to exit):  ")
    if inp == 'q':
        break
    l.append(inp)
    print(l)'''
#delete from list
'''l = [2,3,4,5,6]
del l[0]
print(l)'''
#remove from list
'''l = ["cu", "dinheiro"]
l.remove("dinheiro")
print(l)'''
#pop from list
'''l = [1,2,3,4,5]
l.pop()
print(l)'''
'''l = [1,2,3,4,5]
s = l.pop(0)
print(l)
print(s)'''
#count
'''l = [1,3,3,4,5,2]
print(l.count(3))'''
#copy
'''co = [1,2,3,4,"tandan"]
py = co.copy()
print(py)
'''
#join
'''l = ["ma", "rom", "ba"]
print("I'm " + ", ".join(l[0:2]) + " and " + l[len(l) - 1])'''
#split
'''name = 'Grace,Hopper'
names = name.split(",")
print(names)'''
#reverse
'''name = ["Baiano", "Mané Galinha", "zé pequeno"]
name.reverse()
print(name)'''
#even
'''even_numbers = [i for i in range(1,11) if i % 2 == 0 ]'''
'''l = [1,3,5,4,8,7,6,2]
s = sorted(l)
l.sort()
print(s)
print(l)'''
#class
'''classes = ["ca class", "de class", "oc class"]
for i in classes:
    ina = (i.split(" class"))[0]
    
    classes[classes.index(i)] = ina
classes.sort()
print(classes)'''
'''classes = ["ca class", "de od class", "oc class"]
n = []
for i in classes:
    ina = (i.split(" class"))[0:-1]
    
    n.append("".join(ina))
n.sort()
print(n)'''
'''classes = ["ca class", "de od class", "oc class"]
n = []
for i in classes:
    ina = (i.split(" class"))[0:len(classes) - 1]
    
    n.append("".join(ina))
n.sort()
print(n)'''
#dict files FINALLY
'''s = {"da":"jopa", "ya":["yepal", "tvoio", "mat"]}
print(s["ya"][1])
a = dict(f = "zaminamina", s = " ê ê ", d = " waka waka ")
print(a["f"] + a["s"] + a["d"])
p = {"cu":"é bão", "k9":"é mió", "maconha":"é bão também"}
p["maconha"] = "uma merda"
p["dinheiro"] = "tras isso tudo"
print(sorted(p))
del p["cu"]
print(sorted(p))
d = p.pop("k9")
print(p)
print(d)
print("olha, maconha é " + p["maconha"])
p.clear()
print(p)'''
'''p1 = {'hl':["gaddang", "py", "java"]}
p2 = {'ll':["c", "c++", "assembly"]}
bce = {**p1, **p2}
print(bce)'''
'''p1 = {'hl':["gaddang", "py", "java"]}
p2 = {'ll':["c", "Brainf*ck", "assembly"]}
p1.update(p2)
print(p1)'''
'''d = {'high-level':['java','python', 'c#'], 'low-level':['assembly', 'c', 'c++']}
d.update({"mid-level":"Obj c"})
print(d["high-level"][1], d['low-level'][1],d["mid-level"])
print(d.values())
print(d.keys())
print(d.items())
for k, v in d.items():
    print(f"{k} : {v}")'''
#mine works too
'''c = {'Introduction to Python':[['ms', '9 11'],['af', '1 3']]}
t = False
for i, d in c.items():
    if i == 'Introduction to Python':
        t = True
        if d[0][0] == 'ms':
            print(d[0][1])
if t == False:
    print("No PY")'''
'''c = {'Introduction to Python':[['ms', '9 11'],['af', '1 3']]}
if c.get("Introduction", 'note') == 'note':
    print("nooo")
else:
    for ea in c['unt']
        print(ea[0][1])'''
#char medium
'''l = {"007":[100, 100, 100]
     ,"spider":[33,90,30]
     ,"john wick":[90,90,90]}
asd = {}
for k, n in l.items():
    d = 0
    s= 0
    for i in n:
        d += i
        s += 1
    d /= s
    asd[k] = d
for s, d in asd.items():
    print(f"the average of {s} is {d:.2f}")'''
#Sum of list
'''
d = [1, 2, 3]
print(sum(d))'''
#check name
'''l = {'jacob', 'Grace', 'Anjali', "Haein", "Samantha"}
d = {'Frank', 'Sehr', 'jacob', 'Haein'}
l.add("jacob")
for i in l:
    for da in d:
        if i == da:
            print(i)'''
#sets
'''set_one = {1,2,3,4,5}
set_two = {5, 6, 7, 8}
set_one.Add(6)
set_two.Remove(6)
print(set_one | set_two)
print(set_one - set_two)
print(set_one & set_two)'''
#random
'''import random as b
lorn = [b.randint(0,10) for number in range(0,100)]
print(lorn)'''
#math
'''import math
grade = 99.9
print(math.ceil(grade))'''
#radius
'''import math
are = float(input(" "))
print(round((math.pi * (are * are)* 100)) / 100)'''
#date
'''import datetime
today = datetime.date(2014,7,4)
if today.weekday() == 5 or today.weekday() == 6:
    print("yea")
else:
    print("nah")
print(today.weekday())'''
#requests
'''import requests
import wget
from PIL import Image
import os
p = requests.get("https://randomuser.me/api/").json()
file = wget.download(p['results'][0]['picture']['medium'])
d = Image.open(file)
d.save('ha.jpg')
os.remove(file)'''
#work
'''import requests

r = requests.get('https://randomuser.me/api/').json()
print(r['results'][0]['login']['username'])
print(r['results'][0]['login']['password'])'''
#rabotae
'''import requests
r = requests.get("http://api.open-notify.org/astros.json").json()['people']
for i in r:
    print(i['name'])'''
#PANDAS
'''import pandas as pd
r = pd.read_csv('https://data.cityofnewyork.us/resource/tg4x-b46p.csv')'''
'''print(r.columns)'''
'''print(r.iloc[3,29])'''
'''print(r.head())'''
'''print(r.loc[2,['primary_fur_color', 'x']])'''
'''adf = r["x"][0 : 4]
print(adf)
adf = list(adf.values)
print(adf)'''
'''l = list(r['age'].values)
d = 0
for i in l: 
    if i == 'Adult':
        d += 1
print(d)'''
'''a = 0
for i, d in r.iterrows(): 
    if d['primary_fur_color'] == 'Gray' and d['age'] == 'Adult':
        a += 1
print(a)'''
#pass
'''def da(da):
    if da == True:
        return "cykablyat"
    else:
        pass
print(da(True))'''
# work
'''import random
def columbia_email(f, l, d="columbia.edu"):
    """user inputs strings, 
    Cool email comes out"""
    return f"{f[0]}{l[0]}{str(random.randint(1000,10000))}@{d}"
domain = input("domain zdec (press enter if default):")
fn = input("firstname zdec:")
ln = input("secondname zdec:")
if domain == '':
    print(columbia_email(fn, ln))
else:
    print(columbia_email(fn, ln, domain))'''
'''def dt(y,m,d,h = '00', s="00", me="00"):
    print(f"{y}--{m:0=2}--{d:0=2}:{h:0=2}:{m:0=2}:{s:0=2}")
dt(2024, 7, 9, 11, 0, 22)'''
#GRAPHS WITH MATPLOTLIB
'''import matplotlib.pyplot as mbl'''
'''mine = [0, -5, 0]
fs = [3, 4, 10]
ds = ["2021", "2022", "2023"]'''
'''mbl.scatter(ds, mine)'''
'''mbl.plot(ds, mine,color="red", label="I got")
mbl.plot(ds, fs,color="green", label="F's got")
mbl.title("How many bs f's and I got")
mbl.xlabel("Date")
mbl.xticks(ds)
mbl.ylabel("Bs")
mbl.savefig("Bsfandisgot.jpg")
mbl.legend()
mbl.grid()'''
'''mbl.bar(ds,fs)
mbl.bar(ds,mine)
mbl.show()'''
#Machine Learning
'''from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import pandas as pd 
import math

nba = pd.read_csv('nba_logreg.csv')
nba = nba.dropna()
classific = nba["TARGET_5Yrs"]
data = nba.drop("TARGET_5Yrs", axis=1)
data = data.drop("Name", axis=1)
info = train_test_split(data, classific, test_size = 0.20)
tra_var  = info[0]
#training variables
tra_pred  = info[2]
#training predictions
tes_var  = info[1]
#test variables
tes_pred  = info[3]
#test predictions


#start training
model = LogisticRegression(solver='sag')
model.fit(tra_var,tra_pred)
#predict using model
predictions = model.predict(tes_var)

accuracy = metrics.accuracy_score(tes_pred, predictions)
print(accuracy)'''