name=input("What's yuor name?")
Phrase="Hello"
Greeting=Phrase+","+" "+name
print(Greeting)
question=input("How are you doing?\n")
reply="Now I see you're "+question
print(reply)
order=input("Would you like tea or coffee?\n")
#added restaurant dialog
order=input("Would you like coffee or tea?\n")
if order == "coffee" or order=="Coffee":
    print("Coffee with milk?")
elif order == "tea" or order=="Tea":
    print("Tea with milk?")
extended_order=input(" ")
if extended_order =="yes":
    print("Here is your " +order+" with milk")
elif extended_order =="no":
    print("Would you like to add sugar instead?")
more_extended_order=input(" ")
if more_extended_order == "yes":
    print("Here we go, your " +order+ " with sugar!")
elif more_extended_order == "no":
    print("Then go fuck a brain to someone else!")