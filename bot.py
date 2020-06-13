import discord

token = "NzIwMzg3ODA1NTM2MDU5NDE0.XuQpyA.lc1x61RjY5ZfTRnn8zap2bDqtVU"
client = discord.Client()

@client.event
async def on_message(message):
    words = message.content.split()

    x = 0
    while x < len(words):
        if words[x] == "uwu" or words[x] == "UwU" or words[x] == "uWu" or words[x] == "UWU":
            await message.delete()
            await message.channel.send("[REDACTED]")
        elif words[x] == "owo" or words[x] == "OwO" or words[x] == "oWo" or words[x] == "OWO":
            await message.delete()
            await message.channel.send("[REDACTED]")
        elif words[x] == ":3":
            await message.delete()
            await message.channel.send("[REDACTED]")
        elif words[x] == "furry":
            await message.delte()
            await message.channel.send("[REDACTED]")
        elif words[x] == "technoblade" or words[x] == "Technoblade":
            await message.delete()
            await message.channel.send("[REDACTED]")
        elif x < len(words) - 1 and words[x] == "👉" and words[x + 1] == "👈":
            await message.delete()
            await message.channel.send("[REDACTED]")
        x = x + 1

client.run(token)
