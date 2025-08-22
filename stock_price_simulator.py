import numpy as np

# Used for same value
np.random.seed(42)

# Random Stock prices for 30 days
random_prices=np.random.randint(100,501,30)
print(random_prices)

# Daily Returns 
difference=np.diff(random_prices)
print(f"Daily returns = {difference}")


# Highest and lowest price in 30 days
highest_price=np.max(random_prices)
lowest_price=np.min(random_prices)
print(f"Highest Price in 30 days was: {highest_price}.")
print(f"Lowest Price in 30 days was: {lowest_price}.")

# Moving average of 5 days 
moving_avg=np.sum(random_prices[0:5])/5
print(f"Moving average for 5 days was: {moving_avg}.")




