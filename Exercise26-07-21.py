def for_loop():
    print("Send a message several times")
    for numbres in range(3):
        print("Attempt", numbres + 1)


def odd_number():
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
    count = 0
    for i in numbers:
        if(i%2 == 0 and count < 4): 
            count = count + 1
            print(i)
    print(f"We have {count} even numbres")



