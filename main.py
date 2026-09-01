while True:
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View All Records")
    print("4. Monthly Summary")
    print("5. Category-wise Summary")
    print("6. Exit")

    choise = input("Enter Your Choise: ")


    if choise == "1":
            try:
                addIncome = int(input("Add Your Income: "))
            except ValueError:
                print("Pleace add digit")
                continue
            try:
                addSourse = str(input("Add Income Sorce: "))
            except ValueError:
                print("Pleace add word")
                continue
            try:
                addDate = input("Enter Date(YYYY-MM-DD): ")
            except ValueError:
                print("Pleace Enter Digit")
                continue
            with open("expenses.txt","a") as file:
                file.write("INCOME"+","+f"{addDate},{addSourse},{addIncome}\n")
                print("Add Income successfully")
        

    elif choise == "2":
            try:
                amount = int(input("Enter Your Amount: "))
            except ValueError:
                print("Pleace enter digit")
                continue
            try:
                catagory = str(input("Enter Catagory(Food, Travel, Rent, Shopping, Other): ")).lower()
            except ValueError:
                print("Pleace Enter Word")
                continue
            if catagory == "food"or catagory == "travel"or catagory == "rent"or catagory == "shopping"or catagory == "other":
                try:
                    note = str(input("Enter Note: "))
                    AmountDate = input("Enter Date(YYYY-MM-DD): ")
                except ValueError:
                    print("Pleace Enter Word")
                    continue
                with open("expenses.txt","a") as file:
                    file.write("EXPENSES"+","+f"{AmountDate},{catagory},{amount},{note}\n")
                    print("Add Expense Successfully")
            else:
                print("Pleace Enter Food, Travel, Rent, Shopping, Other This Catagory.")
    

    elif choise == "3":
        with open("expenses.txt","r")as file:
            for line in file:
                parts = line.strip().split(",")
                if parts[0] == "EXPENSES" :
                            print("Type: "+typee+"  Date: "+date+"  Catagory: "+catagory+"  Amount: "+amount+"  Note: "+note)
                elif parts[0] == "INCOME":
                            print("Type: "+typee+"  Date: "+date+"  Sourse: "+Sourse+"  Amount: "+amount)

    elif choise == "4":
        with open("expenses.txt","r")as file:
            for line in file:
                expenses,AmountDate,catagory,amount,note = line.strip().split(",")
        
