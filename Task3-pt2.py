import numpy as np
import matplotlib.pyplot as plt

def read_matrix(filename):                          # Reads a matrix from a text file.

    matrix = []
    with open(filename, "r") as file:

        for line in file:                           # Assuming space-separated values
            row = [float(value) for value in line.split()]
            matrix.append(row)

    return np.array(matrix)                         # Outputs a numpy matrix


def normalize(v):
    return v/np.sum(v)

n = 3
m = 300

A = np.array([[0, -1, 2],
              [3, 0, -4],
              [-5, 6, 0]])

x = np.array([5, 3, 2])
y = np.array([6, 3, 7])
x = normalize(x)
y = normalize(y)


payoff_avg = y.dot(x.dot(A.T))

x_choice = np.random.choice(list(range(n)), m, p=x)
y_choice = np.random.choice(list(range(n)), m, p=y)

payoff = np.array([])
for i in range(m):
    payoff = np.append(payoff, A[y_choice[i]][x_choice[i]])

payoff_sum = np.cumsum(payoff)
for i in range(m):
    payoff_sum[i] = payoff_sum[i]/(i+1.0)

plt.figure(figsize=(8, 6))  # Set plot size
plt.plot(range(m), payoff_sum, marker='.', linestyle='-')
plt.axhline(y=payoff_avg, color='r', linestyle='-.', label='Expected Payoff')
plt.xlabel("Iteration No.")
plt.ylabel("Cumulative Average Payoff")
plt.title("Payoff of the Matrix Game")
plt.grid(True)

plt.show()