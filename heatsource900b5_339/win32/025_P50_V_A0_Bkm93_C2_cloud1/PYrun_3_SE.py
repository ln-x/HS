"""DO NOT DELETE THIS FILE. This script imports the heatsource module and executes the setup routines.
This script must be located in the same directory as HeatSource_control.csv. NOTE that executing this script
from Python shell (IDLE) will not identify __file__ correctly and will result in an error. It must be executed
from command line in windows or terminal in OSX. Your options are to run it manually from there, or you can double click on
HS_Setup.py. Kind of a hack implementation but we're still in beta so whateva. ;) """

from heatsource900 import BigRedButton
from os.path import dirname, exists, join, realpath

def getScriptPath():
    """Gets the path to the directory where the script is being executed from."""
    return dirname(realpath(__file__))

inputdir = getScriptPath() + '/'
control_file = 'HeatSource_Control.csv'

if exists(join(inputdir,control_file)) == False:
	raise Exception("HeatSource_Control.csv not found. Move the executable or place the control file in this directory: %s." % inputdir)

# Run Heat Source Temperature, run_type = 0
#BigRedButton.RunHS(inputdir,control_file)

# Run Heat Source Solar only, run_type = 1
#BigRedButton.RunSH(inputdir,control_file)

# Run Heat Source Hydraulics only, run_type = 2
#BigRedButton.RunHY(inputdir,control_file)

# Run Setup, run_type = 3
BigRedButton.RunSetup(inputdir,control_file)


