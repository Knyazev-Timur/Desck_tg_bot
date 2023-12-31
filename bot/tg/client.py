import requests

from bot.tg.dc import GetUpdatesResponse, SendMessageResponse


class TgClient:
    def __init__(self, token):
        self.token = token

    def get_url(self, method: str) -> str:
        """ Формирование ссылки, токен +метод запроса"""
        return f"https://api.telegram.org/bot{self.token}/{method}"

    def get_updates(self, offset: int = 0, timeout: int = 60) -> GetUpdatesResponse:
        """ Получение сообщений от пользователя """
        url = self.get_url("getUpdates")
        resp = requests.get(url, params={"offset": offset, "timeout": timeout,
                                         "allowed_updates": ["update_id", "message"]})
        return GetUpdatesResponse.Schema().load(resp.json())

    def send_message(self, chat_id: int, text: str) -> SendMessageResponse:
        """ Отправка сообщений пользователю """
        url = self.get_url("sendMessage")
        resp = requests.post(url, params={"chat_id": chat_id, "text": text})
        return SendMessageResponse.Schema().load(resp.json())
