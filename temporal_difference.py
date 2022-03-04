
from numpy.linalg import solve,det
from problem import *

def TD0(problem :Problem, transitions = 1e4):

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

def LSTD(problem :Problem, f_map, transitions = 1e4):

    threshold = 1e-3
    gamma = problem.gamma
    reward = problem.reward
    S = problem.state_space
    policy = problem.policy
    V = [threshold]*len(S)
    d = len(f_map[1])
    A_1 = threshold * np.identity(d)
    b = [0]*d

    s = problem.N - 1 #inital state
    t = 0
    while t < transitions:
        t += 1
        a = policy(s)
        s1 = problem.next_state(s,a)
        R = reward(s,a) #next reward state
        A_1 += f_map[s]*(f_map[s] - gamma *f_map[s])
        b += f_map[s]*R
        s  = s1
    if det(A_1) == 0:
        A_1 = threshold * np.identity(d)
    w = solve(A_1,b)
    V = np.zeros(len(S))
    for s in S:
        V[s] = np.dot(w.T, f_map[s])
    return V



