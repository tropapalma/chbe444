
import math
import chbe444umd as des
import IPython.display as ipd

s = 0.3  # Shading opacity

# Optimal values
k = 1.5
optimal_tau = math.log(3) / k
optimal_CA = 1 / 3
optimal_z = optimal_CA + 0.5 * optimal_tau

# x = C_A and y = tau
expressions = [
    {'latex': 'x_1 = x', 'hidden': 'true'},
    {'latex': 'x_2 = y', 'hidden': 'true'},

    # Objective function
    {'latex': 'x_1 + 0.5 x_2 = z',
     'id': 'obj',
     'color': '#000000'},

    # Shade outside the PFR boundary
    {'latex': 'x_1 < \\\\exp(-1.5 x_2)',
     'id': 'pfr',
     'fillOpacity': s,
     'color': '#f7d9c4'},

    # Shade outside the CSTR boundary
    {'latex': 'x_1 > 1/(1 + 1.5 x_2)',
     'id': 'cstr',
     'fillOpacity': s,
     'color': '#f7d9c4'},

    # Upper bound on tau
    {'latex': 'x_2 > 1',
     'id': 'tau_upper',
     'fillOpacity': s,
     'color': '#f7d9c4'},

    # Nonnegative concentration
    {'latex': 'x_1 < 0',
     'id': 'ca_lower',
     'fillOpacity': s,
     'color': '#f7d9c4'},

    # Nonnegative time constant
    {'latex': 'x_2 < 0',
     'id': 'tau_lower',
     'fillOpacity': s,
     'color': '#f7d9c4'}
]

# Objective function slider
sliders = [
    {'variable': 'z',
     'min': '0',
     'max': '2',
     'step': '0.001'}
]

# Optimal point
points = [
    {'latex': f'({optimal_CA:.6f},{optimal_tau:.6f})',
     'color': '#000000',
     'label': 'optimum',
     'showLabel': True}
]

# Generate Desmos graph
graph_html = des.desmos_graph(
    expressions=expressions,
    sliders=sliders,
    points=points,
    axlim=[-0.2, 1.5, -0.2, 1.5],
    size=[1000, 600]
)

# Save graph as HTML
with open('reactor_nlp_graph.html', 'w', encoding='utf-8') as f:
    f.write(graph_html.get_value())

# Display graph in Jupyter
ipd.display(
    ipd.IFrame(
        'reactor_nlp_graph.html',
        width='100%',
        height=600
    )
)

# Print optimal results
print(f'Optimal C_A = {optimal_CA:.6f} mol/m^3')
print(f'Optimal tau = {optimal_tau:.6f} s')
print(f'Minimum adjusted EP = {optimal_z:.6f}')
