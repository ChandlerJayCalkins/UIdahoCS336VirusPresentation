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
			inflines.append("\n")
			inflines.append("# THIS FILE HAS BEEN INFECTED\n")
			inflines.append("\n")

			# copy over the rest of the file
			inflines.extend(flines)

			# write the lines from the file back into itself with the virus code injected
			with open(infpath, "w") as inf:
				for s in inflines:
					inf.write(s)