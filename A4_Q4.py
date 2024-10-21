import numpy as np

# Function to calculate daily percentage change for each stock
def calculate_daily_percentage_change(stock_prices):
    percentage_changes = np.diff(stock_prices, axis=1) / stock_prices[:, :-1] * 100
    return percentage_changes

# Function to find the stock with the highest volatility (variance in daily returns)
def find_most_volatile_stock(percentage_changes):
    variances = np.var(percentage_changes, axis=1)
    most_volatile_stock = np.argmax(variances)
    return most_volatile_stock, variances[most_volatile_stock]

# Function to determine the best-performing stock over 10 days (based on overall price increase)
def find_best_performing_stock(stock_prices):
    total_change = stock_prices[:, -1] - stock_prices[:, 0]
    best_stock = np.argmax(total_change)
    return best_stock, total_change[best_stock]

# Function to find days where any stock price dropped more than 5%
def find_price_drops(percentage_changes, threshold=-5):
    days_with_drops = np.where(percentage_changes < threshold)
    return days_with_drops

# Function to simulate stock prices input
def get_stock_data():
    # Simulating stock data for 4 stocks over 10 days
    np.random.seed(42)  # For reproducibility
    stock_prices = np.random.randint(90, 110, size=(4, 10)) + np.cumsum(np.random.randn(4, 10) * 2, axis=1)
    print("Simulated Stock Prices (Rows: Stocks, Columns: Days):\n", stock_prices)
    return stock_prices

def main():
    stock_prices = None
    while True:
        print("\nChoose an option:")
        print("1. Calculate daily percentage change for each stock")
        print("2. Identify the stock with the highest volatility")
        print("3. Determine the best-performing stock over the 10-day period")
        print("4. Find days where any stock price dropped more than 5% from the previous day")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1 or choice == 2 or choice == 3 or choice == 4:
            if stock_prices is None:
                stock_prices = get_stock_data()

            if choice == 1:
                percentage_changes = calculate_daily_percentage_change(stock_prices)
                print("Daily Percentage Changes (Rows: Stocks, Columns: Days):\n", percentage_changes)

            elif choice == 2:
                percentage_changes = calculate_daily_percentage_change(stock_prices)
                stock_index, volatility = find_most_volatile_stock(percentage_changes)
                print(f"Stock {stock_index + 1} is the most volatile with a variance of {volatility:.2f}%.")

            elif choice == 3:
                best_stock, best_performance = find_best_performing_stock(stock_prices)
                print(f"Stock {best_stock + 1} is the best-performing stock with a total increase of {best_performance:.2f} units.")

            elif choice == 4:
                percentage_changes = calculate_daily_percentage_change(stock_prices)
                drop_days = find_price_drops(percentage_changes)
                if drop_days[0].size > 0:
                    for stock, day in zip(drop_days[0], drop_days[1]):
                        print(f"Stock {stock + 1} dropped more than 5% on Day {day + 2}.")
                else:
                    print("No stock dropped more than 5% on any day.")
        
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
