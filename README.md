# imageRelaySelfbot
A small python program to relay discord image URLs to a webhook using a user listener account. This was intended to be used with relaying images from fanart reposting channels, but can also be used as a HTTP link and file upload relayer.

The info it includes is the server the relayed file is from and the username of the image sender. It supports sending to multiple webhooks, and listening to multiple servers and channels.

It will relay any links, as well as any uploaded files to the webhook(s) of your choice.

### Usage
1. Put your user token in the variable named "DISCORD_USER_TOKEN".
2. Get the ID of the server you want to listen to, and put it in the "listenserverids.txt" file.
3. Get the channel ID of the channel you want to listen to, and put it in the "listenchannelids.txt" file.
4. Get the webhook you want the channel to relay to and put it in "relaywebhooks.txt". Put it on the SAME LINE NUMBER as the corresponding channel ID in "listenchannelids.txt"

  Example: If the channel ID for #cats-and-tortises is on line 4, the corresponding webhook needs to be on line 4.

### Notes
If you want to relay one channel to multiple webhooks, separate the webhooks with a comma and a space -> `, ` and put it on the same line.

Example: `https://discordapp.com/3817418, https://discordapp.com/329471, https://discordapp.com/01298541`
