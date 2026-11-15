
import numpy as np                                      # For arrays and math ops
import matplotlib.pyplot as plt                         # For plotting graphs
import yfinance as yf                                   # For downloading stock prices
from scipy.interpolate import BarycentricInterpolator   # For polynomial interpolation
from scipy.interpolate import CubicSpline               # For natural cubic spline interpolation

stock_data = yf.Ticker("AMD").history(period="12mo")                    # Get year's worth of data of AMD stock prices
stock_prices = stock_data["Close"].dropna().to_numpy()[-101:]            # Get the closing prices of last 100 stock days for AMD

x = np.arange(101)                          # Make x-axis 0, 1, ..., 100
y = stock_prices                            # Make y-axis the closing prices for each AMD day

x5 = x[::5]                                 # x0 will contain every 5th day, like 0, 5, 10, etc
y5 = y[::5]                                 # y0 will be closing prices on every 5th day

polynomial = BarycentricInterpolator(x5, y5)        # Make polynomial through 21 points
y_polynomial = polynomial(x)                        # Make polynomial on all 101 days
error_polynomial = np.abs(y - y_polynomial)         # Find difference between polynomial for 21 and polynomial for 100 on each day
max_error_polynomial = np.max(error_polynomial)     # Find the largest polynomial error

plt.figure()                     
plt.plot(x, y, label="Daily closing prices")        # Plot all 101 closing prices
plt.plot(x, y_polynomial, label="Polynomial")       # Plot polynomial interpretation
plt.scatter(x5, y5, label="Points")                 # Mark every 5th x and y
plt.xlabel("Day")                    
plt.ylabel("Closing price ($)")              
plt.title("Degree 20 Polynomial Interpolation")             
plt.legend()                                 
plt.grid()                                   
plt.show()                                   

print("Maximum polynomial error:", max_error_polynomial)    # Print maximum error for polynomial interpreation

cubic_spline = CubicSpline(x5, y5, bc_type="natural")       # Make natural cubic spline
y_cubic_spline = cubic_spline(x)                            # Make natural cubic spline on all 101 days
error_cubic_spline = np.abs(y - y_cubic_spline)                   # Find difference between nautral cubic spline for 21 and for 101 on each day
max_cubic_spline_error = np.max(error_cubic_spline)                           # Find largest cubic spline error

plt.figure()           
plt.plot(x, y, label="Daily closing prices")        
plt.plot(x, y_cubic_spline, label="Cubic Spline")        # Plot natural cubic spline interpolation
plt.scatter(x5, y5, label="Points")        
plt.xlabel("Day")                    
plt.ylabel("Closing price ($)")        
plt.title("Natural Cubic Spline Interpolation")         
plt.legend()                                
plt.grid()                              
plt.show()                                

print("Maximum cubic spline error:", max_cubic_spline_error)   # Print maximum error for natural cubic splien interpolation