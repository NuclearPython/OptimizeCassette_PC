#for testing the genration of a usable MCNP file
#from a Mcok MCNP file using Chris' provided functions

#also testing some of the functions in WorkingWithMCNPUtilities
from functions import program_gen
import numpy as np
from WorkingWithMCNPUtilities import modifyRunFile, runMCNPfile, RunACassette
testBasics = 0
if testBasics == 1:
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
    #test the modification of the run file
    numberID = 3
    newPath = modifyRunFile(proposedFilename, numberID)
    #test the runfile creation, movement, and execution
    numberID = 4
    newPath4 = modifyRunFile(proposedFilename, numberID)
    output = runMCNPfile(proposedFilename, numberID)
else:
    feature_vector = np.array([1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2])
    evalNumber = 1
    output = RunACassette(feature_vector, evalNumber)
    print(output)