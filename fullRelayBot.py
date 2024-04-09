import discord as selfcord
import linecache
import re
from discord_webhook import DiscordWebhook

with open('listenserverids.txt') as file:
    serverids = []
    for line in file:
        serverids.append(line.strip())

with open('listenchannelids.txt') as file:
    listenchannels = []
    for line in file:
        listenchannels.append(line.strip())

#put the token of the listener account here.
DISCORD_USER_TOKEN = ""

LISTEN_GUILD_IDS = str(serverids)
LISTEN_CHANNEL_IDS = str(listenchannels)

def main():
    dc = selfcord.Client()

    @dc.event
    async def on_ready():
        await dc.change_presence(status=selfcord.Status.invisible, afk=True, edit_settings=False)
        print(f"Listening User: {dc.user}")

    @dc.event
    async def on_message(message):
        guild_id = str(message.guild.id)
        if guild_id not in LISTEN_GUILD_IDS:
            return

        channel_id = str(message.channel.id)
        if channel_id not in LISTEN_CHANNEL_IDS:
            return

        with open('listenchannelids.txt') as file:
            for line_num, line in enumerate(file, 1):
                if str(message.channel.id) in line:
                    #use line_num to find the corresponding webhook it should send to
                    webhookURLline = linecache.getline('relaywebhooks.txt',line_num).rstrip('\n')
                    break
        WEBHOOK_URL = webhookURLline[0:len(webhookURLline) - 0].split(", ")

        if message.attachments:
            attachmentUnformatted = message.attachments  # get the message's attachment, it is not returned as a string
            attachmentsOnly = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[/\-_@.&+]|[!*\(\),])+',
                                         str(attachmentUnformatted))  # only get the URLs
            attachmentLastSplit = (' '.join(
                attachmentsOnly))  # make the displayed attachment URLs separated with a single space so they embed
            attachmentURL = attachmentLastSplit  # assign it to the final variable
            msg_to_send = f"⁣[{str(message.guild.name).upper()}] {message.author}:\n\n{message.content}\n\n\"Attached Files:\"{attachmentURL}"

        else:
            msg_to_send = f"⁣[{str(message.guild.name).upper()}] {message.author}:\n\n{message.content}"

        #check the listen file, get the line number of it, then get the line number of the relay channel
        for i in range(0, len(WEBHOOK_URL)):
            webhook = DiscordWebhook(url=WEBHOOK_URL[i], username='KF Unify', content=msg_to_send, avatar_url="https://cdn.discordapp.com/attachments/730207383413850172/1072705864747733012/unifeisar.png")
            webhook.execute()

    dc.run(DISCORD_USER_TOKEN)

if __name__ == '__main__':
    main()
