
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

CMD_HELP.update(
    {
        "arts": f"**Plugin : **`arts`\
        \n\n  •  **Syntax :** `{cmd}kodok`\
        \n  •  **Function : **arts Frog.\
        \n\n  •  **Syntax :** `{cmd}kodog`\
        \n  •  **Function : **arts frog bundir.\
        \n\n  •  **Syntax :** `{cmd}dtrump`\
        \n  •  **Function : **arts donald Trump.\
        \n\n  •  **Syntax :** `{cmd}scina`\
        \n  •  **Function : **arts presiden cina.\
        \n\n  •  **Syntax :** `{cmd}wlcm`\
        \n  •  **Function : **arts beruang welcome.\
        \n\n  •  **Syntax :** `{cmd}gta`\
        \n  •  **Function : **arts si jhonson.\
        \n\n  •  **Syntax :** `{cmd}sthink`\
        \n  •  **Function : **arts berfikir\
        \n\n  •  **Syntax :** `{cmd}misi` ; `{cmd}pantau`\
        \n  •  **Function : **Arts Beruang kek lagi mantau.\
        \n\n  •  **Syntax :** `{cmd}sadboy`\
        \n  •  **Function : **ya sadboy coba aja.\
    "
    }
)
