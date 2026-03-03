print("----------------------------------------")
print( "GROCERY STORE BILLING & INVENTORY SYSTEM")
print("---------------------------------------")

# -------- ADMIN LOGIN --------
username = "pavan"
password = 1234

attempt = 0

while attempt < 3:
    u = input("Enter Username: ")
    p = int(input("Enter Password: "))

    if u == username and p == password:
        print("Login Successful!\n")
        break
    else:
        print("Invalid Credentials\n")
        attempt += 1

if attempt == 3:
    print("System Locked! Try Again Later.")
    exit()

# -------- PRODUCTS--------

Rice_price = 50
Sugar_price = 40
Oil_price = 120
Milk_price = 30

Rice_stock = 100
Sugar_stock = 80
Oil_stock = 50
Milk_stock = 60

# -------- COUNTERS --------

total_sales = 0
total_items_sold = 0
total_customers = 0

# -------- MAIN MENU LOOP --------

while True:

    print("\n MAIN MENU ")
    print("1. Purchase Items")
    print("2. Check Stock")
    print("3. Add Stock")
    print("4. Sales Report")
    print("5. Close Shop")

    choice = int(input("Enter Choice: "))

    
    # 1. PURCHASE SECTION

    if choice == 1:

        bill = 0

        while True:

            print("\nAvailable Items: Rice, Sugar, Oil, Milk")
            print("Type 'exit' to finish billing")

            item = input("Enter Item Name: ").lower()

            if item == "exit":
                break

            qty = int(input("Enter Quantity: "))

            # -------- CHECK STOCK --------

            if item == "rice":
                if qty <= Rice_stock:
                    amount = qty * Rice_price
                    Rice_stock -= qty
                else:
                    print("Not Enough Rice Stock!")
                    continue

            elif item == "sugar":
                if qty <= Sugar_stock:
                    amount = qty * Sugar_price
                    Sugar_stock -= qty
                else:
                    print("Not Enough Sugar Stock!")
                    continue

            elif item == "oil":
                if qty <= Oil_stock:
                    amount = qty * Oil_price
                    Oil_stock -= qty
                else:
                    print("Not Enough Oil Stock!")
                    continue

            elif item == "milk":
                if qty <= Milk_stock:
                    amount = qty * Milk_price
                    Milk_stock -= qty
                else:
                    print("Not Enough Milk Stock!")
                    continue

            else:
                print("Invalid Item!")
                continue

            bill += amount
            total_items_sold += qty
            print("Item Added Successfully!")

            # -------- LOW STOCK ALERT --------

            if Rice_stock < 10:
                print("Rice stock is low")
            if Sugar_stock < 10:
                print("Sugar stock is low")
            if Oil_stock < 10:
                print("Oil stock is low")
            if Milk_stock < 10:
                print("Milk stock is low")

        # -------- BILL CALCULATION --------

        if bill > 0:

            # -------- DISCOUNT RULES --------
            if bill > 5000:
                discount = bill * 0.15
                print("15% Discount Applied")
            elif bill > 2000:
                discount = bill * 0.10
                print("10% Discount Applied")
            else:
                discount = 0
                print("No Discount")

            bill_after_discount = bill - discount

            # -------- GST 5% --------
            gst = bill_after_discount * 0.05
            final_bill = bill_after_discount + gst

            print("\n------ BILL ------")
            print("Original Total:", bill)
            print("Discount:", discount)
            print("Amount After Discount:", bill_after_discount)
            print("GST (5%):", gst)
            print("Final Amount:", final_bill)

            total_sales += final_bill
            total_customers += 1

        else:
            print("No items purchased.")

    # 2. CHECK STOCK
    elif choice == 2:

        print("\n------ CURRENT STOCK ------")
        print("Rice:", Rice_stock)
        print("Sugar:", Sugar_stock)
        print("Oil:", Oil_stock)
        print("Milk:", Milk_stock)

        if Rice_stock < 10:
            print("Rice stock is low")
        if Sugar_stock < 10:
            print("Sugar stock is low")
        if Oil_stock < 10:
            print("Oil stock is low")
        if Milk_stock < 10:
            print("Milk stock is low")

    # 3. ADD STOCK
    elif choice == 3:

        print("\n1. Rice")
        print("2. Sugar")
        print("3. Oil")
        print("4. Milk")

        add_item = int(input("Select Item: "))
        add_qty = int(input("Enter Quantity to Add: "))

        if add_item == 1:
            Rice_stock += add_qty
        elif add_item == 2:
            Sugar_stock += add_qty
        elif add_item == 3:
            Oil_stock += add_qty
        elif add_item == 4:
            Milk_stock += add_qty
        else:
            print("Invalid Choice")

        print("Stock Updated Successfully!")

    # 4. SALES REPORT
    
    elif choice == 4:

        print("\n------ SALES REPORT ------")
        print("Total Sales Amount: ₹", total_sales)
        print("Total Items Sold:", total_items_sold)
        print("Total Customers Served:", total_customers)

        print("\nRemaining Stock:")
        print("Rice:", Rice_stock)
        print("Sugar:", Sugar_stock)
        print("Oil:", Oil_stock)
        print("Milk:", Milk_stock)

    
    # 5. CLOSE SHOP
    elif choice == 5:

        print("\n DAY CLOSING SUMMARY ")
        print("Total Sales Today: ", total_sales)
        print("Total Items Sold:", total_items_sold)
        print("Total Customers Served:", total_customers)

        print("\nRemaining Stock:")
        print("Rice:", Rice_stock)
        print("Sugar:", Sugar_stock)
        print("Oil:", Oil_stock)
        print("Milk:", Milk_stock)

        print("\nShop Closed Successfully!")
        print("------------------")
        break

    else:
        print("Invalid Choice")