
from problem import *

def TD0(problem :problem, transitions = 1e4):

    threshold = 1e-3
    gamma = problem.gamma
    reward = problem.reward
    S = problem.state_space
    policy = problem.policy
    V = [threshold]*len(S)
    
    s = problem.N - 1 #inital state
    t = 0
    while t < transitions:
        t += 1
        alpha_t = 1e5/(t + 1e5)
        a = policy(s)
        s1 = problem.next_state(s,a)
        R = reward(s,a) #next reward state
        V[s] = V[s] + alpha_t * (R + gamma * V[s1] - V[s])
        s  = s1
    return V

