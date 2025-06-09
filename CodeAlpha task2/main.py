import os
import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Predefined stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2750,
    "AMZN": 3200,
    "MSFT": 310
}

class Portfolio:
    def __init__(self, stock_prices: dict):
        self.stock_prices = stock_prices
        self.holdings = {}
        self.total_value = 0

    def add_stock(self, symbol: str, quantity: int):
        symbol = symbol.upper()
        if symbol not in self.stock_prices:
            raise ValueError(f"Stock symbol '{symbol}' not found.")
        price = self.stock_prices[symbol]
        value = price * quantity

        if symbol in self.holdings:
            self.holdings[symbol]['quantity'] += quantity
            self.holdings[symbol]['value'] += value
        else:
            self.holdings[symbol] = {
                'quantity': quantity,
                'price': price,
                'value': value
            }

        self.total_value += value

    def get_summary_data(self):
        return [
            {"Symbol": symbol, "Quantity": data["quantity"], "Price": data["price"], "Value": data["value"]}
            for symbol, data in self.holdings.items()
        ]

    def display_summary(self):
        print("\n📊 Portfolio Summary:\n")
        print(f"{'Symbol':<8}{'Quantity':<10}{'Price':<10}{'Value':<10}")
        print("-" * 40)
        for row in self.get_summary_data():
            print(f"{row['Symbol']:<8}{row['Quantity']:<10}{row['Price']:<10}${row['Value']:<10}")
        print("-" * 40)
        print(f"{'Total Investment Value:':<28} ${self.total_value}")

    def generate_summary_image(self, show_image=False, save_path=None):
        df = pd.DataFrame(self.get_summary_data())
        df.loc[len(df)] = ["TOTAL", "", "", self.total_value]

        fig, ax = plt.subplots(figsize=(8, len(df) * 0.6))
        ax.axis('off')
        ax.axis('tight')

        table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1.1, 1.5)
        plt.title("Stock Portfolio Summary", fontsize=14, pad=12)

        if save_path:
            plt.savefig(save_path, bbox_inches="tight")
            print(f"🖼️ Image saved to: {save_path}")
        if show_image:
            plt.show()
        plt.close()

    def save_to_csv(self, filepath: str):
        with open(filepath, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Symbol", "Quantity", "Price", "Value"])
            writer.writeheader()
            writer.writerows(self.get_summary_data())
            writer.writerow({})
            writer.writerow({"Symbol": "Total Investment", "Value": self.total_value})
        print(f"📂 CSV saved to: {filepath}")

def get_desktop_path():
    return os.path.join(os.path.expanduser("~"), "Desktop")

def ask_yes_no(prompt):
    return input(prompt + " (yes/no): ").strip().lower() in ("yes", "y")

def run_portfolio_app():
    print("📈 Welcome to the Stock Portfolio Tracker!")
    print("Enter stock symbol and quantity. Type 'done' to finish.\n")

    portfolio = Portfolio(STOCK_PRICES)

    while True:
        symbol = input("Enter stock symbol (or 'done'): ").strip()
        if symbol.lower() == "done":
            break
        try:
            qty = int(input(f"Enter quantity of {symbol.upper()}: "))
            if qty <= 0:
                print("❌ Quantity must be positive.\n")
                continue
            portfolio.add_stock(symbol, qty)
            print(f"✅ Added {qty} shares of {symbol.upper()}.\n")
        except ValueError as ve:
            print(f"⚠️ {ve}\n")

    if not portfolio.holdings:
        print("📭 No stocks added. Exiting.")
        return

    portfolio.display_summary()

    if ask_yes_no("\n📷 Would you like to **view** the portfolio image on screen?"):
        portfolio.generate_summary_image(show_image=True)

    if ask_yes_no("\n💾 Would you like to **save** summary to your Desktop as CSV and image?"):
        desktop = get_desktop_path()
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        csv_path = os.path.join(desktop, f"portfolio_summary_{timestamp}.csv")
        img_path = os.path.join(desktop, f"portfolio_summary_{timestamp}.png")
        portfolio.save_to_csv(csv_path)
        portfolio.generate_summary_image(save_path=img_path)

    print("\n✅ Program finished. Thank you for using the tracker!")

if __name__ == "__main__":
    run_portfolio_app()
