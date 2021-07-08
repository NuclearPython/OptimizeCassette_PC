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
list = run_on_cluster('mymcnpfile.inp')
print("Submitted",len(list),solver,"jobs")
