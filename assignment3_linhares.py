import matplotlib.pyplot as mbl
import pandas as pd
import reverse_geocode
import matplotlib.ticker as tick
data = pd.read_csv("bfro-report-locations.csv")
counter2 = 0
x = []
y = []
d = 0
a = 0
counter=0
print("----BIGFOOT RESEARCH----")
for index, row in data.iterrows():
    x.append(float(row["latitude"]))
    if float(row["longitude"]) < -180:
        continue
    y.append(float(row["longitude"]))
d = sum(x)/len(x)
a = sum(y)/len(y)
#Get all coordinates and make an average to track down his house
print("----LOADING----")
for index, row in data.iterrows():
    if row["title"].count("rock throw")>0 :
        counter+=1
    if row["title"].count("rock-throw")>0 :
        counter+=1
#Calculate Rock throws in counter variable
for index, row in data.iterrows():
    if row["title"].count("hunters")>0:
        counter2+=1
#Calculate Hunter type encounters in counter2
counter3 = 0
for index, row in data.iterrows():
    if row["title"].count("attack")>0:
        counter3+=1
#Calculate attacks in counter3
counter4 = 0
for index, row in data.iterrows():
    if row["title"].count("death")>0:
        counter4+=1
    if row["title"].count("casualtie")>0:
        counter4+=1
#Calculate Casualties in counter4
counter5 = 0
for index, row in data.iterrows():
    if row["title"].count("red eye")>0:
        counter5+=1
    if row["title"].count("red-eye")>0:
        counter5+=1
#Calculate Casualties in counter5
#Calculate how many encounters per year
years = {}
test = []
byyear = []
for index, row in data.iterrows():
    years[row['timestamp'][0:4]] = 0
for i,s in data.iterrows():
    years[s['timestamp'][0:4]] += 1
for i,s in years.items():
    test.append([i,s])
    byyear.append([i,s])
test.sort(key=lambda x: x[1], reverse=True)
byyear.sort(key=lambda x: int(x[0]))
#Order years by frequency of encounters
Months = {}
testa = []
bymonth = []
for index, row in data.iterrows():
    Months[row['timestamp'][5:7]] = 0
for i,s in data.iterrows():
    Months[s['timestamp'][5:7]] += 1
for i,s in Months.items():
    testa.append([i,s])
    bymonth.append([i,s])
testa.sort(key=lambda x: x[1], reverse=True)
bymonth.sort(key=lambda x: int(x[0]))
#Amount of bigfoots per state
states = {}
tstates = []
bystate = []
for index, row in data.iterrows():
    states[reverse_geocode.get((row["latitude"] , row["longitude"]))['state']] = 0
for i,s in data.iterrows():
    states[reverse_geocode.get((s["latitude"] , s["longitude"]))['state']] += 1
for i,s in states.items():
    tstates.append([i,s])
    bystate.append([i,s])
tstates.sort(key=lambda x: x[1], reverse=True)
bystate.sort(key=lambda x: (x[0]))
#Order months by frequency of encounters
city = {}
tcity = []
bycity = []
for index, row in data.iterrows():
    city[reverse_geocode.get((row["latitude"] , row["longitude"]))['city']] = 0
for i,s in data.iterrows():
    city[reverse_geocode.get((s["latitude"] , s["longitude"]))['city']] += 1
for i,s in city.items():
    tcity.append([i,s])
    bycity.append([i,s])
tcity.sort(key=lambda x: x[1], reverse=True)
bycity.sort(key=lambda x: (x[0]))
#amount per cities
print("----POSSIBLE HOME----")
print(d,',',a)
print("----STATS----")
print(counter,'rocks thrown')
print('spotted by', counter2, "hunters")
print(counter3,"attacks")
print(counter4,"casualties")
print(counter5,"red-eyed")
#Add list of keys and values for each month
d1 = []
d2 = []
for i in bymonth:
    d1.append(i[0])
    d2.append(i[1])
#Create the graphs
mbl.plot(d1,d2)
mbl.title("Encounters by month")
mbl.xlabel("month")
mbl.ylabel("encounters")
mbl.grid()
mbl.show()
#Add list of keys and values for each year
d1 = []
d2 = []
for i in byyear:
    d1.append(i[0])
    d2.append(i[1])
#Create the graphs
fig, ax = mbl.subplots()
mbl.plot(d1,d2)
mbl.title("Encounters by year")
mbl.xlabel("years")
ax.xaxis.set_major_locator(tick.MultipleLocator(25))
mbl.ylabel("encounters")
mbl.grid()
mbl.show()
#Print what we found
print('-----PREFERRED YEARS-----')
print(test[0])
print(test[1])
print(test[2])
print('-----PREFERRED MONTHS-----')
print(testa[0])
print(testa[1])
print(testa[2])
print('-----PREFERRED STATES-----')
print(tstates[0])
print(tstates[1])
print(tstates[2])
print('-----PREFERRED CITIES-----')
print(tcity[0])
print(tcity[1])
print(tcity[2])
print('-----HOW MANY IN TEXAS-----')
print(states['Texas'])
#Query section
print("----Interactive session----")
#need for api
import requests
while True:
    print("query a title and analyze the result, Enter quit to exit")
    inp = input("")
    if inp == 'quit':
        break
    wan = input("wanna know from which state are the first five results (y/n)?    ")
    da = 0  #variable that limits the number of states that you get
    for d, a in data.iterrows(): #Go through each item and check if the search is in the title
        if inp in a['title']:
            print(a["title"])
            if wan == 'y' and da < 5:#if user wants to print state and it is the first state analysed execute
                da += 1 #Limits result to only one result
                req = requests.get(f'https://api.geoapify.com/v1/geocode/reverse?lat={a["latitude"]}&lon={a["longitude"]}&apiKey=5dbe13637b0f485c9217e1996f9fa61e').json()
                #some queries don't have enought data and generate an error
                try:
                    print(req['features'][0]['properties']['city'] + ', ',req['features'][0]['properties']['state'])
                except:
                    try:
                        print(req['features'][0]['properties']['state'])
                    except:
                        print('Error')
