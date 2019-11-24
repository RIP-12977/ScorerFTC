"""
Score Calculator for FTC --
  > Handles Exceptions(no format problems)
  > Cannot handle penalties ATM
  > Cannot crosscheck parameters (i.e. program permits users to 
    enter how many stones placed on foundation in auto even when
    0 stones have been delivered across)

"""

# Initialization #
import os 
os.system('clear')
print("FTC Skystone Scorer",end="\n\n")
print("-"*25)

# Variable Declaration #
autoStuff = {}
teleStuff = {}
autoScore = 0
teleScore = 0
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

# Final Output #
print("Final Combined Score: " + str(teleScore + autoScore),end="\n\n\n")
