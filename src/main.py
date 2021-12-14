'''

Problem Description : You are developing a smartphone app. You have a list of potential customers for your app.
Each customer has a budget and will buy the app at your declared price if and only if the price is less than or equal to the customer's budget.
You want to fix a price so that the revenue you earn from the app is maximized. Find this maximum possible revenue.

For instance, suppose you have 4 potential customers and their budgets are 60, 30, 20, 53 and 14.
In this case, the maximum revenue you can get is 60 .

'''


def findMaxBudget(n, arr):
    # Bubble sort the Array
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j + 1] = arr[j+1] , arr[j]

    # Multiply the smallest element with length of array so that we have base maxBudget which can be comapre with other elements.
    maxBudgte = arr[0] * n

    # Comparing maxBuddget with other elements, if found maxBudget will be udpated.
    for i in range(1,n):
        if maxBudgte < (arr[i] * (n-i)):
            maxBudgte = arr[i] * (n-i)

    return  maxBudgte

if __name__ == "__main__":
    noOfCustomer = 4
    budgte = [30, 20, 53, 14]

    # Calling the function with no of customer and budget array
    maxBudgte = findMaxBudget(noOfCustomer , budgte)

    print("Maximum Budget is $%d" %maxBudgte)



