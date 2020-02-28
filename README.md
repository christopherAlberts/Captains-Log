# CaptainsLog
Awsome daily system logger!!!

![](Image/CaptainsLogLogo.png)

**_Space: the final frontier. These are the voyages of the starship Enterprise..._** 

This is a cool lightweight daily systems loger. Find out what is really happening inside your PC!

## Wanna Try It Out, It's only logical? ##

Just follow these few steps to set up your own personal logger:

1. Click on the big green button in the right hand conner, that says **Clone or download**. And select **Download Zip**.
2. Once the Zip file has downloaded, exstract the folder and search for a file called **_Captains_Log.py_**. 
*So this file is the heart and soul of this program, so whatever you do don't lose it, ok!*
3. You'll need to edit the following 3 variables in this file accordingly. Do this with any text editor of your choosing. Make sure that each variable reference where that file is stored on your own system. 

```python
# This is where all the powershell scripts are stored. (The Log_Script_Library folder)
location_of_powershell_scripts = "C:\\Users\\JamesTKirk\\OneDrive\\Codes\\PythonProjects\\CaptainsLog\\Log_Script_Library\\" 

# This is where all the log file will be stored. (You'll have to create this, wherever)
location_of_logs = "C:\\Users\\JamesTKirk\\OneDrive\\Logs\\"  

# Number of files stored/allowed in Log folder.
num_logs = 30 
```
*If you can get through this without to much crying, we've got a good change of makeing it to the end of this tutorial.*

4. Once the variables are edited correctly, all thats left is for us to make the **_Captains_Log.py_** an executable. The following link describes how to do this: https://www.pyinstaller.org/

5. You can now take the new **_Captains_Log.exe_** and put it in your systems startup file. This will ensure that each time your computer boots up, the program will be execute and generate a log, which will be placed in the log file. To open the startup folder, bring up the Run box, type in **shell:common startup** and hit Enter. 

## How It Works: ##

The *Log_Script_Library* folder, contains a number of Powershell scripts. Each of these scripts pulls a diffrent piece of information form the system. If you have a cool script that you'd like to log, feel free to add it to this file.

## The Output, Baby! ##

I'll leave this for you to discover...








