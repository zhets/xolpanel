from xolpanel import *

@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
	await event.reply("""
 Hai Saya Adalah Bot @xdxl_store Silahkan Ketik /menu""")

@bot.on(events.NewMessage(pattern=r"(?:.menu|/menu)$"))
@bot.on(events.CallbackQuery(data=b'menu'))
async def menu(event):
	inline = [
[Button.inline(" SSH MENU ","ssh")],
[Button.url(" CONTACT ","t.me/xdxl_store")],
[Button.url(" CHANNEL ","t.me/xdxl_vpn"),
Button.url(" GROUP ","t.me/vpn_storeid")]]
	sender = await event.get_sender()
	val = valid(str(sender.id))
	if val == "false":
		try:
			await event.answer("Akses Ditolak", alert=True)
		except:
			await event.reply("Akses Ditolak")
	elif val == "true":
		msg = f"""
**━━━━━━━━━━━━━━━━**
**⟨ ⚡BOT PANEL MENU⚡ ⟩**
**━━━━━━━━━━━━━━━━**
**» 🤖Bot Version:** `v1.0`
**» 🤖Bot By:** `@xdxl_store`

**━━━━━━━━━━━━━━━━**
"""
		x = await event.edit(msg,buttons=inline)
		if not x:
			await event.reply(msg,buttons=inline)
