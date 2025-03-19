import discord
from discord.ext import commands
import asyncio
import os
from myserver import server_on

GUILD_ID = 923167904629928005

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ บอทออนไลน์เป็น {bot.user}')

@bot.command()
async def dm_embed(ctx):
    await ctx.send("✅ กำลังส่งข้อความ...")

    guild = bot.get_guild(GUILD_ID)
    if guild is None:
        await ctx.send("❌ ไม่พบเซิร์ฟเวอร์ที่ระบุ")
        return

    embed1 = discord.Embed(
        title="CZ Shop ร้านค้าขายโปร Free fire 🚀",
        description=(
            "+ เริ่มต้นแค่วันละ 35 บาท เท่านั้น !!\n"
            "+ CZ Panel `มอง ล็อคไหล่ สไนล็อค สไนสับไว`\n"
            "+ CZ Modmenu `มองเส้น ล็อคหัว`\n"
            "+ เติมเงินออโต้ รองรับธนาคาร และวอเล็ท"
        ),
        color=discord.Color.blue()
    ).add_field(
        name="🌐 เว็บไซต์",
        value="[ซื้อ CZ panel คลิกที่นี่](https://czshop.rdcw.xyz/)",
        inline=False
    ).set_image(url="https://i.postimg.cc/9f4tRtF4/Annotation-2025-03-16-005706.png")

    embed2 = discord.Embed(
        title="Mazda Shop ร้านค้าขายโปร Free fire และโค้ด LV.8-30 พร้อมลงแรงค์ 🚀",
        description=(
            "+ จำหน่ายโค้ด LV.8-30 ราคาถูก!!\n"
            "+ จำหน่ายโปร Free fire ios / PC\n"
            "+ เติมเงินออโต้ รองรับธนาคาร และวอเล็ท"
        ),
        color=discord.Color.green()
    ).add_field(
        name="🌐 เว็บไซต์",
        value="[ซื้อ โค้ด คลิกที่นี่](https://mazdamodzshop.com/?page=homesite)",
        inline=False
    ).set_image(url="https://i.postimg.cc/KvzK8cYj/Annotation-2025-03-16-010045.png")

    success, failed = 0, 0

    for member in guild.members:
        if member.bot:
            continue

        try:
            await member.send(embeds=[embed1, embed2])
            await member.send("🔗 Discord: https://discord.gg/XyjyUnxPDw")
            success += 1
            print(f"✅ ส่งข้อความให้ {member}")
            await asyncio.sleep(20)  # sleep กัน rate limit
        except discord.Forbidden:
            failed += 1
            print(f"❌ ไม่สามารถส่งข้อความให้ {member} (ปิด DM)")
        except Exception as e:
            failed += 1
            print(f"⚠️ เกิดข้อผิดพลาดกับ {member}: {e}")

    await ctx.send(f"📌 ส่งข้อความสำเร็จ: {success} คน, ส่งไม่ได้: {failed} คน")

server_on()
bot.run(os.getenv('TOKEN'))
