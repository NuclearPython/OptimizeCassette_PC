#this program is meant to develop  the ability of python to 
# run a specified MCNP file on Alex's Computer
# assumes run.bat is in the same file folder
#and that it's file paths are correct

from subprocess import Popen
import os
import fileinput
import shutil
from functions import program_gen
from translate_feature_vector import translate_feature_vector
import numpy as np
import MCNP_File_Handler
import getResults

run_program_file_location = r"C:\Users\depila\Desktop\Graduate Research\Optimization\OptimizeCassette\run.bat"
program_file_location = "C:\\Users\\depila\\Desktop\\Graduate Research\\Optimization\\OptimizeCassette\\"
program_file_location2 = "C:\\Users\\depila\\Desktop\\Graduate Research\\Optimization\\OptimizeCassette"
#MCNP_data_location = r"C:\Users\depila\fullmcnp\MCNP_DATA\"
#MCNP_exe_location = r":\Users\depila\fullmcnp\MCNP_CODE\bin\mcnp6.exe"

def runMCNPfile(MCNP_filename, numberID):
    #function to run a specified MCNP file inside the sub directory specified by its ID
    #STEP 1: Specify the path of the MCNP file
    MCNP_file_location = program_file_location + str(numberID)+"\\"+MCNP_filename
    #STEP 2: Specify the path of the run program
    specific_run_program_file_location = '"'+program_file_location+str(numberID)+"\\run"+str(numberID)+".bat"+'"'
    os.chdir(program_file_location+str(numberID))

    os.system(specific_run_program_file_location)
    os.chdir(program_file_location2)
    output = "done"
    return output

def modifyRunFile(proposedfileName, numberID):
    #this function is meant to modify run.bat so that it references an new 
    #MCNP file in a directy and generates its results in that directory
    #this function also moves the specified MCNP file to that directory

    #STEP 1: create the directory
    directory = str(numberID)
    parent_dir = program_file_location
    # Path 
    path = os.path.join(parent_dir, directory)
    os.mkdir(path) 
    print("Directory '% s' created" % directory)

    #setup
    runfile = "run.bat"
    modified_run_file ="run"+str(numberID)+".bat" 
    #STEP 2: modify the run file
    with open(runfile) as f:
        with open(modified_run_file, "w") as f1:
            for line in f:
                f1.write(line)
        f1.close()
    f.close()
    with fileinput.FileInput(modified_run_file, inplace=True) as file:
        for line in file:
            print(line.replace("fileToBeRun.inp",proposedfileName ), end='')
    file.close()
    
    #STEP 3: Place modified run file in the new directory
    new_path = shutil.move(modified_run_file, str(numberID))

    #STEP 4: move the MCNP file to the directory
    new_path = new_path = shutil.move(proposedfileName, str(numberID))
    return new_path

def RunACassette(feature_vector, evalNumber):
    variableNames, variableValues = translate_feature_vector(feature_vector)
    #specify files
    MockMCNPfilename = 'JohnMockCassette.inp'
    proposedFilename = 'TestMCNPFile'+str(evalNumber)+'.inp'
    #generate the MCNP file
    filename = program_gen(proposedFilename,MockMCNPfilename,variableValues,variableNames)
    #put the run file and MCNP file in the correct location
    newfilePath = modifyRunFile(proposedFilename, evalNumber)
    #run the MCNP file
    output2 = runMCNPfile(proposedFilename, evalNumber)
    #os.system('u')
    print("Done running MCNP")
    keff = getResults.getResults(evalNumber)
    return keff