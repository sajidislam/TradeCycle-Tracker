# TradeCycle-Tracker

**TradeCycle-Tracker** is a Python tool designed to help options traders track and analyze effective capital utilization. The project addresses the common challenge where the same funds are repeatedly reused across multiple trades, making the sum of individual cash investments misleading compared to the actual capital deployed.

## The Problem

As a frequent options trader—using strategies like cash-secured puts and covered calls—you might experience a scenario like this:

- You use $700 for a cash-secured put, receive a credit, and later close the trade with a small profit.
- Later in the day (or week), you reuse that same $700 for additional trades.
- If you add up the cash amounts for each trade (e.g., $700 used three times equals $2100), it falsely appears that you’ve deployed much more capital than you actually have.

This discrepancy can make it hard to accurately assess your trading performance and capital utilization.

## The Solution

**TradeCycle-Tracker** resolves this dilemma by:

- **Parsing Transaction Data:** Automatically extracting details from your brokerage transaction history.
- **Tracking Effective Capital:** Monitoring how much of your actual funds are tied up in open positions at any given time.
- **Custom Analysis:** Providing insights that help you manage risk and optimize your trading strategy based on your true capital deployment.

## Features

- **Data Parsing:** Convert raw transaction logs into structured data.
- **Capital Utilization Analysis:** Calculate and display the real-time amount of capital deployed.
- **Customizable Reporting:** Adjust the analysis to suit your specific trading patterns and needs.

## Example Transaction

Below is an example of how your transaction history might look in Schwab transaction history:

02/28/2025 Sell to Open Trade Details JEPQ 03/21/2025 53.00 P PUT J P MORGAN EXCHANGE-$53 EXP 03/21/25 1 $0.22 $0.66 $21.34


From this data, the tool will extract:
- **Transaction Date:** `02/28/2025`
- **Action:** `Sell to Open`
- **Symbol/Description:** `JEPQ 03/21/2025 53.00 P PUT J P MORGAN EXCHANGE-$53 EXP 03/21/25`
- **Quantity:** `1`
- **Price:** `$0.22`
- **Fees & Commission:** `$0.66`
- **Amount:** `$21.34`

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/TradeCycle-Tracker.git
   cd TradeCycle-Tracker


2. Install Dependencies: Install any required packages (if applicable) using pip:

pip install -r requirements.txt

3. Run the Parser: Use the provided Python script to parse your transaction data:

python parse_transactions.py

4. Customize Your Analysis: Modify the code as needed to better integrate with your specific trading strategy.


Contributing
Contributions are welcome! If you have suggestions, improvements, or additional features you’d like to see, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License.

In my opinion, TradeCycle-Tracker offers a clear and efficient way to understand your true capital usage, helping you refine your strategy to meet your trading goals.

Feel free to modify or expand this README as your project evolves.
