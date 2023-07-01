from django.core.management import BaseCommand

from bot.models import TgUser
from bot.tg.client import TgClient
from bot.tg.schemas import Message


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tg_client = TgClient()

    def handle(self, *args, **options):
        offset = 0

        self.stdout.write(self.style.SUCCESS('Bot started'))
        while True:
            res = self.tg_client.get_updates(offset=offset)
            for item in res.result:
                offset = item.update_id+1
                self.handle_message(item.message)

    def handle_message(self, msg: Message):
        # self.tg_client.send_message(chat_id=msg.chat.id, text=msg.text)
        tg_user, _ = TgUser.objects.get_or_create(chat_id=msg.chat.id)

        if tg_user.is_verified:
            self.handle_authorized_user(tg_user, msg)
        else:
            chat_id = tg_user.chat_id
            self.tg_client.send_message(msg.chat.id, 'Введите код авторизации:')
            tg_user.update_verification_code()
            self.tg_client.send_message(chat_id, tg_user.verification_code)
            # self.handle_unauthorized_user(tg_user, msg)

    def handle_authorized_user(self, tg_user: TgUser, msg: Message):


        if msg.text.startswith('/'):
            if msg.text == '/goals':
                self.tg_client.send_message(msg.chat.id, f'Вы выбрали ЦЕЛИ')

            elif msg.text == '/create':
                self.tg_client.send_message(msg.chat.id, f'Вы выбрали СОЗДАТЬ')

            else:
                self.tg_client.send_message(tg_user.chat_id, 'Command not found')

        else:
            self.tg_client.send_message(msg.chat.id, f'Приветствую в чате ID:{msg.chat.id}\n'
                                                     f'Доступные команды:\n'
                                                     f'/goals\n/create')


    # def handle_unauthorized_user(self, tg_user: TgUser, msg: Message):
    #     chat_id = tg_user.chat_id
    #     self.tg_client.send_message(msg.chat.id, 'Введите код авторизации:')
    #     tg_user.update_verification_code()
    #     self.tg_client.send_message(chat_id, tg_user.verification_code)
