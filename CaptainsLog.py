
from datetime import datetime
import subprocess
import os

#--------------------------------------------------------------------------------------------------------------------------- 
#                                                          EDIT THIS 
#---------------------------------------------------------------------------------------------------------------------------
# This is where all the powershell scripts are stored. (The Log_Script_Library folder)
location_of_powershell_scripts = "C:\\Users\\JamesTKirk\\OneDrive\\Codes\\PythonProjects\\CaptainsLog\\Log_Script_Library\\" 

# This is where all the log file will be stored. (You'll have to create this, wherever)
location_of_logs = "C:\\Users\\JamesTKirk\\OneDrive\\Logs\\"  

# Number of files stored/allowed in Log folder.
num_logs = 3
#---------------------------------------------------------------------------------------------------------------------------


def Powershell_exe(destination_of_script,destination_of_file):

    # This method can execute powershell scripts 
    # located in both .txt and .ps1 files
    # 
    # destination_of_script = where file containing the script is located
    # destination_of_file = in which file to return output 

    script = open(destination_of_script , "r") 
    p1 = subprocess.run(["powershell.exe", script.read()], capture_output=True, text=True)
    return destination_of_file.write(p1.stdout)   

def Script_Runner(script_folder_loction, output_file_location):
    
    # This method iterates through the script folder. 
    # It then uses the Powershell_exe() method to execute each file.

    # script_folder_loction = Location where all powershell scripts are stored.
    # output_file_location = The location of the log file.

    for filename in os.listdir(script_folder_loction):
        if filename.endswith(".txt") or filename.endswith(".ps1"): 
            
            # scrit = path to a script file
            script = os.path.join(script_folder_loction, filename)
            
            # The Powershell_exe() method is now used to execute te "script" file.
            Powershell_exe(script,output_file_location)

            continue
        else:
            continue

def Maintainer(file_name,num_of_files):

    # This method is used to calculate the amount of files in a folder. 
    # And remove the oldest files if there are to many.

    # file_name = Name of folder containing the files.
    # num_of_files = Number of files allowed in folder.

    while True:

        file_count = sum([len(files) for r, d, files in os.walk(file_name)]) #Counts number of files in folder

        if file_count > num_of_files:
            
            # The following code is used to determin the oldest file in the folder
            path = file_name
            os.chdir(path)
            files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

            oldest_file = files[0]
            # newest_file = files[-1]

            os.remove(oldest_file) # Removes oldest file

        else:
            break

def CaptainsLog(script_file_name, log_file_name, num_of_files): 

    # script_file_name = This is where all the powershell scripts are stored.
    # log_file_name = Name of folder containing the files and its path. 
    # num_of_files = Number of files allowed in log folder.
    

    stardate = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    stardate1 = str(stardate) + ".txt"
    file = open(log_file_name + stardate1, "w")


    file.write("##############################\n")
    file.write("         Captains Log\n")
    file.write("Stardate: " + stardate + "\n")
    file.write("##############################\n")

    Script_Runner(script_file_name, file)
    
    file.write("\nLive long, and prosper\n")
    
    # This method is used to calculate the amount of log files in a folder. 
    # And remove the oldest files if there are to many.
    Maintainer(log_file_name, num_of_files)


CaptainsLog(location_of_powershell_scripts, location_of_logs, num_logs)



