import sys
print(sys.path)
# Gnowee Modules
import GnoweeNSGAPython3
from GnoweeNSGAPython3 import Constraints
from GnoweeNSGAPython3 import GnoweeUtilities
from GnoweeNSGAPython3 import GnoweeHeuristics
from GnoweeNSGAPython3 import ObjectiveFunction
from GnoweeNSGAPython3 import OptiPlot
from GnoweeNSGAPython3 import Sampling
from GnoweeNSGAPython3 import Gnowee
from GnoweeNSGAPython3.ObjectiveFunction import ObjectiveFunction
from GnoweeNSGAPython3.Constraints import Constraint
from GnoweeNSGAPython3.GnoweeHeuristics import GnoweeHeuristics
import numpy as np
from GnoweeNSGAPython3.OptiPlot import plot_vars
import matplotlib.pyplot as plt
numCalls = 0
# User Function Module
import TestMCNPObjFunc
from TestMCNPObjFunc import keff_ObjectiveFunction

sz = 20
all_ints = ["i" for i in range(sz)]
LB = np.ones(sz)
UppB = 3*np.ones(sz)

# Select optimization problem type and associated parameters
gh = GnoweeHeuristics(objective=ObjectiveFunction(keff_ObjectiveFunction),
                      lowerBounds=LB, upperBounds=UppB,
                      varType=all_ints, optimum=0, maxFevals = 300)
print(gh)

# Run optimization
(timeline) = Gnowee.main(gh)

length = len(timeline)
fitnesses = np.zeros(length)
generations = np.zeros(length)
for i in range(0,length):
    t = timeline[i]
    fitnesses[i] = t.fitness
    generations[i] = t.generation

plt.plot(generations, fitnesses, '-r', lw=2) # plot the data as a line
plt.xlabel('Generation', fontsize=14) # label x axis
plt.ylabel('Fittness', fontsize=14) # label y axis
plt.gca().grid() # add grid lines
plt.show() # display the plot
print('\nThe result:\n', timeline[-1])