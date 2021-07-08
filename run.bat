:: This script runs mcnp input files

::absolute location of mcnp executable files
set EXE=C:\Users\depila\fullmcnp\MCNP_CODE\bin\mcnp6.exe

:: absolute location of the cross-section directory
set DATAPATH=C:\Users\depila\fullmcnp\MCNP_DATA\

:: number of threads used for parallel execution
set NUM_THREADS=10

:: input file so long as from same directory
set INP=fileToBeRun.inp

::run mcnp executable
%EXE% inp=%INP% tasks %NUM_THREADS%


