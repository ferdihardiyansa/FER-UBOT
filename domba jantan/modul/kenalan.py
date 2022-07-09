from time import sleep
from rams.utils import edit_or_reply, ram_cmd
from rams import CMD_HELP, CMD_HANDLER as cmd, owner
eor = edit_or_reply

@ram_cmd(pattern='oi(?: |$)(.*)')
async def _(event):
    await eor(event, f"`Hai Perkenalkan Namaku {owner}`")
    sleep(3)
    await eor(event, "`Salam Kenal Ya semua`")
    sleep(1)
    await eor(event, "`gua cuman mau bilang semangat`")
# Create by myself @localheart


@ram_cmd(pattern='sayang(?: |$)(.*)')
async def _(event):
    await eor(event, "`Cuma Mau Bilang`")
    sleep(3)
    await eor(event, "`Aku Sayang Kamu`")
    sleep(1)
    await eor(event, "`I LOVE YOU 💞`")
# Create by myself @localheart


@ram_cmd(pattern='semangat(?: |$)(.*)')
async def _(event):
    await eor(event, "`Apapun Yang Terjadi`")
    sleep(3)
    await eor(event, "`Tetaplah Bernapas`")
    sleep(1)
    await eor(event, "`Dan Selalu Bersyukur`")
# Create by myself @localheart

CMD_HELP.update(
    {
       "kenalan": f"**Plugin :** Kenalan.\
       \n\n    • Syntax : `{cmd}oi`\
       \n     • **Function: **Untuk memperkenalkan diri Mu.\
       \n\n    •  Syntax : `{cmd}sayang`\
       \n     • **Function: **Untuk mengungkapkan Rasa.\
       \n\n    •  Syntax : `{cmd}semangat`\
       \n     • **Function: **Untuk menyemangati seseorang.\
    "
    }
)
