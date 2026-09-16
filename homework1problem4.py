def func(x):                    
    return 0.5 * (x + 9 / x)

x = 500

while 1:                            # Always run until tolerance level is greater than change in iteration from x to newX
    newX = func(x)                  # Plug new X value into function

    if abs(newX - x) < 1e-6:       # Keep going until change per iteration is less than tolereance
        print(newX)                 # Print what iteration converged onto
        break

    x = newX                        # If change in iteration is still large, set x to new X

