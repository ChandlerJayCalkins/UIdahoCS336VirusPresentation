import discord
import random

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
# bot won't run unless you put the token in here
token = ''

# called as soon as the bot is fully online and operational
@client.event
async def on_ready():
	print("Bot is ready")

# plays rock paper scissors with users
@client.event
async def on_message(message):
	if (message.content.startswith("!rps ")):
		words = message.content.split()
		if (len(words) > 1):
			player_choice = words[1].lower()
			if (words[1].lower() == "rock" or words[1].lower() == "paper" or words[1].lower() == "scissors"):
				rand_choice = random.randrange(0, 3)

				if (rand_choice == 0):
					rand_choice = "Rock"
				elif (rand_choice == 1):
					rand_choice = "Paper"
				elif (rand_choice == 2):
					rand_choice = "Scissors"
				else:
					rand_choice = "Error"

				result = ""
				if (player_choice == rand_choice.lower()):
					result = "It's a tie!"
				elif (player_choice == "rock" and rand_choice == "Scissors") or (player_choice == "paper" and rand_choice == "Rock") or (player_choice == "scissors" and rand_choice == "Paper"):
					result = "You win!"
				elif (player_choice == "rock" and rand_choice == "Paper") or (player_choice == "paper" and rand_choice == "Scissors") or (player_choice == "scissors" and rand_choice == "Rock"):
					result = "You lost"

				if (rand_choice == "Rock" or rand_choice == "Paper" or rand_choice == "Scissors"):
					await message.channel.send(f"{rand_choice}: {result}")
				else:
					await message.channel.send("Error with the bot's randomization")
			else:
				await message.channel.send("Incorrect command usage, must type either rock, paper, or scissors after !rps")

client.run(token)