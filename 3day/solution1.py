file = open('personal.txt','r')
lines = file.readlines()
filelength = len(lines)

text = []
linelength = 0
for line in lines:
    text.append(line)
    linelength = len(line)
numsum=0
for i in range(0,filelength):
    line = text[i]
    j=0
    while j < len(line):
        dummy = 1
        number = ""
        initial = j
        if(line[j].isdigit()):
            number+=line[j]
            numindices = []
            numindices.append(j)
            while line[j+dummy].isdigit():
                number+=line[j+dummy]
                numindices.append(j+dummy)
                dummy+=1
        #check whether or not number is a part of the sum
        #generate surrounding indices
        true=0
        if number!="":
            if i-1 >= 0:
                for char in range(0,dummy+2):
                    if text[i-1][char+j-1].rstrip().isdigit() == False and text[i-1][char+j-1].rstrip() != "." and 0<char+j-1 <linelength:
                        true=1

            if i+1 <= filelength-1:
                for char in range(0,dummy+2):
                    if text[i+1][char+j-1].rstrip().isdigit() == False and text[i+1][char+j-1].rstrip() != "." and 0<char+j-1 <linelength:
                        true=1

            if j-1 != -1:
                if text[i][j-1].rstrip().isdigit() == False and text[i][j-1].rstrip() != ".":
                    true = 1
                    
                    
            if j+ dummy <= linelength-1:
                if text[i][j+dummy].rstrip().isdigit() == False and text[i][j+dummy].rstrip()!=".":
                    true=1
                    
            
                            
        
            if true==1 and number!= "":
                numsum+=int(number)
                
        j+=dummy-1
        j+=1
print(numsum)
       
            