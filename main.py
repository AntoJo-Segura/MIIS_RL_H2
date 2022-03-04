from matplotlib.pyplot import *
from problem import *
from temporal_difference import *

colors = ['red', 'green', 'blue', 'violet']

#TD0

def get_plots_A(ax, V_problem, title, trans, index):
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
        get_plots_A(ax,V_lazy,'Lazy',10**exp, i)

    fig.savefig('V_TD0_lazy.png')

    fig, ax = subplots()
    for i,exp in enumerate(exponent):
        V_lazy = TD0(agg_problem, 10**exp)
        get_plots_A(ax,V_lazy,'Aggressive',10**exp, i)

    fig.savefig('V_TD0_agg.png')

#LSTD

def get_plots_B(ax, V_problem, title, fm, trans,index):
    ax.set_xlabel('State')
    ax.set_ylabel('V (s)')
    ax.set_title(title+ ' trans = '+str(int(trans)), fontsize=24, loc="center", pad=10)
    ax.scatter(
        range(0, len(V_problem)), V_problem, 
        marker='.', color=colors[index], 
        label='Feature map : '+ fm
    )
    ax.legend()
    return ax

def solution_1B():
    f_map_list = [f_map_fine,f_map_coarse, f_map_pwl]
    f_map_name =['Fine','Coarse', 'PWL']
    trans = 1e5
    
    fig, ax = subplots()
    for i, f_map in enumerate(f_map_list):
        V_lazy = LSTD(lazy_problem,f_map, trans)
        get_plots_B(ax,V_lazy,'Lazy',f_map_name[i], trans,i)

    fig.savefig('V_LSTD_lazy.png')

    fig, ax = subplots()
    for i, f_map in enumerate(f_map_list):
        V_agg = LSTD(agg_problem,f_map, trans)
        get_plots_B(ax,V_agg,'Aggressive',f_map_name[i], trans,i)

    fig.savefig('V_LSTD_agg.png')


if __name__ == '__main__':
    solution_1A()
    solution_1B()