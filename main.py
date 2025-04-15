import requests
discordUrl = 'https://discord.com/api/webhooks/1361600447554781264/UyXBipgWsIoXsHr-0GRQg6xHBjigYB0TDEW5-KWIBlkgvd336eSX2ccwuUAubrTDMfPs'

text = {
    "content": "Privet"
}

response = requests.post(discordUrl, json=text)