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
indexSum = 0;
for game in games:
    blues=0
    reds=0
    greens=0
    possible = 1;
    for i in range(0,len(game)):
        
        if(game[i].find("blue")!=-1):
            splitted = game[i].split(' ')
            blues = int(splitted[1])
            if blues >14:
                possible = 0
        if(game[i].find("green")!=-1):
            splitted = game[i].split(' ')
            greens = int(splitted[1])
            if greens > 13:
                possible = 0
        if(game[i].find("red")!=-1):
            splitted = game[i].split(' ')
            reds= int(splitted[1])
            if reds > 12:
                possible = 0
    if possible == 1:
        indexSum += a
 

    a+=1
print(indexSum)