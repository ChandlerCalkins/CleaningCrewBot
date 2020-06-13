import discord

token = ""
client = discord.Client()

print("test")

@client.event
async def on_message(message):
    print(message.content)
    words = message.content.split()
    
    x = 0;
    while x < len(words):
        if words[x] == "uwu" or words[x] == "UwU" or words[x] == "uWu" or words[x] == "UWU" or words[x] == "owo" or words[x] == "OwO" or words[x] == "oWo" or words[x] == "OWO":
            await message.delete()
            await message.channel.send("[REDACTED]")
        elif x < len(words) - 1 and words[x] == "👉" and words[x + 1] == "👈":
            await message.delete()
            await message.channel.send("[REDACTED]")
        x = x + 1

client.run(token)
