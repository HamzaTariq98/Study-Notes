import numpy as np


def state_function(s, rewards, gamma, action, n):

    if action == 'left':
        s_ = s-1
    else:
        s_ = s+1
    if s == 0:
        return 100
    if s == 5:
        return 40
    return rewards[s] + gamma**n*max(state_function(s_, rewards, gamma, 'left', n+1), state_function(s_, rewards, gamma, 'right', n+1))


rewards = [100, 0, 0, 0, 0, 40]


print(state_function(2, rewards, 0.5, 'left', 1))
