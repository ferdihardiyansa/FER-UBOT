
from time import sleep

from rams import CMD_HANDLER as cmd
from rams import CMD_HELP
from rams.utils import edit_or_reply, ram_cmd


@ram_cmd(pattern="tahu(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, "`ikan hiu makan tomat`")
    sleep(2)
    await xx.edit("`i love you so much`")
    sleep(1)
    await xx.edit("`JIAKHHHH`")


@ram_cmd(pattern="con(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, "`i have crush on you`")
    sleep(2)
    await xx.edit("`eh tapi boong`")


CMD_HELP.update(
    {
        "Pantun": f"**Plugin : **`pantun`\
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
        \n\n  •  **Syntax :** `{cmd}cru`\
        \n  •  **Function : **confess tapi boong\
        \n\n  •  **Syntax :** `{cmd}misi` ; `{cmd}pantau`\
        \n  •  **Function : **Arts Beruang kek lagi mantau.\
        \n\n  •  **Syntax :** `{cmd}tahu`\
        \n  •  **Function : **pantun tahu.\
    "
    }
)
