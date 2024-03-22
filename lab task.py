# print('"I\'m"','""learnig""','\"\"\"Python\"\"\"', sep='\n')


year = 1582
num = int(input("enter your year: "))
if (num % 4 !=0):
          print("common year")
elif (num % 100 !=0):
          print("leap year")
elif (num % 400 !=0):
          print("common year")
else:
          print("leap year")
         
if num < year:
    print("Not within the Gergorian calender Period")


#def l100kmtompg(liters):
#    miles = 1000 / 1609.344 
#    gallons = liters / 3.785411784 
#    return miles / gallons

#def mpgtol100km(miles):
#    kilometers = 1609.344 / 1000 
#    liters = 3.785411784 
#    return (liters * 100) / (miles * kilometers)

#print(l100kmtompg(3.9))
#print(l100kmtompg(7.5))
#print(l100kmtompg(10.))
#print(mpgtol100km(60.3))
#print(mpgtol100km(31.4))
#print(mpgtol100km(23.5))
