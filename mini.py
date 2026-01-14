expenseslist = [] # list of expenses in form of dictionary
print(" Welcome to Expenses Tracker : Kharcha Kaam Kiya Karo ")

while True:
    print("\n==== Menu ====")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View Total Expense")
    print("4. Exit")
    
    choice = input("Please Enter Your Choice: ")
    
    # 1. Add Expense
    if choice == "1": # Fixed: Added quotes
        date = input("Kis date par kharcha kiya tha? ")
        category = input("Kis type ka kharcha kiya? (Food, Travel, etc.): ")
        description = input("Aur detail dedo: ")
        
        # Added error handling so letters don't crash the app
        try:
            amount = float(input("Enter the amount: "))
            expense = {
                "date": date,
                "category": category,
                "description": description,
                "amount": amount
            }
            expenseslist.append(expense)
            print("\n✅ Done bro. Expense added successfully!")
        except ValueError:
            print("\n❌ Error: Amount me sirf numbers likho!")

    # 2. View All Expense
    elif choice == "2":
        if len(expenseslist) == 0:
            print("\nNo Expenses Added. Jao pehle kharcha karo.")
        else:
            print("\n===== Ye hai aapka sara expense =====")
            count = 1
            for eachkharcha in expenseslist:
                # Fixed: Changed inner quotes to single quotes
                print(f"Kharcha {count} -> Date: {eachkharcha['date']}, Cat: {eachkharcha['category']}, Details: {eachkharcha['description']}, Amount: ₹{eachkharcha['amount']}")
                count += 1
                
    # 3. View Total Spending
    elif choice == "3":
        total = 0
        for eachkharcha in expenseslist:
            total += eachkharcha["amount"]
        print(f"\n💰 Total Kharcha = ₹{total}")
        
    # 4. Exit
    elif choice == "4":
        print("Dhanyavad aapne hamara system use kiya!")
        break
    
    else:
        print("⚠️ INVALID CHOICE. TRY AGAIN")