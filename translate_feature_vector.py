import numpy as np
def translate_feature_vector(feature_vector):
    #set material properties
    density1 = 0.93
    density2 = 18.94
    density3 = 0.971
    densVec = np.array([density1, density2, density3])
    materials = feature_vector
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
        variableValues[i] = densVec[int(round(materials[i-20]-1))]
    ValueString = []
    for i in range(0,20):
        ValueString.append(str(int(round(variableValues[i]))))
    for i in range(20,40):
        ValueString.append(str(variableValues[i]))

    return names, ValueString
