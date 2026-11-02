import numpy as np
from scipy.optimize import minimize

# x[0] = concentration of A (mol/m^3)
# x[1] = reactor time constant (s)
k = 1.5

def adjusted_ep(x):
    return x[0] + 0.5 * x[1]

# SLSQP inequality constraints must be >= 0.
def pfr_constraint(x):
    return x[0] - np.exp(-k * x[1])

def cstr_constraint(x):
    return 1 / (1 + k * x[1]) - x[0]

constraints = [
    {'type': 'ineq', 'fun': pfr_constraint},
    {'type': 'ineq', 'fun': cstr_constraint},
]

# Bounds on concentration and reactor time constant.
bounds = [(0, 1), (0, 1)]
initial_guess = [0.6, 0.5]

res = minimize(
    adjusted_ep,
    initial_guess,
    method='SLSQP',
    bounds=bounds,
    constraints=constraints,
    options={'ftol': 1e-12, 'maxiter': 1000},
)

print('Optimization successful:', res.success)
print(f'Minimum adjusted EP: {res.fun:.6f}')
print(f'Optimal concentration C_A: {res.x[0]:.6f} mol/m^3')
print(f'Optimal time constant tau: {res.x[1]:.6f} s')
