from django.core.management import BaseCommand

from bot.tg.client import TgClient


class Command(BaseCommand):

    def handle(self, *args, **options):
        offset = 0

        tg_client = TgClient()
        while True:
            res = tg_client.get_updates(offset=offset)
            for item in res.result:
                offset = item.update_id+1
                tg_client.send_message(chat_id=item.message.chat.id, text=item.message.text)
