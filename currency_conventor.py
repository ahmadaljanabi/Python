def convertor(currency_type, dollar_value):
    currency = input("How much " + currency_type + " Do you have ? ")
    currency = float(currency)
    dollars = currency / dollar_value
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print("You have $" + dollars + " US Dollars")

menu = """
Welcome to the Currency Convertor

1 - Saudi Riyal (SAR)
2 - Euros (EUR)
3 - Great British Pound (GBP)

Choose an option: """

option = int(input(menu))

if option == 1:
    convertor("Saudi Riyal", 3.75)
elif option == 2:
    convertor("Euros", 1.12)
elif option == 3:
    convertor("Great British Pound", 1.32)
else:
    print("Enter a correct option pleae !")