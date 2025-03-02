import os
import csv

def parse_symbol_description(symbol_desc):
    """
    Parses the symbol/description field to extract:
      - Symbol: the first token (first 4-5 characters until the first space)
      - Exp Date: the second token
      - Strike: the third token (as a decimal)
      - Type: the fourth token, either "P" or "C"
    Also computes Cash Deployed as: float(strike) * 100.
    """
    tokens = symbol_desc.split()
    if len(tokens) < 4:
        print("Not enough tokens in symbol/description:", symbol_desc)
        return None, None, None, None, None

    symbol = tokens[0]
    exp_date = tokens[1]
    strike = tokens[2]
    option_type = tokens[3]

    try:
        cash_deployed = float(strike) * 100
    except ValueError:
        print("Error converting strike to float:", strike)
        cash_deployed = None

    return symbol, exp_date, strike, option_type, cash_deployed

def parse_transaction_data(data):
    """
    Parses a transaction block into a dictionary with additional fields.
    
    Expected block format:
      Line 1: Transaction Date and Action (e.g., "02/28/2025    Sell to Open")
      Line 2: "Trade Details" (ignored)
      Line 3: Part of the symbol/description (e.g., "JEPQ 03/21/2025 53.00 P")
      Line 4: The rest of the symbol/description (e.g., "PUT J P MORGAN EXCHANGE-$53 EXP 03/21/25")
      Line 5: Quantity (e.g., "1")
      Line 6: Price, Fees & Commission, and Amount (e.g., "$0.22    $0.66    $21.34")
    """
    # Split the data into non-empty lines.
    lines = [line.strip() for line in data.strip().splitlines() if line.strip()]
    
    if len(lines) < 6:
        print("Not enough lines to parse transaction:", lines)
        return None

    # Line 1: Transaction Date and Action.
    parts = lines[0].split(maxsplit=1)
    transaction_date = parts[0]
    action = parts[1] if len(parts) > 1 else ""

    # Lines 3 and 4: Combine for the Symbol/Description.
    symbol_description = f"{lines[2]} {lines[3]}"

    # Parse additional details from Symbol/Description.
    symbol, exp_date, strike, option_type, cash_deployed = parse_symbol_description(symbol_description)

    # Line 5: Quantity.
    quantity = lines[4]

    # Line 6: Price, Fees & Commission, Amount.
    try:
        price, fees_commission, amount = lines[5].split()
    except ValueError:
        print("Error parsing price/fees/amount in block:", lines[5])
        return None

    # Build the transaction dictionary.
    transaction = {
        "Transaction Date": transaction_date,
        "Action": action,
        "Symbol/Description": symbol_description,
        "Quantity": quantity,
        "Price": price,
        "Fees & Commission": fees_commission,
        "Amount": amount,
        "Symbol": symbol,
        "Exp Date": exp_date,
        "Strike": strike,
        "Type": option_type,
        "Cash Deployed": cash_deployed
    }
    return transaction

def main():
    input_file = "input.txt"
    csv_file = "transactions.csv"
    
    # Check for the input file.
    if not os.path.exists(input_file):
        print(f"Input file '{input_file}' not found.")
        return
    
    with open(input_file, 'r') as f:
        content = f.read()

    # Split the content by the delimiter "-----------" and filter out empty blocks.
    blocks = [block.strip() for block in content.split("-----------") if block.strip()]
    
    # Parse each block.
    transactions = []
    for block in blocks:
        parsed = parse_transaction_data(block)
        if parsed:
            transactions.append(parsed)
    
    if not transactions:
        print("No valid transactions found.")
        return

    # Define CSV columns (including new columns).
    fieldnames = [
        "Transaction Date", 
        "Action", 
        "Symbol/Description", 
        "Quantity", 
        "Price", 
        "Fees & Commission", 
        "Amount",
        "Symbol",
        "Exp Date",
        "Strike",
        "Type",
        "Cash Deployed"
    ]
    
    # Determine if header needs to be written.
    write_header = not os.path.exists(csv_file)
    
    # Append transactions to the CSV file.
    with open(csv_file, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        for tx in transactions:
            writer.writerow(tx)
            # Print the transaction on the command line.
            print(tx)

if __name__ == "__main__":
    main()
