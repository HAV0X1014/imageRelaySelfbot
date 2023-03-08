import selfcord
import re
from discord_webhook import DiscordWebhook
#put the server and channel IDs here, preferably above the channel you want to listen to. comma separate them with no spaces
serverids = []
channelids = []

#put URLs of webhooks you want to send the images to- quote enclosed and comma separated. using only 1 webhook is ok
WEBHOOK_URL = ["",]
#put the token of the listener account here
DISCORD_USER_TOKEN = ""

#put the listener account's ID here so it doesnt relay its own messages
BOT_ID = 
LISTEN_GUILD_IDS = serverids
LISTEN_CHANNEL_IDS = channelids

def main():
    dc = selfcord.Client()


    @dc.event
    async def on_ready():
        print(f"Listening User: {dc.user}")

    @dc.event
    async def on_message(message):
        attachmentURL = None
        guild_id = message.guild.id
        if guild_id not in LISTEN_GUILD_IDS:
            return

        channel_id = message.channel.id
        if channel_id not in LISTEN_CHANNEL_IDS:
            return

        author_id = message.author.id
        if author_id == BOT_ID:
            return

        if "http" in message.content:                               #also relay HTTP links, like links to pixiv or twitter
            attachmentList = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.content)
            attachmentUnformatted = ' '.join([str(elem) for elem in attachmentList])        #cast the list it returns to a string
            attachmentFormat1 = attachmentUnformatted.strip("['")          #remove those things that break embeds
            attachmentURL = attachmentFormat1.strip("']")                 #remove those again
            
       if message.attachments:
            attachmentUnformatted = message.attachments             #get the message's attachment, it is not returned as a string
            attachmentsOnly = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[/\-_@.&+]|[!*\(\),])+', str(attachmentUnformatted))       #only get the URLs
            attachmentLastSplit = (' '.join(attachmentsOnly))       #make the displayed attachment URLs separated with a single space so they embed
            attachmentURL = attachmentLastSplit                     #assign it to the final variable
        
        if attachmentURL is None:                                   #prevent red shouty text on normal messages without attachments or HTTP in it
            return

        msg_to_send = f"⁣[{str(message.guild.name).upper()}] {message.author.name}:\t{attachmentURL}"

        for i in range(0, len(WEBHOOK_URL)):                        #iterate through the webhook URLs in case you want to send to multiple places
            webhook = DiscordWebhook(url=WEBHOOK_URL[i], username='Unify', content=msg_to_send)
            webhook.execute()

    dc.run(DISCORD_USER_TOKEN)

if __name__ == '__main__':
    main()
