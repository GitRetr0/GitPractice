name=input("What's yuor name?")
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