from matplotlib.pyplot import *
from problem import *
from temporal_difference import *


### 1 A ###
# exponent = [4,5,6,7]
# for exp in exponent:
#     V_lazy = TD0(lazy_problem, 10**exp)
#     plot(V_lazy,'go-')
#     # savefig('V_TD0_1e'+str(exp)+'_lazy.png')
#     show()

# for exp in exponent:
#     V_agg = TD0(agg_problem, 10**exp)
#     plot(V_agg,'go-')
#     # savefig('V_TD0_1e'+str(exp)+'_agg.png')
#     show()

### 1 B ###
f_map_list = [f_map_fine,f_map_coarse, f_map_pwl]
f_map_name =['f_map_fine','f_map_coarse', 'f_map_pwl']

for i, f_map in enumerate(f_map_list):
    V_lazy = LSTD(lazy_problem,f_map_fine, 1e5)
    print(f_map_name[i])
    plot(V_lazy,'go-')
    # savefig('V_TSTD_'+f_map_name[i]+'_lazy.png')
    show()

for i, f_map in enumerate(f_map_list):  
    V_agg = LSTD(agg_problem,f_map, 1e5)
    plot(V_agg,'go-')
    # savefig('V_TSTD_'+f_map_name[i]+'_lazy.png')
    show()