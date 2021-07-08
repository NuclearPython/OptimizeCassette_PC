#for testing the genration of a usable MCNP file
#from a Mcok MCNP file using Chris' provided functions
from functions import program_gen
import numpy as np

#set material properties
density1 = 0.93
density2 = 18.94
density3 = 0.971
densVec = np.array([density1, density2, density3])
#set material vector
materials = np.array([1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2])

#specify the variable names
names = []
for i in range(0,20):
    names.append("<mat"+str(i+1)+">")
for i in range(0,20):
    names.append("<dens"+str(i+1)+">")
#print(names)


#specify the variable values
variableValues = np.zeros(40)
for i in range(0,20):
    variableValues[i] = materials[i]
for i in range(20,40):
    variableValues[i] = densVec[materials[i-20]-1]
ValueString = []
for i in range(0,20):
    ValueString.append(str(int(round(variableValues[i]))))
for i in range(20,40):
    ValueString.append(str(variableValues[i]))
print("done")
#specify files
MockMCNPfilename = 'JohnMockCassette.inp'
proposedFilename = 'TestMCNPFile.inp'
#test the creation
filename = program_gen(proposedFilename,MockMCNPfilename,ValueString,names)

#test the running


