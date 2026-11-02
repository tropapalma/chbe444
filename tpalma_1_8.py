import gamspy as gp
from gamspy import Container, Variable, Equation, Model, Sense, Problem

# Create GAMSPy container
m = Container()

# Decision variables
x2 = Variable(m, name="x2", type="Positive")
x3 = Variable(m, name="x3", type="Positive")

# Objective variable
z = Variable(m, name="z")

# Nonnegativity constraint for reaction x5
nonnegative_x5 = Equation(m, name="nonnegative_x5")
nonnegative_x5[...] = 3*x2 + x3 <= 2

# NADH balance constraint
NADH_balance = Equation(m, name="NADH_balance")
NADH_balance[...] = 7*x2 + 3*x3 >= 2

# Minimum succinate production constraint
minimum_succinate = Equation(m, name="minimum_succinate")
minimum_succinate[...] = x2 + x3 <= 1.5

# Objective function
objective = Equation(m, name="objective")
objective[...] = z == 2 - x2 - x3

# Define optimization model
lp = Model(
    m,
    name="Succinate_Optimization",
    equations=[
        nonnegative_x5,
        NADH_balance,
        minimum_succinate,
        objective
    ],
    problem=Problem.LP,
    sense=Sense.MAX,
    objective=z
)

# Solve LP
lp.solve()

# Optimal values
x1_opt = 1.0
x2_opt = x2.toValue()
x3_opt = x3.toValue()
x4_opt = x2_opt
x5_opt = 2 - 3*x2_opt - x3_opt

# Print results
print("Optimal succinate yield:", z.toValue())
print("Optimal x1:", x1_opt)
print("Optimal x2:", x2_opt)
print("Optimal x3:", x3_opt)
print("Optimal x4:", x4_opt)
print("Optimal x5:", x5_opt)
