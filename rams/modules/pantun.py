
from time import sleep

from rams import CMD_HANDLER as cmd
from rams import CMD_HELP
from rams.utils import edit_or_reply, ram_cmd


@ram_cmd(pattern="sadboy(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, "`Pertama-tama kamu cantik`")
    sleep(2)
    await xx.edit("`Kedua kamu manis`")
    sleep(1)
    await xx.edit("`Dan yang terakhir adalah kamu bukan jodohku`")

