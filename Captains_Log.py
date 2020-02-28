
from datetime import datetime
import subprocess
import os

location_of_powershell_scripts = "C:\\Users\\JamesTKirk\\OneDrive\\Codes\\PythonProjects\\CaptainsLog\\Log_Script_Library\\" # This is where all the powershell scripts are stored.
location_of_logs = "C:\\Users\\JamesTKirk\\OneDrive\\Logs\\"  # This is where the log file will be stored.
num_logs = 30 # Number of files stored in Log folder.


def powershell_exe(destination_of_script,destination_of_file):

    # This method can execute powershell scripts 
    # located in both .txt and .ps1 files
    # 
    # destination_of_script = where file containing the script is located
    # destination_of_file = in which file to return output 

    script = open(destination_of_script , "r") 
    p1 = subprocess.run(["powershell.exe", script.read()], capture_output=True, text=True)
    return destination_of_file.write(p1.stdout)   

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

    powershell_exe(location_of_powershell_scripts + "User_DomainName.txt",file)
    powershell_exe(location_of_powershell_scripts + "System_Info_Full.txt",file)
    powershell_exe(location_of_powershell_scripts + "Disk_Info.txt",file)
    powershell_exe(location_of_powershell_scripts + "Battery_%.txt",file)
    powershell_exe(location_of_powershell_scripts + "Arp_Table.txt",file)
    powershell_exe(location_of_powershell_scripts + "GPU_Info.txt",file)
    powershell_exe(location_of_powershell_scripts + "Ipconfig_All.txt",file)
    powershell_exe(location_of_powershell_scripts + "Wifi_Info.txt",file)
    powershell_exe(location_of_powershell_scripts + "Location.txt",file)
    powershell_exe(location_of_powershell_scripts + "Downloaded_Files.txt",file)
    powershell_exe(location_of_powershell_scripts + "DNS_Cache.txt",file)
    powershell_exe(location_of_powershell_scripts + "Powershell_Command_History.txt",file)
    powershell_exe(location_of_powershell_scripts + "Event_Log(100).txt",file)

    Maintainer(log_file_name, num_of_files) # This method is used to calculate the amount of log files in a folder. 
    # And remove the oldest files if there are to many.

    file.write("\nLive long, and prosper")

CaptainsLog(location_of_powershell_scripts, location_of_logs, num_logs)



