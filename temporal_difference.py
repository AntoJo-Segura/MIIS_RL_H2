
from problem import *

def TD0(problem :problem, max_iter = 100):

    increment = 0
    threshold = 1e-3
    gamma = problem.gamma
    reward = problem.reward
    S = problem.state_space
    transition_p = problem.transition_p
    actions = problem.actions
    policy = problem.policy_p
    V = [threshold]*len(S)
    v = 0
    increment = threshold +1 #just enter into loop
    loop = 0 
    alpha = 0.1 #step size
    
    for i,s in enumerate(S):#For each s in S
        #Sp = problem.state_space
        #for ip, sp in enumerate(Sp):#innecessary loop because it is one-step
        a = policy(s)
        i1 = problem.next_state(s,a)
        R = problem.reward(s,a) #next reward state
        V[i] = V[i] + alpha * (R + gamma * V[i1] - V[i])

    return V

TD0(lazy_problem)