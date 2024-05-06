#_______________________________________________________________________
#Charles Crittenden
#Alarm Program
#Current Time
time = int(input('What time is it now?\n'))
#Alarm Time
alarm = int(input('How many hours until your alarm go off?\n'))
#Get number left over the hours 
nohours =int(alarm/24)
#Get number hours to substract
hourstosub = int(24 * nohours)
#subtract the number of hours from alarm
lefthours = int(alarm - hourstosub)
#Get final Time
finaltime = int(lefthours + time)
#print ('no hours :',nohours )
#print ('left over hours :', lefthours )
if finaltime >= 24:
    finaltime = int(finaltime - 24)
    print ('The alarm will go off at :', finaltime)
else:
    print (f'The alarm will go off in {nohours:.0f} days at', finaltime)
    

name = input('done\n' )


