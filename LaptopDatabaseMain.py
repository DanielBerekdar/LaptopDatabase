import pandas as pd

from Laptop import Laptop


# Functions to print ascii laptop art, found the art on https://ascii.co.uk/art/laptop

def PrintLaptopExitArt():
    with open("LaptopExitArt.txt", 'r') as File:
        read = File.read()
        print(read)
    File.close()


def PrintLaptopIntroArt():
    with open("LaptopIntroArt.txt", 'r') as File:
        read = File.read()
        print(read)
    File.close()


# Main Class
class LaptopDatabaseMain():
    #Retrieving the dataframes from the file into system memory

    Laptop_DataFrame = pd.read_excel("Database.xlsx", index_col=0)
    Sold_Items = pd.read_excel("SoldItems.xlsx", index_col=0)

    # Method to check if a price is valid for entry to the database.
    def isValidNumber(price):
        try:
            float(price)
            return True
        except ValueError:
            print("Please use whole numbers or decimals only.")

    def isValidCondition(condition):
        if condition == 'good' or condition == 'ok' or condition == 'bad':
            return True
        else:
            print("Invalid condition. Please use 'good', 'bad', or 'ok' as conditions.")
            return False

    def isValidYear(year):
        if year < 1980 or year > 2020:
            print("Please choose a date between 1980 and 2020.")
            return False
        if 1980 <= year <= 2020 and (year):
            return True

    # Welcome Screen
    print()
    PrintLaptopIntroArt()
    print("Welcome to Laptop Database, your inventory management system and analytics for Laptop Computers!")

    # User Queries
    query = ""
    while query != 'quit':
        print("MAIN MENU")
        query = input("Would you like to 'buy', 'view', 'sell', or 'quit'? ").lower()
        # Selling a Laptop
        if query == 'sell':
            if Laptop_DataFrame.empty:
                print("The database is empty. Please buy more laptops. Taking you back to the main menu.")
            else:
                print("Here are the serial values of laptops in the database: ")
                print(Laptop_DataFrame[['Manufacturer', 'Model', 'Serial']])
                validSerial = False
                while validSerial is False:
                    Serial = input("What is the serial number of the laptop you want to sell?")
                    if isValidNumber(Serial):
                        Serial = int(Serial)
                        validSerial = True
                        # Ensuring the sold laptop is removed and appended to the 'solditems' DataFrame
                        try:
                            Sold_Item = Laptop_DataFrame[Laptop_DataFrame.Serial == Serial]
                            Sold_Items = Sold_Items.append(Sold_Item, ignore_index=True)
                            Laptop_DataFrame = Laptop_DataFrame[Laptop_DataFrame.Serial != Serial]
                            print("Transaction complete.")

                            Sold_Item_Values = Sold_Item.values
                            Earned_Profit = Sold_Item_Values[0, 4] - Sold_Item_Values[0, 3]
                            print("Profit Earned: $" + str(Earned_Profit))
                            with open("transaction.txt", "a") as file:
                                file.write(str(Earned_Profit) + "\n")
                            #Writing to file and then re-retrieving it to have the most up to date information in system memory.
                            Laptop_DataFrame = Laptop_DataFrame.to_excel("Database.xlsx")
                            Sold_Items = Sold_Items.to_excel("SoldItems.xlsx")
                            Laptop_DataFrame = pd.read_excel("Database.xlsx", index_col=0)
                            Sold_Items = pd.read_excel("SoldItems.xlsx", index_col=0)
                        # Catching missing serials
                        except(IndexError):
                            print("Error finding that serial number in the database")

                        except(AttributeError):
                            print(AttributeError)
                            print("Error finding that serial  in the database")
                    else:
                        print("Invalid serial number. please use only numbers.")
                        validSerial = False
        # How to view information about the laptop database.
        if query == 'view':
            viewQueryQuit = False
            # While loop so it wont kick you out when you search for multiple things.
            while viewQueryQuit == False:
                print("VIEW MENU")
                viewQuery = input(
                    "What would you like to view? enter 'help' for a command list, 'quit' to return to main menu. : ").lower()
                # SELECT * FROM DataBase
                if viewQuery == 'everything':
                    print("NOT SOLD:")
                    print(Laptop_DataFrame)
                    print("SOLD:")
                    print(Sold_Items)
                # Selecting purchase price (but capturing  other information to make the price meaningful)
                if viewQuery == 'purchase_price':
                    print(Laptop_DataFrame[['Manufacturer', 'Model', 'Purchase_Price']])
                # To find a Purchase price less than the given X
                if viewQuery == 'purchase_price_under_x':
                    x = input("Enter a value for X: ")
                    if isValidNumber(x) is True:
                        x = int(x)
                        print(Laptop_DataFrame.loc[
                                  Laptop_DataFrame['Purchase_Price'] < x, ['Manufacturer', 'Model', 'Purchase_Price']])
                        validX = True
                    else:
                        print("invalid value for x. Please use a valid number.")
                        validX = False
                if viewQuery == 'purchase_price_over_x':
                    x = input("Enter a value for X: ")
                    if isValidNumber(x) is True:
                        x = int(x)
                        print(Laptop_DataFrame.loc[
                                  Laptop_DataFrame['Purchase_Price'] > x, ['Manufacturer', 'Model', 'Purchase_Price']])
                        validX = True

                    else:
                        print("invalid value for x. Please use a valid number.")
                        validX = False
                # Viewing purchase price
                if viewQuery == 'purchase_price_equals_x':
                    x = input("Enter a value for X: ")
                    if isValidNumber(x) is True:
                        x = int(x)
                        print(Laptop_DataFrame.loc[
                                  Laptop_DataFrame['Purchase_Price'] == x, ['Manufacturer', 'Model', 'Purchase_Price']])
                        validX = True
                    else:
                        print("invalid value for x. Please use a valid number.")
                        validX = False
                # Viewing selling price
                if viewQuery == 'selling_price':
                    print(Laptop_DataFrame[['Manufacturer', 'Model', 'Selling_Price']])
                if viewQuery == 'selling_price_under_x':
                    x = input("Enter a value for X: ")
                    if isValidNumber(x) is True:
                        x = int(x)
                        print(Laptop_DataFrame.loc[
                                  Laptop_DataFrame['Selling_Price'] < x, ['Manufacturer', 'Model', 'Selling_Price']])
                        validX = True

                    else:
                        print("invalid value for x. Please use a valid number.")
                        validX = False
                if viewQuery == 'selling_price_over_x':
                    x = input("Enter a value for X: ")
                    if isValidNumber(x) is True:
                        x = int(x)
                        print(Laptop_DataFrame.loc[
                                  Laptop_DataFrame['Selling_Price'] > x, ['Manufacturer', 'Model', 'Selling_Price']])
                        validX = True

                    else:
                        print("invalid value for x. Please use a valid number.")
                        validX = False

                if viewQuery == 'selling_price_equals_x':
                    x = input("Enter a value for X: ")
                    if isValidNumber(x) is True:
                        x = int(x)
                        print(Laptop_DataFrame.loc[
                                  Laptop_DataFrame['Selling_Price'] == x, ['Manufacturer', 'Model', 'Selling_Price']])
                        validX = True

                    else:
                        print("invalid value for x. Please use a valid number.")
                        validX = False
                # Viewing condition
                if viewQuery == 'condition':
                    print(Laptop_DataFrame[['Manufacturer', 'Model', 'Condition']])

                if viewQuery == 'condition_is_x':
                    condition = input("Which condition do you want to find?")
                    if isValidCondition(condition):
                        print(Laptop_DataFrame.loc[
                                  Laptop_DataFrame['Condition'] == condition, ['Manufacturer', 'Model', 'Condition']])
                    else:
                        print("Please try again.")
                # Viewing year

                if viewQuery == 'year_built':
                    print(Laptop_DataFrame[['Manufacturer', 'Model', 'Year_Built']])

                if viewQuery == 'year_built_before_x':
                    yearBuilt = input("Which year?")
                    if isValidNumber(yearBuilt):
                        yearBuilt = int(yearBuilt)
                        if isValidYear(yearBuilt):
                            print(Laptop_DataFrame.loc[
                                      Laptop_DataFrame['YearBuilt'] < yearBuilt, ['Manufacturer', 'Model',
                                                                                  'YearBuilt']])
                        else:
                            print("Please try again.")
                    else:
                        print("Invalid year.")
                if viewQuery == 'year_built_after_x':
                    yearBuilt = input("Which year?")
                    if isValidNumber(yearBuilt):
                        yearBuilt = int(yearBuilt)
                        if isValidYear(yearBuilt):
                            print(Laptop_DataFrame.loc[
                                      Laptop_DataFrame['YearBuilt'] > yearBuilt, ['Manufacturer', 'Model',
                                                                                  'YearBuilt']])
                        else:
                            print("Please try again.")
                    else:
                        print("Invalid year.")

                if viewQuery == 'year_built_equals_x':
                    yearBuilt = input("Which year?")
                    if isValidNumber(yearBuilt):
                        yearBuilt = int(yearBuilt)
                        if isValidYear(yearBuilt):
                            print(Laptop_DataFrame.loc[
                                      Laptop_DataFrame['YearBuilt'] == yearBuilt, ['Manufacturer', 'Model',
                                                                                   'YearBuilt']])
                        else:
                            print("Please try again.")
                    else:
                        print("Invalid year.")

                if viewQuery == 'model':
                    print(Laptop_DataFrame[['Manufacturer', 'Model']])

                if viewQuery == 'model_is_x':
                    model = input("Which model?")
                    print(Laptop_DataFrame.loc[
                              Laptop_DataFrame['Model'] == model, ['Manufacturer', 'Model']])
                # Viewing manufacturer
                if viewQuery == 'manufacturer':
                    print(Laptop_DataFrame[['Manufacturer', 'Model']])

                if viewQuery == 'manufacturer_is_x':
                    manufacturer = input("Which Manufacturer?")
                    print(Laptop_DataFrame.loc[
                              Laptop_DataFrame['Manufacturer'] == manufacturer, ['Manufacturer', 'Model']])
                if viewQuery == 'describe':
                    print(Laptop_DataFrame.describe())
                if viewQuery == 'sold':
                    print(Sold_Items)
                # To view profit
                if viewQuery == 'profit':
                    profits = []
                    with open("transaction.txt", "r") as file:
                        for line in file:
                            profits.append(int(line))
                    print("Total profit is $" + str(sum(profits)))

                # To quit viewing
                if viewQuery == 'quit':
                    viewQueryQuit = True

                if viewQuery == "help":
                    #Help Menu for Viewing
                    ViewHelpMenu = """
                            
                        COMMAND LIST
                        
                        ' everything ' -> displays everything in the database.
                        
                        PROFIT
                        ' profit ' -> displays total profit earned. 
                        
                        PURCHASE_PRICE
                        ' purchase_price ' -> displays all models, manufacturers, and their respective purchase prices.
                        ' purchase_price_under_x ' -> displays all the laptops the shop purchased under a value: x.
                        ' purchase_price_over_x ' -> displays all the laptops the shop purchased over a value: x.
                        ' purchase_price_equals_x ' -> displays all the laptops the shop purchased equal to a value: x.
                            
                        SELLING_PRICE 
                        ' selling_price' -> displays all laptop models, manufacturers, and their respective purchase prices. 
                        ' selling_price_under_x ' -> displays all the laptops the shop is selling under a value: x.
                        ' selling_price_over_x ' -> displays all the laptops the shop  is  selling  over a value: x.
                        ' selling_price_equals_x ' -> displays all the laptops the shop purchased equal to a value: x. 
                          
                        CONDITION
                            ' condition ' -> displays all laptops and their respective condition."
                        ' condition_is_x ' -> displays all laptops with the specified condition: 'good', 'bad', 'ok'."
                           
                        YEAR BUILT
                        ' year_built ' -> displays all the laptops and their year built.
                        ' year_built_before_x ' -> displays laptops built before a specified year.
                        ' year_built_after_x ' -> displays laptops built after a specified year.
                        ' year_built_equals_x' -> displays laptops built on a specified year.
                                         
                         MODEL
                        ' model ' -> displays all laptop models in the database.
                        ' model_is_x ' -> displays all laptops with the specified model.
                         
                        MANUFACTURER
                        'manufacturer ' -> displays all laptops and their manufacturer. 
                        'manufacturer_is_x ' -> displays all laptops with the specified manufacturer. 
        
                         Data SUMMARY
                        'describe ' Displays descriptive statistics that aid in visualizing the data in the database.
                            
                         SOLD
                        ' sold ' -> displays previously sold items.
                          
                          QUIT"
                         'quit' -> goes back to the main menu.
                        
                        """
                    print(ViewHelpMenu)
        #Buying laptops
        if query == 'buy':
            validSerial = False
            while validSerial is False:
                Serial = input("What is the serial of the laptop?")
                if isValidNumber(Serial):
                    laptop = Laptop(Serial)
                    validSerial = True
                else:
                    print("Invalid Serial. Please use numbers only.")
                    validSerial = False
            #Checking valid models
            validModel = False
            while not validModel:
                Model = input("What is the model of the laptop? (ex 'thinkpad'): ").lower()
                if Model == "" or Model == " ":
                    print("Invalid Model, text or numbers only.")
                    validModel = False
                else:
                    laptop.SetName(Model)
                    validModel = True
            #Checkign valid manufacturers
            validManufacturer = False
            while not validManufacturer:
                Manufacturer = input("What is the manufacturer? (ex: 'ibm'): ").lower()
                if Manufacturer == "" or Manufacturer == " ":
                    print("Invalid manufacturer. numbers or numbers only.")
                    validManufacturer = False
                else:
                    laptop.SetManufacturer(Manufacturer)
                    validManufacturer = True
            #Checking valid years
            validYear = False
            YearBuilt = 0
            while validYear is False:
                try:
                    YearBuilt = int(input("What year was this laptop built? (ex '1998'): "))
                except(TypeError, ValueError):
                    print("Please use four digits for your date. EX: '1998',")
                    validYear = False

                if YearBuilt < 1980 or YearBuilt > 2020 or not isValidNumber(YearBuilt):
                    print("Please choose a date between 1980 and 2020.")
                    validYear = False
                if 1980 <= YearBuilt <= 2020 and (YearBuilt):
                    laptop.SetYearBuilt(YearBuilt)
                    validYear = True
            #Checking valid conditions
            isValidCondition = False
            while not isValidCondition:
                Condition = input("What is the laptop's condition? ('good' 'ok' 'bad'): ").lower()
                if Condition == 'good' or Condition == 'ok' or Condition == 'bad':
                    laptop.SetCondition(Condition)
                    isValidCondition = True
                else:
                    print("Invalid entry. Please use 'good', 'bad', or 'ok' as conditions.")
                    isValidCondition = False

            # Catching bad selling + purchasing prices
            isDigits = False
            while not isDigits:
                Purchase_Price = input("What is the purchase price of the Laptop?")
                Selling_Price = input("What is the selling price of the Laptop?")

                if isValidNumber(Purchase_Price) == True and isValidNumber(Selling_Price) == True:
                    Purchase_Price = float(Purchase_Price)
                    Selling_Price = float(Selling_Price)
                    if Purchase_Price >= 0 and Selling_Price >= 0:
                        if Purchase_Price >= Selling_Price:
                            print("You are attempting to sell the Laptop without profit. Do you want to override this "
                                  "failsafe?")
                            lessProfit = input("'yes' or 'no'?")
                            lessProfit = lessProfit.lower()

                            if lessProfit == 'no':
                                print("Please Re-Enter purchase and selling price.")
                                isDigits = False

                            elif lessProfit == 'yes':
                                laptop.SetPurchasePrice(Purchase_Price)
                                laptop.SetSellingPrice(Selling_Price)
                                isDigits = True

                            else:
                                print("Please choose 'yes' or 'no'")
                                isDigits = False
                        else:
                            laptop.SetPurchasePrice(Purchase_Price)
                            laptop.SetSellingPrice(Selling_Price)
                            isDigits = True
                    else:
                        print("Invalid prices, please choose a positive price.")
                else:
                    print("Invalid Entries.")
                    isDigits = False
            #Storing the laptop details as a dictionary to store it into the Pandas DataFrame
            New_Laptop_Row = {
                'Serial': Laptop.GetSerial(laptop),
                'Model': Laptop.GetName(laptop),
                'Manufacturer': Laptop.GetManufacturer(laptop),
                'YearBuilt': Laptop.GetYearBuilt(laptop),
                'Condition': Laptop.GetCondition(laptop),
                'Purchase_Price': Laptop.GetPurchasePrice(laptop),
                'Selling_Price': Laptop.GetSellingPrice(laptop),
            }
            #Writing the new laptop to the dataframe
            Laptop_DataFrame = Laptop_DataFrame.append(New_Laptop_Row, ignore_index=True)
            Laptop_DataFrame.to_excel("Database.xlsx")
            Laptop_DataFrame = pd.read_excel("Database.xlsx", index_col=0)

            print("Successfully added the " + laptop.Name + " to the Database:")
            print(Laptop_DataFrame[Laptop_DataFrame.Model == laptop.Name])
            print("Transaction complete")
        #QUitting the whole program + Printing the art.
        if query == 'quit':
            print()
            print("Thank you for using LaptopDatabase!")
            PrintLaptopExitArt()
            break
