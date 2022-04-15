import numpy as np
import csv
from sklearn.linear_model import LinearRegression

# inputs
gamma = []
beta = []
dgamma = []
dbeta = []

with open('data_test.csv', mode ='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        gamma.append(float(row['gamma']))
        beta.append(float(row['beta']))
        dgamma.append(float(row['dgamma']))
        dbeta.append(float(row['dbeta']))








# declerations
time = []
ratio = []
error = []
fit_constant = True  # the condtion for a constant ratio is set to true

# put numbers in ratio array and error array
for i in range(0, len(gamma)):
    temp_ratio = np.tan(beta[i]) / np.sin(gamma[i])
    ratio.append(temp_ratio)
    print(*ratio)
    a = (1.0/(((np.cos(beta[i]))**2.0)*(np.sin(gamma[i]))))*dbeta[i]
    b = (np.tan(beta[i])* -dgamma[i]*np.cos(gamma[i])*(1/(np.sin(gamma[i])**2)))
    temp_error = np.sqrt(a**2 + b**2)
    error.append(temp_error)
# turn arrays in to numpy  arrays and create time array
for i in range(0, len(gamma)):
    time.append(i)
x = np.array(time).reshape(-1,1)
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
print("lower bound is:",l_bound)

# fit the two array that I want
model = LinearRegression().fit(x, ratio)
# the slope of my linear regression
slope = model.coef_
print("the slope is:", slope)
#  the y intercept of our line
y_intr = model.intercept_

print("the y intercept:", y_intr)

if slope != 0.0: #make sure we can get results
    x_intr_l = (l_bound - y_intr)/slope # where the regression line intersects bounds
    x_intr_h = (h_bound - y_intr)/slope
    print(x_intr_h)
    print(x_intr_l)
    print(x[0])
    print(x[-1])

    # compares x values to window of interest to determine if regression line moves outside errors
    if x_intr_h > x[0] and x_intr_h < x[-1]:
        fit_constant = False
        print(fit_constant)
    elif (x_intr_l > x[0] and x_intr_l < x[-1]):
        fit_constant = False
        print(fit_constant)
else:
    print("the slope is zero")
for i in range(len(gamma)):
    if abs(l_bound - ratio[i]) < error[i]:
        print("good")
    else:
        print("bad")



