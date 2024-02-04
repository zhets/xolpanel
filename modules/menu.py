from xolpanel import *

@bot.on(events.NewMessage(pattern=r"(?:.menu|/menu)$"))
@bot.on(events.CallbackQuery(data=b'menu'))
async def menu(event):
	inline = [
[Button.inline("[ SSH MENU ]","ssh"),
Button.inline("[ TRIAL SSH ]","trial-ssh")],
[Button.url("[ FEEDBACK ]","https://t.me/Lemontreee3"),
Button.url("[ WHATSAPP ]","https://wa.me/62882003753308")]]
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
**⟨ 👨‍💻Admin Panel Menu ⟩**
**━━━━━━━━━━━━━━━━**
**» 🤖Bot Version:** `v3.0`
**» 🤖Bot By:** `@Lemontreee3`

**━━━━━━━━━━━━━━━━**
"""
		x = await event.edit(msg,buttons=inline)
		if not x:
			await event.reply(msg,buttons=inline)