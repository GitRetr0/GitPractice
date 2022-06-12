name=input("What's yuor name?\n")
Phrase="Hello"
Greeting=Phrase+","+" "+name
print(Greeting)
question=input("How are you doing?\n")
reply="Now I see you're "+question
print(reply)
#this is just a comment to be commited
#some social interaction below
order=input("Would you like to buy your wife some flowers or chocolate?\n")
if order=="flowers" or order == "Flowers":
    print("Roses or tulips?")
elif order=="Chocolate" or "chocolate":
    print("Milk chocolate or dark?")
choice=input("")
    #now adding an end of purchase
if choice == "roses"or "Roses":
    print("Here is your flowers!")
else:
     print("Maybe sweets then?")
neworder=input("")
if neworder == "yes":
    print("Milk chocolate or dark?")
else:
    print("Goodbye then")
#please, this code has to be updated because it doesn't work as planned