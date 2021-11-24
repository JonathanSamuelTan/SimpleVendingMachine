#global variable
drinks = ["COCA COLA","FANTA","SPRITE","POCARI SWEAT","AQUA"]
quantities = [10,10,10,10,10]
price = [8000,7500,7000,9000,5000] #in IDR


def CheckStock():
    l= len(drinks)
    print("Today we have :")
    for x in range(l):
        format_drinks = f"{drinks[x]:<15}"
        format_price  = f"RP.{price[x]:,}"
        format_qtc    = f"{quantities[x]:>3} bottles available"
        print(x+1,".",format_drinks,"\t : @",format_price," => ",format_qtc)

def buy():
    orders =[]
    order_qtc=[]
    order_price=[]
    cont = True
    x=0
    while(cont):
        CheckStock()
        print("Input your order number (number only): ")
        order = int(input("=> "))
        n = order-1
        product = orders.insert(x,drinks[n])
        print("How Much ? (number only) :")
        qtc = int(input("=> "))
        if(quantities[n]< 1):
            print("Sorry our stock is not enough for your order")
            product = drinks[n]
            orders.remove(product)
        else:
            order_price.insert(x,price[n])
            quantities[n]-=qtc
        order_qtc.insert(x,qtc)

        print("Any thing else?(yes/no):")
        YN = input("=> ")
        if(YN.casefold() == "yes"):
            cont = True
            x+=1
        elif(YN.casefold() == "no"):
            print("Your Orders: ")
            l = len(orders)
            total = 0

            for j in range(l):
                format_drinks = f"{orders[j]:<15}"
                format_price  = f"RP.{order_price[j]:,}"
                format_qtc    = f"x {order_qtc[j]:>3}"
                format_result = f"= Rp{order_price[j]*order_qtc[j]:,}"
                print("||",j+1,".",format_drinks,"\t",format_price,format_qtc,format_result,"||")
                total += order_price[j]*order_qtc[j]
                format_total = f"TOTAL = Rp.{total:,}"
            print(format_total)
            break
        else:
            print("your input isn't valid , restart your order")
            buy()

def restock():
    print("1. Add new products")
    print("2. Restock existing products")
    choose = int(input("=> "))
    if(choose == 1):
        l = len(drinks)
        while(True):
            name = input("Input Product's Name : ")
            drinks.insert(l,name)
            Idr = int(input("Input Product's Price (IDR) :"))
            price.insert(l,Idr)
            qtc = int(input("Input Product's Quantity (number only):"))
            quantities.insert(l,qtc)
            CheckStock()
            cont = input("Do you want add product again ?(yes or no) :")
            if(cont.casefold()=="yes"):
                l+=1
                continue
            elif(cont.casefold()=="no"):
                print("=====THANKYOU=====")
                break

    elif(choose == 2):
        cont = True
        while(cont):
            CheckStock()
            print("Product number you want to restock :")
            n = int(input("=> "))
            print("How much ? (number only): ")
            qtc = int(input("(bottles => "))
            quantities[n-1] +=qtc
            print("Processing.....")
            print("Done.....")
            CheckStock()
            x = input("restock again ? (yes or no) => ")
            if(x.casefold() == "yes"):
                continue
            elif(x.casefold()):
                print("======THANKYOU=====")
                break

    