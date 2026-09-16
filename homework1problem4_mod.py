import pandas as pd
import matplotlib.pyplot as plt

def func(x):                    
    return 0.5 * (x + 9 / x)

x = 500
iteration = 0

iterations = []
errors = []
xlist = []

while 1:                            # Always run until tolerance level is greater than change in iteration from x to newX
    iterations.append(iteration)    # Record data, that being the iteration count, the x value, and errors
    xlist.append(x)
    errors.append(abs(x - 3))
    
    newX = func(x)                  # Plug new X value into function
    
    if abs(newX - x) < 1e-6:       # Keep going until change per iteration is less than tolereance
        iteration += 1
        iterations.append(iteration)
        xlist.append(newX)
        errors.append(abs(newX - 3))
        break

    x = newX                        # If change in iteration is still large, set x to new X
    iteration += 1

table = pd.DataFrame({                              # Form table and print values
    "Iterations": iterations,
    "X": xlist,
    "Errors": errors
})

print(table)

plt.semilogy(iterations, errors)                    # Plot graph
plt.xlabel("Iterations")
plt.ylabel("Errors")
plt.show()