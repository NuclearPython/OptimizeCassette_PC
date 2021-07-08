# this file is meant for the development and testing of the program's
# capabilities to read the results in their respective files
 
import numpy as np
#from MCNP_file_Handler import mcnp_file_handler
import MCNP_File_Handler
import shutil

testHandler =  MCNP_File_Handler.mcnp_file_handler()

program_file_location = "C:\\Users\\depila\\Desktop\\Graduate Research\\Optimization\\OptimizeCassette\\"
outputNumber = 1

source = program_file_location+str(outputNumber)+"\\outp"
destination = program_file_location + "output\\output"+str(outputNumber)+ ".inpo"

shutil.copy(source, destination)

output_file_string = destination
keff = testHandler.get_keff(output_file_string)
print(keff)