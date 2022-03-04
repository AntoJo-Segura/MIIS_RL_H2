from matplotlib.pyplot import *
from problem import *
from temporal_difference import *

colors = ['red', 'green', 'blue', 'violet']
def get_plots(ax, V_problem, title, trans, index):
    ax.set_xlabel('State')
    ax.set_ylabel('V (s)')
    ax.set_title(title, fontsize=24, loc="center", pad=10)
    ax.scatter(
        range(0, len(V_problem)), V_problem, 
        marker='.', color=colors[index], 
        label='trans = '+str(trans)
    )
    ax.legend()
    return ax

def solution_1A():

    exponent = [4,5,6,7]
    fig, ax = subplots()
    for i,exp in enumerate(exponent):
        V_lazy = TD0(lazy_problem, 10**exp)
        get_plots(ax,V_lazy,'Lazy',10**exp, i)

    fig.savefig('V_TD0_lazy.png')

    fig, ax = subplots()
    for i,exp in enumerate(exponent):
        V_lazy = TD0(agg_problem, 10**exp)
        get_plots(ax,V_lazy,'Aggresive',10**exp, i)

    fig.savefig('V_TD0_agg.png')

solution_1A()

def solution_1B():
    f_map_list = [f_map_fine,f_map_coarse, f_map_pwl]
    f_map_name =['Fine','Coarse', 'PWL']

    for i, f_map in enumerate(f_map_list):
        V_lazy = LSTD(lazy_problem,f_map_fine, 1e5)
        print(f_map_name[i])
        plot(V_lazy,'go-',label='Feature map: '+ f_map_name[i])
        # savefig('V_TSTD_'+f_map_name[i]+'_lazy.png')
        show()

    for i, f_map in enumerate(f_map_list):  
        V_agg = LSTD(agg_problem,f_map, 1e5)
        plot(V_agg,'go-',label='Feature map: '+ f_map_name[i])
        # savefig('V_TSTD_'+f_map_name[i]+'_lazy.png')
        show()

# solution_1B()