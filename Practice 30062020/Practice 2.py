one_maoshanwang = 20.0

numwilling = int(input("How many you want?\n"))
amtwilling = float(input("How much money do you have at hand?\n"))
newnum = int(amtwilling // one_maoshanwang)

if amtwilling >= (one_maoshanwang * numwilling):
    print("Great! Here you go!")

elif (amtwilling >= (one_maoshanwang * newnum)) and (newnum > 0):
    print("I can give you ", newnum, " instead")
else:
    print("qu jia sai la!")

