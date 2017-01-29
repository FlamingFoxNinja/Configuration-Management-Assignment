# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
def Ninety_Nine_Bottles_of_Beer():
    b = 99
    while (b > 0):
        if b == 1:
            print str(b) + " bottles of beer on the wall, " + str(b) + " bottles of beer"
            print "take one down, pass it around, no more bottles of beer on the wall"
        else:
            print str(b) + " bottles of beer on the wall, " + str(b) + " bottles of beer"
            print "take one down, pass it around," +  str(b-1) + " bottles of beer on the wall"
        b = b - 1
        
Ninety_Nine_Bottles_of_Beer()
    
