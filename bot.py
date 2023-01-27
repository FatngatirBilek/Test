import openai
import discord

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    openai.api_key = "OPENAIKEY"
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt= message.content,
    )
    response = response["choices"][0]["text"]
    await message.channel.send(response)

client.run("DiscordBotToken")
