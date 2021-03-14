import requests, json
createfriendsfile = open('friends.txt','w')
createfriendsfile.close()
createguildsfile = open('guilds.txt','w')
createguildsfile.close()
file = open('friends.txt','a')
guild = open('guilds.txt','a')
with open('config.json') as f:
    config = json.load(f)
token = config.get('token')
headers = {'Authorization': token}
def scrape():
  r = requests.get('https://discord.com/api/v8/users/@me/relationships', headers=headers)
  for x in r.json():
    file.write(f'{x["id"]}\n')
  p = requests.get('https://discord.com/api/v8/users/@me/guilds', headers=headers)
  for t in p.json():
    guild.write(f'{t["id"]}\n')
    print("Scraped - You May Close This Now")
scrape()