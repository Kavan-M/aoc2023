import itertools

file = open('personal.txt','r')
lines = file.readlines()

games = []
games1=[]
for line in lines:
    
    entries = line.split(',')
    lost = []
    blost = []
    for entry in entries:
        lost+=entry.split(';')
    for l in lost:
        blost+=l.split(':')
        games.append(blost)

games = list(games for games,_ in itertools.groupby(games))



#print(games)
a=1
powerSum = 0;
for game in games:
    hblues=0
    hreds=0
    hgreens=0
    for i in range(0,len(game)):
        
        if(game[i].find("blue")!=-1):
            splitted = game[i].split(' ')
            blues = int(splitted[1])
            if blues > hblues:
                hblues = blues
        if(game[i].find("green")!=-1):
            splitted = game[i].split(' ')
            greens = int(splitted[1])
            if greens > hgreens:
                hgreens = greens
        if(game[i].find("red")!=-1):
            splitted = game[i].split(' ')
            reds= int(splitted[1])
            if reds > hreds:
                hreds = reds

        power = hreds * hgreens * hblues
    print(hreds,hgreens,hblues)
    print(a,power)
    powerSum +=power
 

    a+=1
print(powerSum)