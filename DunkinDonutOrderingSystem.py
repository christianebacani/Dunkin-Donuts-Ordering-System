def menu():
    totalPrice = 0
    while True:
        print("\tMENU")
        print("1.) Donuts")
        print("2.) Beverages")
        print("3.) Combos & Shareables")
        print("4.) Bundles")
        print("5.) Savory and Bakery")
        print("6.) Grab-And-Go")
        print("7.) Breakfast")

        choice = int(input("Enter your choice here : "))
        price = 0
        if choice == 1:
            print("\nDONUTS\t\t\t\tPRICE")
            print("1.) Bavarian Filled\t\tP 12")
            print("2.) Sugar Raised\t\tP 12")
            print("3.) Boston Kreme\t\tP 12")
            print("4.) Strawberry Filled\t\tP 12")
            print("5.) Blueberry Cheese\t\tP 15")
            print("6.) Choco BTN\t\t\tP 15")
            print("7.) Choco Kreme Filled\t\tP 15")
            print("8.) Strawberry Kreme Filled\tP 15")
            print("9.) Glazed\t\t\tP 8")
            print("10.) Cheese Trickles\t\tP 8")
            print("11.) Sugar Raised\t\tP 8")
            print("12.) Choco Wacko\t\tP 12")
            print("13.) Choco Bang\t\t\tP 30")
            print("14.) Dunkin` Yan\t\tP 15")

            orderDonuts = int(input("Enter your order here : "))

            if orderDonuts == 1:
                price += 12

            elif orderDonuts == 2:
                price += 12

            elif orderDonuts == 3:
                price += 12

            elif orderDonuts == 4:
                price += 12

            elif orderDonuts == 5:
                price += 15

            elif orderDonuts == 6:
                price += 15

            elif orderDonuts == 7:
                price += 15

            elif orderDonuts == 8:
                price += 15

            elif orderDonuts == 9:
                price += 8

            elif orderDonuts == 10:
                price += 8

            elif orderDonuts == 11:
                price += 8
            
            elif orderDonuts == 12:
                price += 12

            elif orderDonuts == 13:
                price += 30

            elif orderDonuts == 14:
                price += 15

            else:
                print("Invalid Order!")
                continue
            pass
        
        elif choice == 2:
            print("\nBEVERAGES\t\t\tPRICE")
            print("1.)Hot Choco\t\t\tP 15")
            print("2.) Brewed Coffee\t\tP 15")
            print("3.) Cafe Americano\t\tP 15")
            print("4.) Iced Coffee\t\t\tP 15")
            print("5.) Mango Fruit Tea\t\tP 20")
            print("6.) Chocolate Pearl Drink\tP 40")
            print("7.) Mango Pearl Drink\t\tP 40")

            orderBeverages = int(input("Enter your order here : "))

            if orderBeverages == 1:
                price += 15

            elif orderBeverages == 2:
                price += 15

            elif orderBeverages == 3:
                price += 15

            elif orderBeverages == 4:
                price += 15

            elif orderBeverages == 5:
                price += 20

            elif orderBeverages == 6:
                price += 40

            elif orderBeverages == 7:
                price += 40

            else:
                print("Invalid Order!")
                continue
            pass

        elif choice == 3:
            print("\nCOMBOS & SHAREABLES\t\tPRICE")
            print("1.) Justin`s Cravings\t\tP 40")
            print("2.) Ken`s Choice     \t\tP 40")
            print("3.) Josh`s Fave      \t\tP 40")
            print("4.) Stell`s Selection\t\tP 40")
            print("5.) Pablo`s Pick     \t\tP 40")
            print("6.) Shareables 1     \t\tP 150")
            print("7.) Shareables 2     \t\tP 150")
            
            orderShareables = int(input("Enter your order here : "))

            if orderShareables == 1:
                price += 40
            
            elif orderShareables == 2:
                price += 40

            elif orderShareables == 3:
                price += 40

            elif orderShareables == 4:
                price += 40

            elif orderShareables == 5:
                price += 40

            elif orderShareables == 6:
                price += 150

            elif orderShareables == 7:
                price += 150

            else:
                print("Invalid Order!")
                continue
            pass

        elif choice == 4:
            print("\nBUNDLES\t\t\t\tPRICE")
            print("1.) Little Bunch\t\tP 200")
            print("2.) Awesome Bundle\t\tP 250")
            print("3.) Munchkins Bucket\t\tP 150")

            orderBundles = int(input("Enter your order here "))

            if orderBundles == 1:
                price += 200

            elif orderBundles == 2:
                price += 250

            elif orderBundles == 3:
                price += 150

            else:
                print("Invalid Order!")
                continue
            pass

        elif choice == 5:
            print("\nSAVORY AND BAKERY\t\tPRICE")
            print("1.) Cheese Bunwich\t\tP 25")
            print("2.) Bacon Cheesy Mushroom\tP 30")
            print("3.) Tuna\t\t\tP 25")
            print("4.) Spanish Sausage\t\tP 30")
            print("5.) Cheese Croissant\t\tP 30")
            print("6.) Cheesy Tuna\t\t\tP 25")
            print("7.) Egg and Cheese\t\tP 30")

            orderPastries = int(input("Enter your order here : "))

            if orderPastries == 1:
                price += 25
            
            elif orderPastries == 2:
                price += 30

            elif orderPastries == 3:
                price += 25

            elif orderPastries == 4:
                price += 30

            elif orderPastries == 5:
                price += 30

            elif orderPastries == 6:
                price += 25

            elif orderPastries == 7:
                price += 30

            else:
                print("Invalid Order!")
                continue
            pass

        elif choice == 6:
            print("\nGRAB-AND-GO\t\tPRICE")
            print("1.) D` Coffee Box\tP 150")

            orderGrabAndGo = int(input("Enter your order here : "))

            if orderGrabAndGo == 1:
                price += 150
            
            else:
                print("Invalid Order!")
                continue
            pass

        elif choice == 7:
            print("\nBREAKFAST\t\tPRICE")
            print("1.) Waffle\t\tP 40")

            orderBreakfast = int(input("Enter your order here : "))
            
            if orderBreakfast == 1:
                price += 40
            
            else:
                print("Invalid Order!")
                continue
            pass

        else:
            print("Invalid choice! Please choose a valid option.")
            continue

        quantity = int(input("Enter quantity here : "))
        totalPrice += price * quantity
        orderAgain = input("Do you want to order again (y/n)?: ").lower()

        if orderAgain != "y":
            print("Total Price : P", totalPrice)
            userMoney = int(input("Enter your money here : P "))
            if userMoney < totalPrice:
                print("Insufficient Money!")
                continue
            else:
                change = userMoney - totalPrice
                print("Change : P", change)
                print("THANK YOU FOR ORDERING, PLEASE COME AGAIN!")
                break

        else:
            continue

def aboutUs():
    print("\nDunkin` brings indulgence to everybody`s day with signature\n\t\tdonuts, coffee, baked goods, and more.")

def userChoose():
    while True:
        print("Welcome to Dunkin Donuts!")
        input("Press enter to start : ")

        print("\n1) Menu")
        print("2.) About us")
        print("3.) Exit")

        choose = int(input("Enter your choice here : "))

        if choose == 1:
            menu()

        elif choose == 2:
            aboutUs()
            break

        elif choose == 3:
            print("\nTHANK YOU FOR VISITING OUR PAGE!")
            exit()
        else:
            print("Invalid Choice!")
            continue

userChoose()
