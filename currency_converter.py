
# Project: Currency Converter
# PS No. 35
# Language: Python 3

EXCHANGE_RATES = {
    "INR": 1,
    "USD": 83,
    "EUR": 90,
    "GBP": 105
}


def convert_to_inr(amount, currency):
    """Convert the given amount to INR."""
    return amount * EXCHANGE_RATES[currency]


def convert_currency(amount, from_currency, to_currency):
    """Convert an amount between supported currencies."""
    amount_in_inr = convert_to_inr(amount, from_currency)
    converted_amount = amount_in_inr / EXCHANGE_RATES[to_currency]
    return round(converted_amount, 2)


def main():
    print("===== CURRENCY CONVERTER =====")
    print("Supported currencies: INR, USD, EUR, GBP")

    try:
        amount = float(input("Enter amount: "))

        if amount < 0:
            print("Amount cannot be negative.")
            return

        from_currency = input("From currency: ").strip().upper()
        to_currency = input("To currency: ").strip().upper()

        if from_currency not in EXCHANGE_RATES:
            print(
                f"Unsupported currency '{from_currency}'. "
                "Available: INR, USD, EUR, GBP"
            )
            return

        if to_currency not in EXCHANGE_RATES:
            print(
                f"Unsupported currency '{to_currency}'. "
                "Available: INR, USD, EUR, GBP"
            )
            return

        result = convert_currency(
            amount, from_currency, to_currency
        )

        print(
            f"{amount:g} {from_currency} = "
            f"{result:.2f} {to_currency}"
        )

    except ValueError:
        print("Invalid amount. Enter a number.")


if __name__ == "__main__":
    main()
