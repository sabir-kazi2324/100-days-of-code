while True:
    year = int(input("Enter year : "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("leap year")
            else:
                print("normal year")
        else:
            print("leap year")
    else:
        print("4 normal year")
