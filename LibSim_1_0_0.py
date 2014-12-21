# FileName: LibSim.py
'''Libsim 1.0.0

LibSim program is an agent-based simulation program to study
the occupation of lockers in Peking University library. It is
a python 3 styled code written in object-oriented fashion.

Programmer:
Meng Xiangxi
PhD student, Peking University
mengxiangxibme(>_<)gmail.com

History:
1.0.0 Released 20141213
'''

import random

# Model specifications, constants
hours = 10 # Total openning hours of PKULib
emptyperiod = 30 # Period of evacuation
simdays = 100 # Days to simulate
numlocker = 150 # Set number of lockers
numgoodreader = 900 # Set number of good readers
numbadreader = 100 # Set number of bad readers    

#=====================Classes====================#

class Locker:
    '''The locker in PKULib'''
    empty = True # If the locker is empty
    readerID = 'null' # The reader occupying the locker

    def chkempty(self): # Check if the locker is empty
        return self.empty

    def setempty(self, value): # Change the empty status
        self.empty = value     # value is Boolean

    def getreaderID(self):     # Return the occupyer
        return self.readerID
    
    def setreaderID(self, ID): # Change the occupyer
        self.readerID = ID

    def emptygoodreader(self): # Only good readers leave
        if self.readerID[0] == 'G':
            self.empty = True
            self.readerID = 'null'

class Reader:
    '''Parent class for the readers'''
    numlocker = -1 # The last used locker number

    def chklocker(self, locker): # When entering PKULib, reader look for locker
        for lockernum in range(0,numlocker): # Traverse the lockers
            if locker[lockernum].chkempty(): # If locker is empty
                inchappy()                   # Feel happy
                locker[lockernum].setempty(False) # Occupy it
                self.numlocker = lockernum   # Record the locker number
                return 0                     # Stop looking for lockers
        self.numlocker = -1                  # Cannot find locker

    def getlockernum(self): # Return the number of locker last used
        return self.numlocker

    def leave(self,locker): # Leaving PKULib, release the locker
        if self.numlocker > 0:
            locker[self.numlocker].setreaderID('Null')
            locker[self.numlocker].setempty(True)
            self.numlocker = -1
        
class GoodReader(Reader):
    '''Readers taking their own belongings'''
    def __init__(self): # Inherit the __init__() and parameter of Reader
        Reader.__init__(self)
        numlocker = -1
        self.numlocker = numlocker

    def chklocker(self,locker,ID): # The chklocker() function of child class
        for lockernum in range(0,numlocker):
            if locker[lockernum].chkempty():
                inchappy()
                locker[lockernum].setempty(False)
                self.numlocker = lockernum
                locker[lockernum].setreaderID('G'+str(ID)) # G for 'GoodReader'
                return 0
        self.numlocker = -1
        incmad()

class BadReader(Reader):
    '''Readers leaving their own belongings'''
    def __init__(self): # Inherit the __init__() and parameter of Reader
        Reader.__init__(self)
        numlocker = -1  # Don't know why have to write this... But bugs if not
        self.numlocker = numlocker
        
    def chklocker(self,locker,ID): # The chklocker() function of child class
        for lockernum in range(0,numlocker):
            if locker[lockernum].chkempty():
                inchappy()
                locker[lockernum].setempty(False)
                self.numlocker = lockernum
                locker[lockernum].setreaderID('B'+str(ID)) # B for 'BadReader'
                return 0
        self.numlocker = -1
        incmad()

#====================Paramters===================#

# Total number of readers
numtotreader = numgoodreader + numbadreader

# Hourly entrance number
hrnumreader = (numgoodreader+numbadreader)//hours
hrnumreaderres = (numgoodreader+numbadreader)%hours

# Initialize the parameters
locker = [Locker() for _ in range(numlocker)]
goodreader = [GoodReader() for _ in range(numgoodreader)]
badreader = [BadReader() for _ in range(numbadreader)]

# Target variable
happiness = 0
madness = 0

def inchappy():
    '''Access and alter the variable 'happiness'.'''
    global happiness
    happiness += 1

def incmad():
    '''Access and alter the variable 'madness'.'''
    global madness
    madness += 1

#=====================Function===================#

def readerenter(namelistpara, numreaderenterpara):
    '''A certain reader enters.'''
    numreaderenter = namelistpara[numreaderenterpara]
    # Convert to the subscript of the reader
    if numreaderenter < 0:
        goodreader[-numreaderenter-1].chklocker(locker,-numreaderenter-1)
        # Convert the negative values to the subscript of goodreader
    else:
        badreader[numreaderenter].chklocker(locker, numreaderenter)

#=======================Main=====================#

for day in range(0,simdays): # Simulate for each day
    if day%emptyperiod == 0: # Empty the lockers periodically
        for i in badreader:  # Propell badreaders
            i.leave(locker)
    namelist = []            # Initialze namelist container
### Here, namelist combines goodreader and badreader. Negative values are
### for goodreader and vice versa. The subscript of goodreader is obtained by
### convertion: -numnamelist - 1.
    for numnamelist in range(-numgoodreader, numbadreader):
    # Construct original namelist
        namelist.append(numnamelist)
    random.shuffle(namelist) # Shuffle(): change the order of element randomly
    for varhour in range(0, hours-1):  # Simulate hour by hour
        for numreaderenterori in range(varhour*hrnumreader, (varhour+1)*hrnumreader):
        # Every hour except the last, an equal number of readers enter
            readerenter(namelist, numreaderenterori)
        for goodreaderleave in goodreader: # goodreader leave after one hour
            goodreaderleave.leave(locker)
    varhour = hours - 1 # The last opening hour
    for numreaderenterori in range(varhour*hrnumreader, numtotreader):
    # In the last hour, all unentered readers enters
        readerenter(namelist, numreaderenterori)
    for goodreaderleave in goodreader: # All goodreader leave
            goodreaderleave.leave(locker)

#======================Output====================#

print('happiness:', happiness)
print('madness:', madness)
