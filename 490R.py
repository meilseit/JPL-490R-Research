import numpy as np
import csv
from sklearn.linear_model import LinearRegression

# inputs
gamma = []
beta = []
dgamma = []
dbeta = []

with open("data_test.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    for row in csv_reader:
        gamma.append(float(row[0]))
        beta.append(float(row[1]))
        dgamma.append(float(row[2]))
        dbeta.append(float(row[3]))

# verify the type of row in case code breaks
print(type(row))
print(gamma)
print(beta)
print(dgamma)
print(dbeta)
# declerations
time = []
ratio = []
error = []
fit_constant = True  # the condtion for a constant ratio is set to true

# put numbers in ratio array and error array
for i in range(0, len(gamma)):
    ratio[i] = np.tan(beta[i]) / np.sin(gamma[i])
    a = (1/(((np.cos(beta[i]))**2)*(np.sin(gamma[i]))))*dbeta
    b = (np.tan(beta[i])* -dgamma[i]*np.cos(gamma[i])*(1/(np.sin(gamma[i])**2)))
    error[i] = np.sqrt(a**2 + b**2)
# turn arrays in to numpy arrays

np.asarray(ratio)
np.asarray(error)


num = 0.0
counter = 0.0
# find avg error
for i in error:
    num += i
    counter += 1
#  boundaries for the regression analysis
l_bound = (-num/counter)
h_bound = (num/counter)

# fit the two array that I want
model = LinearRegression().fit(time, ratio)
# the slope of my linear regression
slope = model.coef_
print(slope)
#  the y intercept of our line
y_intr = model.intercept_

if slope != 0.0: #make sure we can get results
    x_intr_l = (l_bound - y_intr)/slope # where the regression line intersects bounds
    x_intr_h = (h_bound - y_intr)/slope

    # compares x values to window of interest to determine if regression line moves outside errors
    if (x_intr_h > time[0] and x_intr_h < time[-1]):
        fit_constant = False
        print(fit_constant)
    elif (x_intr_l > time[0] and x_intr_l < time[-1]):
        fit_constant = False
        print(fit_constant)
else:
    print("the slope is zero")














