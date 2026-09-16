import pandas as pd

def func(r, P):
    return ((12 * P) / r) * ((1 + r / 12) ** 300 - 1) - 1000000 # Equation to solve for r, interest rate

print("f(a): ", func(0.01, 500))    # Step 1, found bracket [a, b] where f(a)f(b) < 0
print("f(b): ", func(0.50, 500))
print("f(a)f(b) =", func(0.01,500) * func(0.50,500), "< 0")

def bisection(a, b, P):             # Step 2, continously find midpoint and find f(mid)
    while ((b - a) / 2) > 1e-6:    # If maximum error from midpoint becomes less than allowed tolerance, 
                                    # we reached point where we acecpt midpoint as closest approximation to answer
        mid = (a + b) / 2

        if func(mid, P) == 0:       # Return midpoint if solution found
            return mid

        if (func(a, P) * func(mid, P)) < 0:        # Set b down to mid if less than 0
            b = mid

        if (func(a, P) * func(mid, P)) > 0:        # Set a up to mid if greater than 0
            a = mid

    return (a + b) / 2              # If exactly = 0 solution never found, use very close midpoint approx when tolerance becomes greater

monthlyDeposits = []                # Prepare lists to make Pandas table
interestRates = []

for P in range(500, 1001, 50):                      # For each dollar deposist value, add deposit value and following interest rate to lists
    r = bisection(0.01, 0.50, P)
    monthlyDeposits.append(P)
    interestRates.append(r * 100)

table = pd.DataFrame({                              # Form table and print values
    "Monthly deposits ($)": monthlyDeposits,
    "Interest rates (%)": interestRates
})

print(table)