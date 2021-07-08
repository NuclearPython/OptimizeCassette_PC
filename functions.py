import fileinput
import numpy as np
import pandas as pd
import time
from numpy import genfromtxt
import os


#This makes and replaces the file with variables inputs are the new file, mock
#variable names and values, the variable neames and values must be the same length
# also if there is an error make sure to check to make sure data is string
def program_gen(proposed_filename,mock_MCNP,var_values,var_names):
    time.sleep(1)
    with open(mock_MCNP) as f:
        with open(proposed_filename, "w") as f1:
            for line in f:
                f1.write(line)
        f1.close()
    f.close()
    # variable changer
    o=0
    for o in range(len(var_values)):
        with fileinput.FileInput(proposed_filename, inplace=True) as file:
            for line in file:
                print(line.replace(var_names[o], var_values[o]), end='')
        file.close()
    return proposed_filename


#varvalues = [str(1),str(2),str(3),str(5),str(-5)]
#varnames = []
#for i in range(len(varvalues)):
#    v= '<var'+str(i)+'>'
#    varnames.append(v)


#program_gen('Test.txt','readbase.txt',varvalues,varnames)   




######### new function this is the job submission thing
#need more info it is TBD going to learn more about and make sure it works as we need it to

#submitting MCNP6.2 jobs to necluster script
solver = 'mcnp' #defined differently if script can run multiple different programs
# boolean: Set True to submit jobs, False to just check how many jobs will be submitted
submit_jobs = True
cluster_input_string = """#!/bin/bash
#PBS -V
#PBS -q fill
#PBS -l nodes=1:ppn=8

hostname
module load MCNP6/2.0

RTP="/tmp/runtp--".`date "+%R%N"`
cd $PBS_O_WORKDIR
mcnp6 TASKS 8 name=%%%INPUT%%% runtpe=$RTP
grep -a "final result" %%%INPUT%%%o > %%%INPUT%%%_done.dat
rm $RTP"""

def run_on_cluster(common_string):
    list_of_jobs_submitted = []

    for file in os.listdir('.'):
        # Checking if file ends in ".inp" and if the flag is in the filename
        if file.endswith(".inp") == False:
            continue
        if common_string not in file:
            continue
        print("Creating cluster script for  MCNP job: " + file)

        script_string = cluster_input_string
        script_string = script_string.replace("%%%INPUT%%%", file)
        script_file_string = file + "_script.txt"
        script_file = open(script_file_string, 'w')
        script_file.write(script_string)
        script_file.close()

        print("Submitting MCNP job: " + file)
        list_of_jobs_submitted.append(file)

        if submit_jobs == True:
            # This line actually submits the job
            os.system('qsub ' + script_file_string)
    return list_of_jobs_submitted
#list = run_on_cluster('mymcnpfile.inp')
#print("Submitted",len(list),solver,"jobs")   





# This searches an output file for a specific string and returns that line
# check the end result, it returns the lines with total tallies and uncertainties
# if your string doesn't match it returns a blank list  
def get_results(file_name, string_to_search):
    """ Check if any line in the file contains given string """
    # Open the file in read only mode
    result = []
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if string_to_search in line:
                res = True, line
                result.append(res)
    return result

#q = get_results('child0.txt','      total      ')
