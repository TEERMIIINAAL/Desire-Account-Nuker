import requests,os,threading,time,json
from discord.ext import commands
with open('config.json') as f:
    config = json.load(f)
token = config.get('token')
prefix = "nigger"
friends = open('friends.txt')
guilds = open('guilds.txt')
headers = {'authorization': token}
client = commands.Bot(command_prefix=prefix, case_insensitive=False, self_bot=True)
def removefriends(u):
    while True:
       r = requests.delete(f"https://discord.com/api/v8/users/@me/relationships/{u}", headers=headers)
       if 'global' in r.text:
            time.sleep(r.json()['global'])
            print(f"Removed Relationship => {u}")
       else:
          break
def removeguilds(i):
    while True:
       r = requests.delete(f"https://discord.com/api/v8/users/@me/guilds/{i}", headers=headers)
       if 'global' in r.text:
            time.sleep(r.json()['global'])
            print(f"Left Guild => {i}")
       else:
          break
def spamguilds(name):
  while True: 
    json = {'name': name, 'type': 0}
    r = requests.post('https://discord.com/api/v8/guilds', headers=headers, json=json)
    if 'global' in r.text:
      time.sleep(r.json()['global'])
      print(f"Created Guild => {name}")
    else:
      break
def guildspam():
  name = input("\nGuild Names: ")
  amount = input("Amount: ")
  print()
  for i in range(int(amount)):
    threading.Thread(target=spamguilds, args=(name,)).start()
def removefriend():
  for f in friends:
    threading.Thread(target=removefriends, args=(f,)).start()
def removeguild():
  for g in guilds:
    threading.Thread(target=removeguilds, args=(g,)).start()
def menu():
  os.system('clear')
  print('''

                                    ╔╦╗╔═╗╔═╗╦╦═╗╔═╗                    
                                     ║║║╣ ╚═╗║╠╦╝║╣                      
                                    ═╩╝╚═╝╚═╝╩╩╚═╚═╝ 

                                 [1] Remove All Friends                
                                 [2] Remove All Guilds               
                                 [3] Create/Spam Guilds          
                                 [4] All In One/Account Nuke
                                 [5] Desire Nuker Credits
                                 [6] Exit The Program :)

  ''')
  choice = int(input("> "))
  if choice == 1:
    removefriend()
    time.sleep(2)
    menu()
  elif choice == 2:
    removeguild()
    time.sleep(2)
    menu()
  elif choice == 3:
    guildspam()
    time.sleep(2)
    menu()
  elif choice == 4:
    removefriend()
    removeguild()
    time.sleep(2)
    os.system('clear')
    print("Done Nuking - Spam Config: \n")
    guildspam()
    time.sleep(2)
    menu()
  elif choice == 5:
    print("\nThis tool was made by Yum & Dux - Press [Enter] To Return To Main-Menu")
    input()
    os.system('clear')
    print("Returning To Menu...")
    time.sleep(1)
    menu()
  elif choice == 6:
    os._exit(0)
  else:
    os.system('clear')
    print("Invalid Choice - Returning To Menu...")
    time.sleep(1)
    menu()
@client.event
async def on_ready():
  try:
      menu()
  except:
    pass
def Startup():
  try:
    client.run(token, bot=False)
  except:
    print("Invalid Token In Config.json File!")
if __name__ == "__main__":
    Startup()