from asyncio import sleep
from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
from rams.events import register
from rams import CMD_HELP
from rams import CMD_HANDLER as cmd
from rams.utils import ram_cmd
