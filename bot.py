import discord

token = ""
prefix = '!'
client = discord.Client()
silenced = 0

#returns if the person using the command is allowed to or not
def hasPermission(userID):
    return userID == 224746044502704130 or userID == 215296706131001345 or userID == 161216398159380480 or userID == 181713957248172032

@client.event
async def on_message(message):
    global silenced
    words = message.content.split()

    index = 0
    while index < len(words):
        #redacts message from person who had silence command used on them
        if message.author.id == silenced:
            await message.delete()
            await message.channel.send("[REDACTED]")
        #redacts uwu
        elif words[index].lower() == "uwu":
            await message.delete()
            await message.channel.send("[REDACTED]")
        #redacts owo
        elif words[index].lower() == "owo":
            await message.delete()
            await message.channel.send("[REDACTED]")
        #redacts cat face
        elif words[index] == ":3":
            await message.delete()
            await message.channel.send("[REDACTED]")
        #redacts the word furry
        elif words[index].lower() == "furry":
            await message.delte()
            await message.channel.send("[REDACTED]")
        #redacts shy fingers
        elif index < len(words) - 1 and words[index] == "\U0001F449" and words[index + 1] == "\U0001F448":
            await message.delete()
            await message.channel.send("[REDACTED]")
        #redacts shy fingers around another emoji
        elif index < len(words) - 2 and words[index] == "\U0001F449" and words[index + 2] == "\U0001F448":
            await message.delete()
            await message.channel.send("[REDACTED]")
        #redacts tongue emoji
        elif words[index] == "\U0001F445":
            await message.delete()
            await message.channel.send("[REDACTED]")
        #allows people to redact other people
        elif len(words) >= 2 and index == 0 and words[index].lower() == prefix + "silence":
            if hasPermission(message.author.id):
                silenced = message.mentions[0].id
                await message.channel.send("Silencing Initiated...")
        #unsilences the silenced
        elif len(words) == 1 and index == 0 and words[index].lower() == prefix + "free":
            if hasPermission(message.author.id):
                silenced = 0
                await message.channel.send("Silencing Terminated...")
        #tells the bot not to repeat the redacted message anymore if a normal message is sent
        else:
            repeat = 0
        index = index + 1

client.run(token)
