from xolpanel import *

@bot.on(events.CallbackQuery(data=b'delete-ssh'))
async def delete_ssh(event):
	async def delete_ssh_(event):
		async with bot.conversation(chat) as user:
			await event.respond("**Username To Be Deleted:**")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		try:
			subprocess.check_output(f"userdel -f {user}",shell=True)
		except:
			await event.respond(f"**User** `{user}` **Not Found**")
		else:
			await event.respond(f"**Successfully Deleted** `{user}`")
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await delete_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'ssh'))
async def ssh(event):
	async def ssh_(event):
		inline = [
[Button.inline(" ᴛʀɪᴀʟ ꜱꜱʜ ","trial-ssh"),
Button.inline(" ᴄʀᴇᴀᴛᴇ ꜱꜱʜ ","create-ssh")],
[Button.inline(" ᴅᴇʟᴇᴛᴇ ꜱꜱʜ ","delete-ssh"),
Button.inline(" ᴄʜᴇᴄᴋ ꜱꜱʜ ","login-ssh")],
[Button.inline(" ᴍᴇᴍʙᴇʀ ꜱꜱʜ ","show-ssh")],
[Button.inline("‹ ᴍᴀɪɴ ᴍᴇɴᴜ ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
**━━━━━━━━━━━━━━━━**
  **⟨ ⚡SSH MENU⚡ ⟩**
**━━━━━━━━━━━━━━━━**
**» Service:** `SSH`
**» Host/IP:** `{DOMAIN}`
**» ISP:** `{z["isp"]}`
**» Country:** `{z["country"]}`
**» 🤖@xdxl_store**
**━━━━━━━━━━━━━━━━**
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await ssh_(event)
	else:
		await event.answer("Access Denied",alert=True)
