#  Our usual imports
import numpy as np

import scipy
from scipy.stats import norm

import matplotlib.pyplot as plt
%matplotlib inline

#  Black-Scholes formulas for call and put prices
def call_price(d1, d2, S, K, r, t):
    C = np.multiply(S, norm.cdf(d1)) - \
        np.multiply(norm.cdf(d2) * K, np.exp(-r * t))
    return C

def put_price(d1, d2, S, K, r, t):
    P = -np.multiply(S, norm.cdf(-d1)) + \
        np.multiply(norm.cdf(-d2) * K, np.exp(-r * t))
    return P

#  Utility function to calculate the d1 and d2 vcalues that are needed above
def d(S, K, r, sigma, t):
    d1 = np.multiply( 1. / sigma * np.divide(1., np.sqrt(t)),
        np.log(S/K) + (r + sigma**2 / 2.) * t  )
    d2 = d1 - sigma * np.sqrt(t)
    return d1, d2

#  We will assume the 50 strike call

#  These are needed for the Black-Schole model, but these values are unimportant as we are setting time to zero
r = 0.01
sigma = 0.2

#  Days to expiration.  We are interested in the call's value at expiration.
t = 0

#  Strike Price
K = 50

#  We are assuming we paid a debit of this much for the call
C0 = 1.45

#  Generate a range of stock prices for plotting.  There will be issues with this is S is exactly equal to K.
S = np.linspace(45, 55, 100)

#  Calculate the call price as a function of S
d1, d2 = d(S, K, r, sigma, t)
C = call_price(d1, d2, S, K, r, t)

#  Plot the payout graph
plt.plot(S, C - C0, 'k')
plt.xlabel('Stock Price ($)')
plt.ylabel('Profit/Loss ($)')
plt.grid(True)

#  Parameters needed for the model
r = 0.01
sigma = 0.2

#  Zero DTE
t = 0

#  We are assuming we are Long the 50/52 call spread.
#  In other words, we are long the 50 and short the 52 call.
#  These are the strikes
K1 = 50
K2 = 52

#  We are assuming this is the cost of the spread when we placed the position.
C0 = 1.10

#  Generate a range of stock prices
S = np.linspace(45, 55, 100)

#  Calculate the price of the 50-strike option
d1, d2 = d(S, K1, r, sigma, t)
C1 = call_price(d1, d2, S, K1, r, t)

#  Calculate the price of the 52-strike option.
d1, d2 = d(S, K2, r, sigma, t)
C2 = call_price(d1, d2, S, K2, r, t)

# Plot Payout
plt.plot(S, (C1 - C2) - C0)
plt.grid(True)
plt.xlabel('Stock Price ($)')
plt.ylabel('Profit/Loss ($)')