import logging

from .. import loader, utils
from hikkatl.tl.types import Message


@loader.tds
class TagAll(loader.Module):

    strings = {
        "name": "TagAll",
        "info_user": "User {io}"
    
    @loader.command(alias="tl")
    async def tagall(self, message: Message, client: hikkatl.client.TelegramClient):
        if message.from_id.chat_id:
            chat_id = message.from_id.chat_id
            chat = client.get_entity(chat_id)
            result = client.get_participants(chat=chat)
            users = result.users
            
            for i in users:
                await client.send_message(entity=chat, message=self.strings("info_user").format(io=i))


