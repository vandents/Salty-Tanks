"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Instructor: Prof. Brian Drake
Course: MTH 302-02
Program: Project 3 - Salty Tanks

@date Friday, April 17, 2020
@author Scott VandenToorn
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as LA
import math as m


# ---------------------------------------------------------------------------
#  Functions
# ---------------------------------------------------------------------------

def x1(t):
  return 6237 * m.exp(-0.0073 * t) * -0.878 + 5251 * m.exp(-0.0567 * t) * -0.424 + 10302 * m.exp(-0.181 * t) * -0.223 + 10000

def x2(t):
  return 6237 * m.exp(-0.0073 * t) * 0.649 + 5251 * m.exp(-0.0567 * t) * -0.593 + 10302 * m.exp(-0.181 * t) * -0.477 + 4000

def x3(t):
  return 6237 * m.exp(-0.0073 * t) * -0.276 + 5251 * m.exp(-0.0567 * t) * -0.367 + 10302 * m.exp(-0.181 * t) * 0.888 + 2000


# ---------------------------------------------------------------------------
#  Driver code
# ---------------------------------------------------------------------------

# Find eigenvalues and eigenvectors
A = np.array([
  [ -10 / 500,   0,           5 / 100   ],
  [ 10 / 500,    -15 / 200,   5 / 100   ],
  [ 0,           15 / 200,    -15 / 100 ]
])

eigenvalues, v = LA.eig(A)
print('\n\n', np.around(eigenvalues, 4), '\n\n')
print(np.around(v, 3), '\n\n')

# Find equalibrium solution
B = Matrix([
  [ -10 / 500,   0,           5 / 100,     -100 ],
  [ 10 / 500,    -15 / 200,   5 / 100,     0    ],
  [ 0,           15 / 200,    -15 / 100,   0    ]
])

print("RREF and pivot columns: {}\n\n".format(B.rref()))

# Plot salts
salt_x1 = []
salt_x2 = []
salt_x3 = []

for t in range(500):
  salt_x1.append(x1(t))
  salt_x2.append(x2(t))
  salt_x3.append(x3(t))

plt.plot(salt_x1)
plt.plot(salt_x2)
plt.plot(salt_x3)
plt.title('Salt Content by Tank')
plt.xlabel('Time (days)')
plt.ylabel('Salt (g)')
plt.text(350, 7500, 'x1', verticalalignment = 'bottom', color = 'blue', fontsize = 10)
plt.text(350, 7000, 'x2', verticalalignment = 'bottom', color = 'orange', fontsize = 10)
plt.text(350, 6500, 'x3', verticalalignment = 'bottom', color = 'green', fontsize = 10)
plt.grid()
plt.show()
