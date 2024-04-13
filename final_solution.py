#module used
from pulp import *
import pickle
#------------------------------------------------------------------------------------------------------

def read_matrix(filename):
    output = []
    with open(filename, 'rb') as file:
        while True:
            try:
                f = pickle.load(file)
                output.append(f)
            except:
                break

    return output

#-------------------------------------------------------------------------------------------------------
all_mat = read_matrix("mybinary.dat")
for A in all_mat:

    AT=[[A[0][i],A[1][i],A[2][i]] for i in range(len(A))]    #exmaple transpose matrix

    #-------------------------------------------------------------------------------------------------------
    x = []           #values of x
    y = []           #values of y


    # I shall assume the matrix is of size 3 x 3
    n = len(A[0])

    # Need to maximise w such that (we <= Ax) & (x[i] >= 0) & (sum(x[i]) = 1)
    #for x
    model_x = LpProblem("MatrixGame", sense=LpMaximize)

    #for y
    model_y = LpProblem("MatrixGame", sense=LpMaximize)

    #---------------------------------------------------------------------------------------------------------
    # Decision variables
    for i in range(n):
        #for x 
        x.append(i)
        x[i] = LpVariable("x_"+str(i), 0, None, LpContinuous)

        #for y
        y.append(i)
        y[i] = LpVariable("y_"+str(i), 0, None, LpContinuous)   


    w = LpVariable("Payoff", None, None, LpContinuous)


    # Constraints

    for i in range(len(A)):
        #for x
        model_x += LpAffineExpression([(x[j],A[i][j]) for j in range(n)]) >= w

        #for y
        model_y += LpAffineExpression([(y[j],AT[i][j]) for j in range(n)]) >= w


    #for x
    model_x += LpAffineExpression([(x[j],1) for j in range(n)]) == 1

    #for y
    model_y += LpAffineExpression([(y[j],1) for j in range(n)]) == 1


    # Objective function

    model_x += w
    model_y += w

    #---------------------------------------------------------------------------------------------------------

    # Solve the model, and silence the logging

    model_x.solve(PULP_CBC_CMD(msg=False))
    model_y.solve(PULP_CBC_CMD(msg=False))


    #----------------------------------------------------------------------------------------------------------
    #output of solution

    print("MATRIX:")
    f = [print(i) for i in A]
    print("")
    for v in model_x.variables():
        print(v.name, "=", v.varValue)
    print("")
    for v in model_y.variables():
        print(v.name, "=", v.varValue)
    print("-----------------------------------------------")
    print("")