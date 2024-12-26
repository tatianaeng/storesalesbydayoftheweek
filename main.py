# design a program that asks the user to enter a store's sales for each day of the week
# the amounts should be stored in a list
# use a loop to calculate the total sales for the week and display the result

# create an empty list
salesThisWeek = []

# ask the user to enter the store's sales 7 times (1 for each day of the week)
for day in range(1,8):

    # ask user to input the store's sales for that day
    amountInSales = float(input(f"How much did we bring in in sales on day {day} this week? $"))

    print(f"Day {day} sales: ${amountInSales:.2f}\n")

    # add that day's sales amount to the list
    salesThisWeek.append(amountInSales)

    # increment the "day" counter
    day += 1

# print the list containing the 7 sales amounts
print(f"Each day's sales this week in dollars: {salesThisWeek}")

# create and initialize a weeklyTotal variable
weeklyTotal = 0

# iterate through each day's sales amount in the list
for amount in salesThisWeek:

    # keep a running total of the weekly sales amount
    weeklyTotal = weeklyTotal + amount

# print result
print(f"The store sold ${weeklyTotal:,.2f} this week!")