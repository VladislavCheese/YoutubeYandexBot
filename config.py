login = "YANDEX_LOGIN"
password = "YANDEX_PASSWORD"
telegram_bot_token = "TG_BOT_TOKEN"
telegram_user_id = telegram_id

proxy = None
# {
#     'proxy_url': 'http://russia-dd.proxy.digitalresistance.dog:443',
# }

start_text = "Данный бот запускает видео с YouTube на Яндекс.Станции.\n" \
             "Может быть ипользован только его владельцем - @vladislav_syrov.\n" \
             "Подробности можно узнать через /help"
help_text = "Бот анилизирует каждое текстовое сообщение и ищет в нем ссылку на youtube видео." \
            "Для передачи данных на Яндрекс.Станцию используется закрытое API, которое " \
            "требут логин и пароль пользователя yandex. Далее в аккаунте автоматически находится " \
            "станция подключенная к телевизору и через нее открывается видео. Идея не моя, более подробно " \
            "можно прочитать тут: https://habr.com/ru/post/479242 . Также ссылка на мой репозиторий с " \
            "доработаным ботом: https://github.com/VladislavCheese/YoutubeYandexBot."