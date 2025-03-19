import discord
from discord.ext import commands
import asyncio
import os
from myserver import server_on

GUILD_IDS = [1315950507130355813, 1317703769387040831] 

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
        title="THOMAS SHOP ร้านจำหน่ายโปรราคาถูกและอื่นๆอีกมากมาย",
        description=(
            "+ โปรฟีาย แอนดรอยด์ IOS PC\n"
            "+ โปรROV แอนดรอยด์ IOS\n"
            "+ จำหน่ายโค้ด LV.8-30 ราคาถูก!\n"
            "+ เติมเงินออโต้ รองรับธนาคาร และวอเล็ท\n"
            "+ รหัสROV เริ่มต้น 40 บาทเท่านั้น"
        ),
        color=discord.Color.blue()
    ).add_field(
        name="🌐 เว็บไซต์",
        value="เว็บไซต์ขายโปรราคาถูก [คลิกที่นี่](https://thomas.rexzy.xyz/)",
        inline=False
    ).set_image(url="https://img2.pic.in.th/pic/imagef22c934b4052933a.png")

    success, failed = 0, 0

    for member in guild.members:
        if member.bot:
            continue

        try:
            await member.send(embed=embed1)
            await member.send("🔗 Discord: https://discord.gg/thomas")
            await member.send("🔗 Discord: https://discord.gg/ujpkAPkx")
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
