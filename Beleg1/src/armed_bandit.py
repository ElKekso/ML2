#%%
import numpy as np
import matplotlib.pyplot as plt

def get_bandit_function(k):
    mean, deviation = 0, 1                                                 
    rng = np.random.default_rng()                               
    bandit_means = []
    for x in range(k):                                          #draw k gaussian random numbers q_i as centers
        bandit_means.append(rng.normal(mean, deviation))

    def bandit_function(action):                                #define a function which expects a parameter action and returns a random number from N(q_i,1)
        return rng.normal(bandit_means[action], 1)

    return bandit_function, bandit_means                        #return that function and a list of the q_i's

func,bandit_means = get_bandit_function(5)

print(bandit_means)

plt.plot([1,2,3,4],[3,7,2,12])

plt.show



