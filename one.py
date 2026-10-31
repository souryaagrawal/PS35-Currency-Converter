
# Project: Currency Converter
# PS No. 35
# Language: Python 3

# Store exchange rates with INR as the base currency 
EXCHANGE_RATES = {
    "INR": 1,
    "USD": 83,
    "EUR": 90,
    "GBP": 105
}

# Convert the given amount into INR
def convert_to_inr(amount, currency):
    """Convert the given amount to INR."""
    return amount * EXCHANGE_RATES[currency]

# Convert an amount from one currency  to another
def convert_currency(amount, from_currency, to_currency):
    """Convert an amount between supported currencies."""
    amount_in_inr = convert_to_inr(amount, from_currency)
    converted_amount = amount_in_inr / EXCHANGE_RATES[to_currency]
    return round(converted_amount, 2)

# Main function
def main():
    print("===== CURRENCY CONVERTER =====")
    print("Supported currencies: INR, USD, EUR, GBP")

    try:
        # Get the amount from the user
        amount = float(input("Enter amount: "))
        
        # Check for negative amount               
        if amount < 0:
            print("Amount cannot be negative.")
            return
            
       # Get source and target currencies
        from_currency = input("From currency: ").strip().upper()
        to_currency = input("To currency: ").strip().upper()
        
       # Validate source currency
        if from_currency not in EXCHANGE_RATES:
            print(
                f"Unsupported currency '{from_currency}'. "
                "Available: INR, USD, EUR, GBP"
            )
            return
            
       # Valid target currency
        if to_currency not in EXCHANGE_RATES:
            print(
                f"Unsupported currency '{to_currency}'. "
                "Available: INR, USD, EUR, GBP"
            )
            return
            
       # Convert the amount into the target currency
        result = convert_currency(
            amount, from_currency, to_currency
        )
        
       # Display the converted amount
        print(
            f"{amount:g} {from_currency} = "
            f"{result:.2f} {to_currency}"
        )

    except ValueError:
        print("Invalid amount. Enter a number.")


if __name__ == "__main__":
    main()
