import logging

import hikkatl.tl.types

from .. import loader, translations, utils
from hikkatl.tl.types import Message
@loader.tds
class TagAll(loader.Module):
    @loader.command(alias="tagall")
    async def e(self, message: Message, client: hikkatl.client.TelegramClient):
        if message.from_id.chat_id:
            chat_id = message.from_id.chat_id
            chat = client.get_entity(chat_id)
            result = client.get_participants(chat=chat)
            users = result.users
            
            for i in users:
                await client.send_message(entity=chat, message=f"User {i}")


