def for_loop():
    print("Send a message several times")
    for numbres in range(3):
        print("Attempt", numbres + 1)


def odd_number():
    count = 0
    for number in range(1,10,2):
        if(count < 4): 
            count = count + 1
            print(number)
    print(f"We have {count} even numbres")



odd_number()