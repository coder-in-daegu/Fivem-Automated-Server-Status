import requests
import discord
import asyncio

from discord_components import DiscordComponents, Button, ButtonStyle


client = discord.Client()
DiscordComponents(client)

#디스코드 설정
channel = 950931370224533514
token = ""

#메시지 설정
online_message = "아케인 서버가 온라인 상태 입니다.\n\n아래 접속 버튼을 통해 서버에 접속해주세요!"
offline_message = "아케인 서버가 오프라인 상태 입니다.\n\n공지사항 채널을 확인 해주세요!"
img_url = "https://cdn.discordapp.com/attachments/918827534379012126/950931603771760660/5524d2945650988b.png"

@client.event
async def on_ready():
    ch = client.get_channel(channel)
    try:
        msg = await ch.send("@everyone\n")
    except:
        print("[Status Engine] [!] 채팅채널이 없습니다. 메시지를 전송하지 않았습니다.") 
    online=discord.Embed(title="**서버 상태**", description=online_message, color=0x37ff00)
    online.set_thumbnail(url=img_url)
    online.set_footer(text="FiveM :: Dev")
    offline=discord.Embed(title="**서버 상태**", description=offline_message, color=0xff0000)
    offline.set_thumbnail(url=img_url)
    offline.set_footer(text="FiveM :: Dev")
    while True:
        try:
            response = requests.get("http://127.0.0.1:30120/info.json")
            print("[Status Engine] [R] 서버 상태를 확인중 입니다.") 
            if response.status_code == 200:
                print("[Status Engine] [S] 서버가 온라인 상태입니다.") 
                await msg.edit(embed=online, components=[[Button(label=f"온라인", style=ButtonStyle.green, disabled=True), Button(label=f"서버 접속", style=ButtonStyle.URL, url="http://fivemjs.kro.kr/")]])
            else:
                print("[Status Engine] [S] 서버가 오프라인 상태입니다.") 
                await msg.edit(embed=offline, components=[[Button(label=f"오프라인", style=ButtonStyle.red, disabled=True), Button(label=f"잠시 대기해주세요", style=ButtonStyle.gray, disabled=True)]])
        except:
            try:
                print("[Status Engine] [S] 서버가 오프라인 상태입니다.") 
                await msg.edit(embed=offline, components=[[Button(label=f"오프라인", style=ButtonStyle.red, disabled=True), Button(label=f"잠시 대기해주세요", style=ButtonStyle.gray, disabled=True)]])
            except:
                print("[Status Engine] [S] 채팅채널이 없습니다. 메시지를 전송하지 않았습니다.") 

        await asyncio.sleep(3)




client.run(token)
