import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

# Calculate 60 input values (1 - 60) according to formula, 2pi(i) / 60, for producing t
# np.arrange creates array from 1 - 60
t = (2 * np.pi * np.arange(1, 61)) / 60

# For producing y, use formula e^sin(t - 1)
# Since t is array, it actually raises e to each value in array so that we produce y with 60 values
y = np.e ** np.sin(t - 1)

# Randomly generate 60 numbers then 10% * y * random numbers to produce 60 random errors
noise = 0.1 * y * np.random.randn(60)

# Add such noise to y to get 60 output values with errors
y_with_noise = y + noise



# Create poly matrix according to formula
# Use np.column_stack to combine 1D arrays into matrix
A = np.column_stack([
    np.ones(60),  
    t,        
    t ** 2,  
    t ** 3,     
    t ** 4,   
    t ** 5,    
    t ** 6      
])

b = y_with_noise # b becomes y values with noise
AT = A.T # AT is A transpose

# Want to find ATA = ATb, so calculate both using @ as matrix multiplier
ATA = AT @ A
ATb = AT @ b

# np.linalg solves linear matrix equations
# Use to solve ATAc = ATb for unknown coefficients
c = np.linalg.solve(ATA, ATb)

# Get y values when finally multipling coefficients with A
y_c = A @ c

# Calculate residuals to start finding RMSE
r = b - y_c

# np.sum adds all residuals squared, then / 60 and sqrt to find rmse
rtop = np.sum(r ** 2)
rmse = np.sqrt(rtop / 60)

print("Poly coefficients:", c)
print("Poly RMSE:", rmse)

# Create trig matrix according to formula
B = np.column_stack([
    np.ones(60),
    np.cos(t),
    np.sin(t),
    np.cos(2 * t),
    np.sin(2 * t)
])

# Pretty much same proces but trig matrix and 5 coefficients
BT = B.T

BTB = BT @ B
BTb = BT @ b

d = np.linalg.solve(BTB, BTb) # Solve BTBd = BTb

y_d = B @ d

# Calculate RMSE
r_d = b - y_d

rtop_d = np.sum(r_d ** 2)
rmse_d = np.sqrt(rtop_d / 60)

print("Trig coefficients:", d)
print("Trig RMSE:", rmse_d)

# Plot noisy y data points
plt.scatter(t, y_with_noise, label="Noisy data y")

# Plot poly and trig least squares fit curves
plt.plot(t, y_c, label="Polynomial least-squares fit")
plt.plot(t, y_d, label="Trigonometric least-squares fit")

plt.xlabel("t")
plt.ylabel("y")
plt.title("Least Squares Fits")
plt.legend()
plt.grid()
plt.show()