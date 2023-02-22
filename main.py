# add your Library that you want to use
# เพิ่ม ไลบารี่ ที่ต้องการใช้งาน ลงในบรรทัด
import os
import discord
from discord.ext import commands
from gtts import gTTS
from dotenv import load_dotenv
from discord.voice_client import VoiceClient
import asyncio
#กำหนดตัวแปร intents
intents=discord.Intents.default()
intents.message_content = True
intents.members = True
#กำหนดตัวแปร bot ให้เป็น ให้บอทรับคำสั่งโดยกำหนดใช้งาน prefix !
bot = commands.Bot(command_prefix="!", intents=intents)

#กำหนดฟังชั่น on_ready ให้ print คำว่า "ลงชื่อเข้าใช้ในฐานะเข้าของ 'ชื่อบอท' " เมื่อ bot ลงชื่อเข้าใช้เรียบร้อยแล้ว
@bot.event
async def on_ready():
    print('ลงชื่อเข้าใช้ในฐานะเจ้าของ {0.user}'.format(bot))

#สร้างคำสั่ง text to speak โดยกำหนดชื่อฟังชั่นเป็น 'speak' และใช้งานโดยการ ใช้ คำสั่ง prefix ! ตามด้วยชื่อฟังชั่น
@bot.command()
async def speak(ctx, *, text):
     # สร้างไฟล์เสียงพูดด้วย gTTS
    tts = gTTS(text=text, lang='th')

    # บันทึกไฟล์เสียงพูดเป็นชื่อ say.mp3
    tts.save('say.mp3')

    # เชื่อมต่อไปยัง voice channel ของผู้ใช้
    channel = ctx.author.voice.channel
    voice_client = await channel.connect()

    # เล่นไฟล์เสียงพูดผ่าน voice client
    source = discord.FFmpegPCMAudio('say.mp3')
    voice_client.play(source)

    # รอจนกว่าเสียงพูดจะเล่นเสร็จ
    while voice_client.is_playing():
        await asyncio.sleep(1)

    # หลังจากเสียงพูดเล่นเสร็จแล้วให้บอทออกจาก voice channel
    await voice_client.disconnect()


#กำหนดตัวแปร token
load_dotenv()
token = os.getenv('TOKEN')
bot.run(token)