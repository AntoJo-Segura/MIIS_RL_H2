from matplotlib.pyplot import *
from problem import *
from temporal_difference import *

for exp in [4,5,6]:
    V_lazy = TD0(lazy_problem, 10**exp)
    plot(V_lazy,'go-')
    # savefig('V_TD0_1e'+str(exp)+'_lazy.png')
    show()

for exp in [4,5,6]:
    V_agg = TD0(agg_problem, 10**exp)
    plot(V_agg,'go-')
    # savefig('V_TD0_1e'+str(exp)+'_agg.png')
    show()
