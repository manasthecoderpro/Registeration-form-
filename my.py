#amount of money of money 

annual = 750 
spar = 350

print("Need Students for Annual Function OR Spardha 2024")

sugg = input("Do you want to take part in Annual Function? ") #sugg = Suggestion

if sugg == "yes":
	name = input("Your Name? ")
	clAss = input("Class :")
	print("Bring Rs." , annual , "by tomorrow")
elif sugg == "no":
	print("Want to take part in Spardha 2024? ")
else:
	print("OK")

if sugg == "yes":
	print("Congratulations, you have taken part in Anuual Function & these are your details:" , "Name:" , name , "," , "Class:" , clAss)
	
sps = input() #sps = Spardha Stundents

if sps == "yes":
	sname = input("Name? ")
	scl = input("Class? ")
	print("Bring Rs." , spar , "by tomorrow")
else:
	print("Ok")



if sps == "yes":
	print("Congratulations, you have taken part in Spardha 2024 & these are your details:" , "Name:" , sname , "," ,  "Class:" , scl)
else:
	print("If you want to participate, restart the program")



