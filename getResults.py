# an example of a user supplied file for getting results from the MCNP output

#in this case it is returning the keff
import numpy as np
#from MCNP_file_Handler import mcnp_file_handler
import MCNP_File_Handler
import shutil

testHandler =  MCNP_File_Handler.mcnp_file_handler()

program_file_location = "C:\\Users\\depila\\Desktop\\Graduate Research\\Optimization\\OptimizeCassette\\"
def getResults(numberID):
    outputNumber = numberID

    source = program_file_location+str(outputNumber)+"\\outp"
    destination = program_file_location + "output\\output"+str(outputNumber)+ ".inpo"

    shutil.copy(source, destination)
    output_file_string = destination
    keff = testHandler.get_keff(output_file_string)
    return keff