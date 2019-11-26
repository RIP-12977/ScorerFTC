"""
Score Calculator for FTC --
  > Handles Exceptions(no format problems)
  > Cannot crosscheck parameters (i.e. program permits users to 
    enter how many stones placed on foundation in auto even when
    0 stones have been delivered across)
  > Saves entered scores into text file 

"""

import datetime as dt 

# Initialization #
import os 
os.system('clear')
print("FTC Skystone Scorer",end="\n\n")
print("Input numbers/strings as requested")
print("Enter 'exit' whenever to stop calculating score",end="\n\n")
print("-"*25)

# Variable Declaration #
autoStuff = {}
teleStuff = {}
autoScore = 0
teleScore = 0
penaltyScore = 0
exit = False

# Fill Methods / Input Validator #
def fillAuto(*args):
  autoStuff["Moved Foundation?"] = 10
  autoStuff["Moved x Skystone?"] = 10
  autoStuff["Moved x Stones?"] = 2
  autoStuff["Moved x Extra Stones?"] = 2
  autoStuff["Parked?"] = 5
  autoStuff["x Stones in Foundation?"] = 4
def fillTele(*args):
  teleStuff["Moved Foundation?"] = 15
  teleStuff["x Robots Parked?"] = 5
  teleStuff["x Capstones Capped?"] = 5
  teleStuff["x Stones Placed?"] = 1
  teleStuff["x Stones Delivered?"] = 1
  teleStuff["x Levels in Skyscraper?"] = 2
def inputValid(*args):
  global exit 
  
  #if input is y/n
  if 'exit' in args[0].lower():
    exit = True 
    return
  elif len(args) == 1:
    return 
  
  #if input is a number 
  if args[1] =='n' and not args[0].isdigit():
    num2 = ""
    while not num2.isdigit():
      num2 = input("Enter x number: ")
    return int(num2)
  return int(args[0])
def writeFile(string):
  try:
    f1 = open('scoreHistory.txt','a+')
  except:
    f1 = open('scoreHistory.txt',"w+")
    print("Score History File Created!")
  time = dt.datetime.now()
  min = str(time.minute).zfill(2)
  out = "{}-{}-{} @ {}:{} --> ".format(time.year,time.month,time.day,time.hour,min)
  out += 'Auto: {} , TeleOp: {} , Penalty: {} --> Total Score: {}'
  f1.write(out.format(autoScore,teleScore,penaltyScore,string) + "\n")


'''

main program 

'''

fillAuto() 
fillTele() 

# auto loop # 
print("Calculating Auto Points:",end="\n\n")
for x in autoStuff:
  if "x" in x:
    print(x)
    num = input("Enter x number: ")
    num = inputValid(num,'n')
    if exit: 
      break 
    autoScore += int(autoStuff[x]) * num 
    print()
  else:
    print(x,end=" ")
    inu = input("[y/n] ")
    inputValid(inu)
    if exit: 
      break 
    if 'y' in inu.lower():
      autoScore += int(autoStuff[x])
    print()
print("\nFinal Auto Score: " + str(autoScore),end="\n\n")
print("-"*25)
exit = False 

# teleOp loop # 
print("Calculating TeleOp Points:",end="\n\n")
for x in teleStuff:
  if "x" in x:
    print(x)
    num = input("Enter x number: ")
    num = inputValid(num,'n')
    if exit: 
      break 
    teleScore += int(teleStuff[x]) * num 
    print()
  else:
    print(x,end=" ")
    inu = input("[y/n] ")
    inputValid(inu)
    if exit: 
      break 
    if 'y' in inu.lower():
      teleScore += int(teleStuff[x])
    print()
print("\nFinal TeleOp Score: " + str(teleScore),end="\n\n")
print("-"*25)

# Penalty Loop #
userIn = input("Were there any penalties against the other alliance? [y/n] ")
if('y' in userIn.lower()):
  penaltyScore = int(input("How many? "))
print("\nFinal Penalty Added: " + str(penaltyScore),end="\n\n")
print("-"*25)

# Final Output #
finalScore = str(teleScore + autoScore + penaltyScore)
print("Final Combined Score: " + finalScore,end="\n\n\n")
writeFile(finalScore)
