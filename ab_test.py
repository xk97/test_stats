"""
A/B testing: Ads Click Through Rate
https://byrony.github.io/understanding-ab-testing-and-statistics-behind.html
Question:
Two Ads, Ad one has 1000 impressions and 20 clicks, CTR is 2%;
Ad two has 900 impressions and 30 clicks, CTR is 3.3%.
Test whether there is difference between Click Through Rate (CTR) between Ad one and two.
"""

import numpy as np
from scipy import stats
#%% t-test for equal mean H0
#Why use t-test rather than Z-test?

# We use t-test instead of Z-test since we don't know the standard deviation of the population. So we use the standard deviation of sample to replace the unknown standard deviation of the population, then t-test should be implemented. Notice this is different from the first example where observation mean is compared with expected mean. As there is only one population, assume the null hypothesis is true then standard deviation of population can be computed.
# follow normal distribution: sample mean ~ N(p, p * (1 - p)/n)

n1, c1, n2, c2 = 1000, 20, 900, 30
p1 = c1 / n1
p2 = c2 / n2
# se - np.sqrt(Var1 / n1 + Var2 / n2 )  # se of mean
se = np.sqrt( p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2 )
t = np.abs(p1 - p2) / se
print(f'{p1}, {p2}, {t}')
p_value = 1 - stats.t.cdf(t, df=min(n1 -1, n2-1))
# two tailed t-test  Ha: not equal mean
print(f'p = {p_value * 2}')
# one tailed t-test  Ha: p2 > p1
print(f'p = {p_value * 2}')


#%% A/B testing Chi-square
#Hypothesis:
#H0: Variable Ad type and variable Whether click are independent
#Ha: Variable Ad type and variable Whether click are not independent
#     click | nonClick
#Ad1
#Ad2
X = np.array([[20, 980], [30, 870]])
print(X)
print('If p_value < 0.05, we can reject null hypothsis')
print('chi2 {}, p_value {}, dof {}, \nexpected {} '.format(*stats.chi2_contingency(X, correction=False)))

#%% Normal Approximation to Binomial:
# we can use normal distribution to approximate binomial distribution (sum of bernoulli) when n is large.
