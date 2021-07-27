
#for view the funcion change the state of the variable successful 
def for_else():
    successful = False
    for number in range(1, 6, 2):
        print("Attempt", number)
        if(successful):
            print(successful)
            break
    else:
        print("Attemted 3 times and failed")


#Iterable
def iterable():
    for letter in "Python is a lenguaje programing":
        print(letter)

    for number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print(number)

    shopping_cart = ["Apple", "pineapple", "wather melon", "shaver", "bread", "ham"]
    for item in shopping_cart:
        print(item)