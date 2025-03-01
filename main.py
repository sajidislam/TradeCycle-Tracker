data = """
02/28/2025    Sell to Open
Trade Details
JEPQ 03/21/2025 53.00 P 
PUT J P MORGAN EXCHANGE-$53 EXP 03/21/25
1
$0.22    $0.66    $21.34
"""

def parse_transaction_data(data):
    # Split the data into non-empty lines and remove extra whitespace.
    lines = [line.strip() for line in data.strip().splitlines() if line.strip()]

    # The first line contains the transaction date and action.
    # Example: "02/28/2025    Sell to Open"
    parts = lines[0].split(maxsplit=1)
    transaction_date = parts[0]
    action = parts[1] if len(parts) > 1 else ""

    # The second line is "Trade Details" which we skip.
    # The third and fourth lines together form the symbol/description.
    symbol_description = f"{lines[2]} {lines[3]}"

    # The fifth line is the quantity.
    quantity = lines[4]

    # The sixth line contains price, fees & commission, and amount.
    price, fees_commission, amount = lines[5].split()

    return {
        "Transaction Date": transaction_date,
        "Action": action,
        "Symbol/Description": symbol_description,
        "Quantity": quantity,
        "Price": price,
        "Fees & Commission": fees_commission,
        "Amount": amount
    }

# Test the parser with the provided data.
parsed_data = parse_transaction_data(data)
print(parsed_data)
