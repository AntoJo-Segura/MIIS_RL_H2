import numpy as np


class policy():
    def __init__(self, action_f, prob_f):
        self.policy_p = prob_f
        self.policy = action_f

    def vec_to_f(self, vec_pol):
        def pol(state):
            return vec_pol[state]
        self.policy = pol

    def generate_p_f(self):
        def prob(action, state):
            if self.policy(state) == action:
                return 1
            else:
                return 0
        
        self.policy_p = prob


class problem():
    def __init__(self, pol : policy, N = 100):
        self.N = N
        self.actions = ["low", "high"] 
        self.state_space = range(0, N)
        self.gamma = 0.9
        self.arrival_p = 0.5
        self.policy = pol.policy
        self.policy_p = pol.policy_p

    def trunc(self,s): 
        return min(self.N-1,max(s,0))

    def next_state(self, s,a):
        It = 0
        if np.random.rand() < self.arrival_p :
            It = 1
        St = 0
        if np.random.rand() < self.rate(a):
            St = 1

        return self.trunc(s+ It - St)

    def reward(self,s,a):
        if a == "low" :
            c = 0.0
        else:
            c = 0.01

        return -pow(s/self.N,2)-c
    
    def rate(self, a):
        if a == "low" :
            q = 0.51
        else:
            q = 0.6
        return q


    def transition_p(self,new_s,action,s):
        diff = new_s - s 
        not_arrival_p = 1 - self.arrival_p
        depart_p = self.rate(action)
        not_depart_p = 1 - depart_p

        if diff > 1 or diff < -1:
            return 0

        if diff == 1:
            return self.arrival_p * not_depart_p
        
        if diff == 0:
            return not_arrival_p * not_depart_p + self.arrival_p * depart_p

        if diff == -1:
            return not_arrival_p * depart_p




class matrix_problem(problem):
    def __init__(self, pol: policy , N = 100):
        super().__init__(pol, N)

        self.reward_space = list(map(lambda x:
            self.reward(x, self.policy(x)),
            self.state_space
        ))
        self.transition_m = self.get_transition_matrix()
    
    def get_transition_matrix(self):
        P  =[[0]*len(self.state_space)]*len(self.state_space)
        for i,x in enumerate(self.state_space):
            for j,y in enumerate(self.state_space):
                P[i][j]= self.transition_p(x, self.policy(y), y)
        return P


###POLICY ######

def lazy_p(state):
    return "low"

def lazy_p_p(action, state):
    if action == "low":
        return 1 
    else :
        return 0


lazy_policy = policy(lazy_p, lazy_p_p)
lazy_problem = problem(lazy_policy)

def aggre_policy( state):
    if state < 50:
        return "low"
    else:
        return "high"

def aggre_policy_p( action, state):
    if state < 50 and action == "low" or state >= 50 and action == "high" :
        return 1
    else:
        return 0


agg_policy = policy(aggre_policy, aggre_policy_p)
agg_problem = problem(agg_policy)

###check vec_to_f#######
lazy_policy = policy(lazy_p, lazy_p_p)

lazy_policy.vec_to_f(["high"]*len(range(0,100)))
# print(type(lazy_policy.policy))#class function
# print(lazy_policy.policy(15) == "high")