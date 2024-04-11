from pulp import *


def read_matrix(filename):                          # Reads a matrix from a text file.

    matrix = []
    with open(filename, "r") as file:

        for line in file:                           # Assuming space-separated values
            row = [float(value) for value in line.split()]
            matrix.append(row)

    return matrix


A = [[0, -1, 2],
    [3, 0, -4],
    [-5, 6, 0]]
x = []


# I shall assume the matrix is of size 3 x 3
n = len(A[0])

# Need to maximise w such that (we <= Ax) & (x[i] >= 0) & (sum(x[i]) = 1)


model = LpProblem("MatrixGame", sense=LpMaximize)


# Decision variables

for i in range(n):
    x.append(i)
    x[i] = LpVariable("x_"+str(i), 0, None, LpContinuous)

w = LpVariable("Payoff", None, None, LpContinuous)


# Constraints

for i in range(len(A)):
    model += LpAffineExpression([(x[j],A[i][j]) for j in range(n)]) >= w

model += LpAffineExpression([(x[j],1) for j in range(n)]) == 1


# Objective function

model += w

# Solve the model, and silence the logging

model.solve(PULP_CBC_CMD(msg=False))


for v in model.variables():
    print(v.name, "=", v.varValue)