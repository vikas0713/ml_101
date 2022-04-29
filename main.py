import numpy
import pandas
import matplotlib.pyplot as plt
from pandas import DataFrame


from sklearn.linear_model import LinearRegression


data = pandas.read_csv('data/3.2 cost_revenue_clean.csv')
X = numpy.array(DataFrame(data, columns=['production_budget_usd']))
y = numpy.array(DataFrame(data, columns=['worldwide_gross_usd']))


# running regression here
regression = LinearRegression()
regression.fit(X, y)
print(regression.coef_)    # theta_1
# Intercept
print(regression.intercept_)   # theta_0

# Linear regression Formula to predict theta_0 + theta_1*x

plt.scatter(X, y, alpha=0.3)
plt.plot(X, regression.predict(X), color='red', linewidth=4)
plt.title("Budget Vs Worldwide Gross")
plt.xlabel("Production Budget in USD")
plt.ylabel("Worldwide Gross in  USD")
plt.show()

# Evaluate
print(regression.score(X, y)*100)
