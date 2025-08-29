import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sample data: Portfolio values over time (monthly)
dates = pd.date_range(start='2020-01-01', periods=12, freq='M')  # 12 months from January 2020
portfolio_value = np.array([10000, 10200, 10500, 11000, 11500, 12000, 12500, 13000, 14000, 15000, 16000, 17000])  # Portfolio values for each month

# Create a DataFrame to hold the data
portfolio_df = pd.DataFrame({
    'Date': dates,
    'Portfolio Value': portfolio_value
})

# Plotting the line chart
plt.figure(figsize=(10, 6))
plt.plot(portfolio_df['Date'], portfolio_df['Portfolio Value'], marker='o', color='blue', linestyle='-', linewidth=2, markersize=6)

# Adding title and labels
plt.title('Portfolio Growth Over Time', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Portfolio Value ($)', fontsize=12)

# Rotate date labels for better readability
plt.xticks(rotation=45)

# Adding grid for better visualization
plt.grid(True)

# Tight layout to make sure everything fits
plt.tight_layout()

# Show the chart
plt.show()
