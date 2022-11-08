import random
x=random.randint(1,100)
count=0
def match_num():
    try:
        y=int(input("Enter a number in (1-100)range: "))
        global count
        if x == y:
            count+=1
            print("Yahooo... You guessed it correctly\nYou took ",count,"chances to guess it\n:)")
        elif x < y:
            print("too high. choose lower number")
            count+=1
            match_num()
        elif x > y:
            print("too low. choose higher number")
            count+=1
            match_num()
    except:
        print("Oops..  Invalid answer")
        match_num()
match_num()