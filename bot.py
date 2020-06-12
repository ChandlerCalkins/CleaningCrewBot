import discord

token = ""
client = discord.Client()

print("test")

@client.event
async def on_message(message):
    print(message.content)
    words = message.content.split()
    for x in words:
        if x == "uwu" or x == "UwU" or x == "uWu" or x == "UWU" or x == "owo" or x == "OwO" or x == "oWo" or x == "OWO":
            await message.delete()
            await message.channel.send("[REDACTED]")

client.run(token)
