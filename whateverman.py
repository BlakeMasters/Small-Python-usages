
    
# task 3
#need 3 number lists for each pixel which gives rgb. 
#whole list remove /n so lst3.clear("/n")
#remove spaces lst3.split()
#, append to new list each 3?
f = open("ny.txt", "r")
file = open("newimg.txt", "w")
class image:
    #initializing
    def __init__(self,code,x,y,maxi,lst3):
        self.code = code
        self.x = x
        self.y = y
        self.maxi = maxi
        self.lst3 = lst3
    #color inverse, takes the max, in this case it will always be 255 and subtracts the original value
    def Negate(self,lst3):
        for i in lst3:
            i[0]= 255 - int(i[0])
            i[1]= 255 - int(i[1])
            i[2]= 255 - int(i[2])
            #i open and clsoe the file each time to write something, takes longer but has no errors
            file = open("newimg.txt", "a")
            file.write(str(i[0])+ " "+str(i[1])+ " "+str(i[2])+ " ")
            file.close()
    def greyscale(self,lst3):
        for i in lst3:
            #greyscale formula, all 3 rgb values need to be the same, give by the eq
            greys = int(0.3 * i[0] + 0.59 * i[1] + 0.11 * i[2])
            
            i[0]= greys
            i[1]= greys
            i[2]= greys
            file = open("newimg.txt", "a")
            file.write(str(i[0])+ " "+str(i[1])+ " "+str(i[2])+ " ")
            file.close()
            
        
    def removeRBG(self,lst3):
        #checks which value is to be "removed", or simply changed to zero and repeats the same writing process
        a = input("Enter first letter of color to be removed:")
        if a == 'r':
            rmove = 1
        elif a == 'g':
            rmove = 2
        elif a == 'b':
            rmove = 3
        for i in lst3:
            i[rmove] = 0
            file = open("newimg.txt", "a")
            file.write(str(i[0])+ " "+str(i[1])+ " "+str(i[2])+ " ")
            file.close()
           
f1 = f.readline(2)
f2 = f.readline(3)
f3 = f.readline(3)
f4 = f.readline(3)
#rest of this is reading that long string of numbers into a usable format, mine looks like [[12,24,27].ect]
lst3 = f.readlines()
lst3 = ''.join(lst3)
lst3 = lst3.strip()
lst3 = lst3.split(" ")
nlst3 = []
mlst3 = []
for i in lst3:
    nlst3.append(int(i))
    if len(nlst3) ==3:
        mlst3.append(nlst3)
        nlst3 = []
lst3 = mlst3
#class initialization from the original file open and function calling
nyimg = image(f1,f2,f3,f4,lst3)

nyimg.greyscale(lst3)
        
    
    
    
