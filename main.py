name="Vaishnavi"
print(name)
age= 13
print(age)
# I use str() to convert an integer into a string
print(name + str(age))
#Printing Arrays
colors=["black", "blue", "purple", "pink"]
print(colors)
#Print one value from the array list
print (colors[2])
#Print total length of the array
print(len(colors))
# Getting Input from the user
fav_Destination= input("Enter your favourite destination: ")
print(fav_Destination)
# Understanding use of IF-ELSE
age=int(input("Enter your Age: "))
if(age>10 and age <13):
    print("you are still a kid")
elif(age >=13 and age <=19):
    print("You are a teenager")  
else:
    print("you are an adult") 

# Understand for Loop
for i in range(1,10):
    print(i)
for i in colors:
     print(i)   

 # Use of While Loop
count=9
while(count>=0):
    print(count)
    count=count-1   