#SET animal = INPUT "What animal are you ?"
# If animal is "chicken"
#    THEN PRINT "This is my favourite animal"
#END

animal = input("What animal are you? ").lower()
if animal == "tiger":
    print("this is my favourite animal")
elif animal == "kitten":
    print("i love kittens!")
else:
    print("this is not my favourite animal")
