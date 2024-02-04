from xolpanel import *

@bot.on(events.CallbackQuery(data=b'ssh'))
async def ssh(event):
	async def ssh_(event):
		inline = [
[Button.inline("[ TRIAL SSH ]","trial-ssh"),
Button.inline("[ CREATE SSH ]","create-ssh")],
[Button.inline("[ DELETE SSH ]","delete-ssh"),
Button.inline("[ CHECK Login SSH ]","login-ssh")],
[Button.inline("[ SHOW ALL USER SSH ]","show-ssh")],
[Button.inline("‹ MAIN MENU ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
**━━━━━━━━━━━━━━━━**
**⟨ SSH Menu ⟩**
**━━━━━━━━━━━━━━━━**
**» Service:** `SSH`
**» Hostname/IP:** `{DOMAIN}`
**» ISP:** `{z["isp"]}`
**» Country:** `{z["country"]}`
**» 🤖@Lemontreee3**
**━━━━━━━━━━━━━━━━**
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await ssh_(event)
	else:
		await event.answer("Access Denied",alert=True)