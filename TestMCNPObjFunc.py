#this is a function meant for testing and development purposes
#specifically, this file is meant to be used to test the capability
#of the program to use the keff results of a MCNP file as an objective 
#function output
import WorkingWithMCNPUtilities
evaluationNumber = 0

def keff_ObjectiveFunction(material_Vector):
    global evaluationNumber
    evaluationNumber = evaluationNumber +1
    keff = WorkingWithMCNPUtilities.RunACassette(material_Vector, evaluationNumber)
    return 1-float(keff) #because Gnowee minimizes the objective function