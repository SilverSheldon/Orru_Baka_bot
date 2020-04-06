import config
import telebot
import time
import db


bot = telebot.TeleBot(config.TOKEN)  # Создание экземпляра класса TeleBot
bot.delete_webhook()  # Удаление вэбхука

admin_id_list = [335672004, 377838656, 634780542]

# Общие команды --------------------------------------------------------------------------------------------------------
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.clear_step_handler(message)
    kbd = telebot.types.InlineKeyboardMarkup()
    kbd.add(telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
    text = 'Привет! {0.first_name} на связи.\n' \
           'Чтобы узнать о доступных командах, нажми "В главное меню"'.format(bot.get_me())
    with open(r"media\hello.jpg", "rb") as start_pic:
        if message.text == '/start':
            bot.send_photo(chat_id=message.chat.id, photo=start_pic, caption=text, reply_markup=kbd)
        else:
            bot.edit_message_media(media=telebot.types.InputMediaPhoto(start_pic),
                                   chat_id=message.chat.id,
                                   message_id=message.message_id)
            bot.edit_message_caption(caption=text,
                                     chat_id=message.chat.id,
                                     message_id=message.message_id,
                                     parse_mode='html',
                                     reply_markup=kbd)


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.clear_step_handler(message)
    kbd = telebot.types.InlineKeyboardMarkup()
    kbd.add(telebot.types.InlineKeyboardButton(text='Донаты', callback_data='donate'),
            telebot.types.InlineKeyboardButton(text='Мои соцсети', callback_data='references'))
    kbd.row(telebot.types.InlineKeyboardButton(text='Мой телеграмм-канал', callback_data='channel'))
    kbd.row(telebot.types.InlineKeyboardButton(text='Все релизы в Моей озвучке', callback_data='anime_list'))
    kbd.row(telebot.types.InlineKeyboardButton(text='Настройки (только для админов)', callback_data='admin_commands'))
    kbd.row(telebot.types.InlineKeyboardButton(text='Написать разработчику', url='https://t.me/Jitterbug_Jemboree'))
    text = 'Главное меню'
    with open(r"media\help.jpg", "rb") as help_pic:
        if message.text == '/help':
            bot.send_photo(chat_id=message.chat.id, photo=help_pic, caption=text, reply_markup=kbd)
        else:
            bot.edit_message_media(media=telebot.types.InputMediaPhoto(help_pic),
                                   chat_id=message.chat.id,
                                   message_id=message.message_id)
            bot.edit_message_caption(caption=text,
                                     chat_id=message.chat.id,
                                     message_id=message.message_id,
                                     reply_markup=kbd)


@bot.message_handler(commands=['donate'])
def donate_command(message):
    bot.clear_step_handler(message)
    kbd = telebot.types.InlineKeyboardMarkup()
    kbd.row(telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
    text = 'Поддержать чеканной монетой можно любым из способов:\n' \
           'Перевод на Qiwi кошелек: +79998616461\n' \
           'Перевод на карту сбербанка: 4276 4000 7542 7477\n' \
           'Перевод VK:\n' \
           '  <a href="https://vk.com/im?peers=-181492719_c159&sel=190579374">- в личные сообщения</a>\n' \
           '  <a href="https://vk.com/im?peers=c159_190579374&sel=-181492719">- в сообщения группы VK</a>'
    with open(r"media\donate.jpg", "rb") as donate_pic:
        if message.text == '/donate':
            bot.send_photo(chat_id=message.chat.id, photo=donate_pic, caption=text, parse_mode='html', reply_markup=kbd)
        else:
            bot.edit_message_media(media=telebot.types.InputMediaPhoto(donate_pic),
                                   chat_id=message.chat.id,
                                   message_id=message.message_id)
            bot.edit_message_caption(caption=text,
                                     chat_id=message.chat.id,
                                     message_id=message.message_id,
                                     parse_mode='html',
                                     reply_markup=kbd)


@bot.message_handler(commands=['channel'])
def channel_command(message):
    bot.clear_step_handler(message)
    kbd = telebot.types.InlineKeyboardMarkup()
    kbd.add(telebot.types.InlineKeyboardButton(text='Открыть канал', url='https://t.me/orrubaka'),
            telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
    text = 'Присоединяйся к моему <a href="https://t.me/orrubaka">каналу</a>, где публикуется самая свежая озвучка!'
    with open(r"media\channel.jpg", "rb") as channel_pic:
        if message.text == '/channel':
            bot.send_photo(message.chat.id, photo=channel_pic, caption=text, parse_mode='html', reply_markup=kbd)
        else:
            bot.edit_message_media(media=telebot.types.InputMediaPhoto(channel_pic),
                                   chat_id=message.chat.id,
                                   message_id=message.message_id)
            bot.edit_message_caption(caption=text,
                                     chat_id=message.chat.id,
                                     message_id=message.message_id,
                                     parse_mode='html',
                                     reply_markup=kbd)


@bot.message_handler(commands=['references'])
def references_command(message):
    bot.clear_step_handler(message)
    kbd = telebot.types.InlineKeyboardMarkup()
    kbd.add(telebot.types.InlineKeyboardButton(text='Страница ВК', url='https://vk.com/lenaivanova1998'),
            telebot.types.InlineKeyboardButton(text='Группа ВК', url='https://vk.com/orrubaka'))
    kbd.add(telebot.types.InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/orrubaka'),
            telebot.types.InlineKeyboardButton(text='Канал в Telegram', url='https://t.me/orrubaka'))
    kbd.row(telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
    text = 'Я в соцсетях'
    with open(r"media\references.jpg", "rb") as references_pic:
        if message.text == '/references':
            bot.send_photo(chat_id=message.chat.id, photo=references_pic, caption=text, reply_markup=kbd)
        else:
            bot.edit_message_media(media=telebot.types.InputMediaPhoto(references_pic),
                                   chat_id=message.chat.id,
                                   message_id=message.message_id)
            bot.edit_message_caption(caption=text, chat_id=message.chat.id,
                                     message_id=message.message_id,
                                     reply_markup=kbd)


@bot.message_handler(commands=['anime_list'])
def anime_list_command(message):
    bot.clear_step_handler(message)
    kbd = telebot.types.InlineKeyboardMarkup()
    for item in db.get_category_list():
        kbd.row(telebot.types.InlineKeyboardButton(text=item, callback_data=item))
    kbd.row(telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
    text = 'Список озвученных тайтлов по категориям и сезонам.\nСо временем постараемся залить все серии сюда :)'
    with open(r"media\anime_list.jpg", "rb") as anime_list_pic:
        if message.text == '/anime_list':
            bot.send_photo(chat_id=message.chat.id, photo=anime_list_pic, caption=text, reply_markup=kbd)
        else:
            bot.edit_message_media(media=telebot.types.InputMediaPhoto(anime_list_pic),
                                   chat_id=message.chat.id,
                                   message_id=message.message_id)
            bot.edit_message_caption(caption=text,
                                     chat_id=message.chat.id,
                                     message_id=message.message_id,
                                     reply_markup=kbd)


# Команды только для админов -------------------------------------------------------------------------------------------
@bot.message_handler(commands=['admin_commands'])
def admin_commands_command(message, is_admin=None):
    bot.clear_step_handler(message)
    if is_admin or message.from_user.id in admin_id_list:
        kbd = telebot.types.InlineKeyboardMarkup()
        kbd.add(telebot.types.InlineKeyboardButton(text='Добавить аниме', callback_data='add_new_anime'),
                telebot.types.InlineKeyboardButton(text='Удалить аниме', callback_data='delete_anime'))
        kbd.add(telebot.types.InlineKeyboardButton(text='Все команды бота', callback_data='all_commands'),
                telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
        text = 'Добро пожаловать в админку!\nДоступные команды:'
        with open(r"media\admin.jpg", "rb") as admin_pic:
            if message.text == '/admin_commands':
                bot.send_photo(photo=admin_pic, chat_id=message.chat.id, caption=text, reply_markup=kbd)
            else:
                bot.edit_message_media(media=telebot.types.InputMediaPhoto(admin_pic),
                                       chat_id=message.chat.id,
                                       message_id=message.message_id)
                bot.edit_message_caption(caption=text,
                                         chat_id=message.chat.id,
                                         message_id=message.message_id,
                                         reply_markup=kbd)
    else:
        accept_error(message)


@bot.message_handler(commands=['all_commands'])
def all_commands_command(message, is_admin=None):
    bot.clear_step_handler(message)
    if is_admin or message.from_user.id in admin_id_list:
        kbd = telebot.types.InlineKeyboardMarkup()
        kbd.add(telebot.types.InlineKeyboardButton(text='Панель админа', callback_data='admin_commands'),
                telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
        with open(r"media\admin.jpg", "rb") as admin_pic:
            text = 'Список всех команд\n\n' \
                   'Общие:\n\n' \
                   '  /start\n' \
                   '  /help\n' \
                   '  /donate\n' \
                   '  /channel\n' \
                   '  /references\n' \
                   '  /anime_list\n\n' \
                   'Админские:\n\n' \
                   '  /admin_commands\n' \
                   '  /all_commands\n' \
                   '  /add_new_anime\n' \
                   '  /delete_anime'
            if message.text == '/all_commands':
                bot.send_photo(photo=admin_pic, chat_id=message.chat.id, caption=text, reply_markup=kbd)
            else:
                bot.edit_message_caption(caption=text,
                                         chat_id=message.chat.id,
                                         message_id=message.message_id,
                                         reply_markup=kbd)
    else:  # если не админ
        accept_error(message)


# ------------------------------------------------- ДОБАВЛЕНИЕ АНИМЕ ---------------------------------------------------
@bot.message_handler(commands=['add_new_anime'])
def add_new_anime_command(message, is_admin=None):
    bot.clear_step_handler(message)
    if is_admin or message.from_user.id in admin_id_list:
        kbd = telebot.types.InlineKeyboardMarkup()
        for item in db.get_category_list():
            kbd.row(telebot.types.InlineKeyboardButton(text=item, callback_data=item.upper()))
        kbd.add(telebot.types.InlineKeyboardButton(text='Панель админа', callback_data='admin_commands'),
                telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
        text = 'Перед добавлением аниме выбери категорию.\n' \
               'Если это новая категория, пришли мне её название.\n' \
               'Список имеющихся категорий:'
        with open(r"media\admin.jpg", "rb") as admin_pic:
            send = bot.send_photo(photo=admin_pic, chat_id=message.chat.id, caption=text, reply_markup=kbd)
            bot.register_next_step_handler(message=send, callback=waiting_for_category)
    else:  # если не админ
        accept_error(message)


def waiting_for_category(message, is_admin=None, ctg=None):
    global anime_category
    if is_admin or message.from_user.id in admin_id_list:
        kbd = telebot.types.InlineKeyboardMarkup()
        kbd.add(telebot.types.InlineKeyboardButton(text='Панель админа', callback_data='admin_commands'),
                telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
        if message.text or ctg is not None:
            if message.text:
                anime_category = message.text
            else:
                anime_category = ctg
            anime_list = ''
            for item in db.get_anime_list(ctg=anime_category):
                anime_list += item + '\n'
            text = 'Теперь пришли название аниме. ' \
                   'Список имеющихся аниме по категории "' + anime_category + '":\n\n' + anime_list
            with open(r"media\admin.jpg", "rb") as admin_pic:
                send = bot.send_photo(chat_id=message.chat.id, photo=admin_pic, caption=text, reply_markup=kbd)
                bot.register_next_step_handler(send, waiting_for_name)
        else:
            send = bot.send_message(chat_id=message.chat.id, text='Установи категорию!!!')
            bot.register_next_step_handler(send, waiting_for_category)
    else:
        accept_error(message)


def waiting_for_name(message):
    global anime_name
    if message.from_user.id in admin_id_list:
        kbd = telebot.types.InlineKeyboardMarkup()
        kbd.add(telebot.types.InlineKeyboardButton(text='Панель админа', callback_data='admin_commands'),
                telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
        text = 'Теперь пришли ссылку на это аниме (можно на онлайник, можно на видео с канала, да хоть на ютуб).'
        if message.text:
            with open(r"media\admin.jpg", "rb") as admin_pic:
                anime_name = message.text
                send = bot.send_photo(photo=admin_pic, chat_id=message.chat.id, caption=text, reply_markup=kbd)
                bot.register_next_step_handler(send, waiting_for_url)
        else:
            send = bot.send_message(message.chat.id, 'Пришли название!!!')
            bot.register_next_step_handler(send, waiting_for_name)
    else:
        accept_error(message)


def waiting_for_url(message):
    if message.from_user.id in admin_id_list:
        kbd = telebot.types.InlineKeyboardMarkup()
        kbd.add(telebot.types.InlineKeyboardButton(text='Панель админа', callback_data='admin_commands'),
                telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
        text = 'Аниме добавлено.'
        with open(r"media\admin.jpg", "rb") as admin_pic:
            if message.text:
                if message.text.startswith('https://'):
                    anime_url = message.text
                    db.add_anime(ctg=anime_category, name=anime_name, url=anime_url)
                    bot.send_photo(chat_id=message.chat.id, photo=admin_pic, caption=text, reply_markup=kbd)
                else:
                    send = bot.send_message(message.chat.id, 'Пришли ссылку!!!')
                    bot.register_next_step_handler(send, waiting_for_url)
            else:
                send = bot.send_message(message.chat.id, 'Пришли ссылку!!!')
                bot.register_next_step_handler(send, waiting_for_url)
    else:
        accept_error(message)


# --------------------------------------------------- УДАЛЕНИЕ АНИМЕ ---------------------------------------------------
@bot.message_handler(commands=['delete_anime'])
def delete_anime_command(message, is_admin=None):
    bot.clear_step_handler(message)
    if is_admin or message.from_user.id in admin_id_list:
        kbd = telebot.types.InlineKeyboardMarkup()
        for item in db.get_category_list():
            kbd.row(telebot.types.InlineKeyboardButton(text=item, callback_data=item.lower()))
        kbd.add(telebot.types.InlineKeyboardButton(text='Панель админа', callback_data='admin_commands'),
                telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
        text = 'Перед удалением аниме выбери категорию.\nСписок имеющихся категорий:'
        with open(r"media\admin.jpg", "rb") as admin_pic:
            send = bot.send_photo(chat_id=message.chat.id, photo=admin_pic, caption=text, reply_markup=kbd)
            bot.register_next_step_handler(message=send, callback=waiting_for_category_for_delete)
    else:  # если не админ
        accept_error(message)


def waiting_for_category_for_delete(message, is_admin=None, ctg=None):
    global anime_category_for_delete
    if is_admin or message.from_user.id in admin_id_list:
        if message.text or ctg is not None:
            if message.text:
                anime_category_for_delete = message.text
            else:
                anime_category_for_delete = ctg
            kbd = telebot.types.InlineKeyboardMarkup()
            for item in db.get_anime_list(ctg=ctg):
                kbd.row(telebot.types.InlineKeyboardButton(text=item, callback_data=item[:10]))
            kbd.add(telebot.types.InlineKeyboardButton(text='Панель админа', callback_data='admin_commands'),
                    telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
            text = 'Какое аниме будем удалять? ' \
                   'Список имеющихся аниме по категории "' + anime_category_for_delete + '":'
            with open(r"media\admin.jpg", "rb") as admin_pic:
                send = bot.send_photo(chat_id=message.chat.id, photo=admin_pic, caption=text, reply_markup=kbd)
                bot.register_next_step_handler(send, waiting_for_name_for_delete)
        else:
            send = bot.send_message(chat_id=message.chat.id, text='Установи категорию!!!')
            bot.register_next_step_handler(send, waiting_for_category_for_delete)
    else:
        accept_error(message)


def waiting_for_name_for_delete(message, is_admin=None, name=None):
    global anime_name_for_delete
    if is_admin or message.from_user.id in admin_id_list:
        if message.text or name is not None:
            if message.text:
                anime_name_for_delete = message.text
            else:
                anime_name_for_delete = name
            kbd = telebot.types.InlineKeyboardMarkup()
            kbd.add(telebot.types.InlineKeyboardButton(text='Панель админа', callback_data='admin_commands'),
                    telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
            text = 'Аниме удалено.'
            db.delete_anime(name=anime_name_for_delete)
            with open(r"media\admin.jpg", "rb") as admin_pic:
                bot.send_photo(chat_id=message.chat.id, photo=admin_pic, caption=text, reply_markup=kbd)
        else:
            send = bot.send_message(message.chat.id, 'Пришли название!!!')
            bot.register_next_step_handler(send, waiting_for_name_for_delete)
    else:
        accept_error(message)


# Прочие/дополнительные функции ----------------------------------------------------------------------------------------
def get_anime(message, ctg):
    kbd = telebot.types.InlineKeyboardMarkup()
    for n, u in db.get_anime_list_and_refs(ctg=ctg):
        kbd.row(telebot.types.InlineKeyboardButton(text=str(n), url=str(u)))
    kbd.row(telebot.types.InlineKeyboardButton(text='Назад', callback_data='anime_list'))
    kbd.row(telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
    bot.edit_message_caption(caption=ctg, chat_id=message.chat.id, message_id=message.message_id, reply_markup=kbd)


def accept_error(message):
    kbd = telebot.types.InlineKeyboardMarkup()
    kbd.row(telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
    text = 'ТЫ НЕ  ̶А̶Д̶М̶И̶Н̶  ПРОЙДЕШЬ!!!'
    with open(r"media\accept_error.jpg", "rb") as accept_error_pic:
        if message.text:
            bot.send_photo(chat_id=message.chat.id,
                           photo=accept_error_pic,
                           caption=text,
                           reply_markup=kbd)
        else:
            bot.edit_message_media(chat_id=message.chat.id,
                                   message_id=message.message_id,
                                   media=telebot.types.InputMediaPhoto(accept_error_pic))
            bot.edit_message_caption(caption=text,
                                     chat_id=message.chat.id,
                                     message_id=message.message_id,
                                     reply_markup=kbd)


# Обработка запросов ---------------------------------------------------------------------------------------------------
@bot.callback_query_handler(func=lambda c: True)
def all_callbacks(c):

    # Общие команды
    if c.data == 'start':
        start_command(c.message)
    elif c.data == 'help':
        help_command(c.message)
    elif c.data == 'donate':
        donate_command(c.message)
    elif c.data == 'channel':
        channel_command(c.message)
    elif c.data == 'references':
        references_command(c.message)
    elif c.data == 'anime_list':
        anime_list_command(c.message)

    # Админские команды
    elif c.data == 'admin_commands':
        if c.from_user.id in admin_id_list:
            admin_commands_command(c.message, True)
        else:
            accept_error(c.message)
    elif c.data == 'all_commands':
        if c.from_user.id in admin_id_list:
            all_commands_command(c.message, True)
        else:
            accept_error(c.message)
    elif c.data == 'add_new_anime':
        if c.from_user.id in admin_id_list:
            add_new_anime_command(c.message, True)
        else:
            accept_error(c.message)
    elif c.data == 'delete_anime':
        if c.from_user.id in admin_id_list:
            delete_anime_command(c.message, True)
        else:
            accept_error(c.message)

    for ctg in db.get_category_list():
        if c.data == ctg:  # в качестве колбэка принимается категория из БД и она же потом передается в функцию
            get_anime(c.message, ctg)  # вывод аниме для пользователей
        elif c.data == ctg.upper():  # для добавления аниме
            bot.clear_step_handler(message=c.message)
            waiting_for_category(c.message, is_admin=True, ctg=ctg)
        elif c.data == ctg.lower():  # для удаления аниме, 1-й этап
            bot.clear_step_handler(message=c.message)
            waiting_for_category_for_delete(c.message, is_admin=True, ctg=ctg)
        else:
            for anime in db.get_anime_list(ctg=ctg):
                if c.data == anime[:10]:
                    bot.clear_step_handler(message=c.message)
                    waiting_for_name_for_delete(c.message, is_admin=True, name=anime)


# Обработка сообщений --------------------------------------------------------------------------------------------------
@bot.message_handler(content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location', 'contact'])
def text_message(message):
    kbd = telebot.types.InlineKeyboardMarkup()
    kbd.add(telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
    if message.text:
        if message.text.lower() == 'пасхалка':
            bot.send_sticker(message.chat.id, data='CAACAgIAAxkBAAMiXjc3MHuW4Vhz_efkFQKeA8-ppKQAArgAA3uVzxo82SLLmUQS9hgE')
            bot.send_message(message.chat.id, text='Потерялся без кнопочек?)\nВведи /start или /help')
        elif message.text.lower() == 'лена' or message.text.lower() == 'елена' or message.text.lower() == 'orru':
            with open(r"media\lena.jpg", "rb") as lena_pic:
                bot.send_photo(message.chat.id, lena_pic, reply_markup=kbd)
        elif message.text.lower() == 'саша' or message.text.lower() == 'александр' or message.text.lower() == 'airis':
            with open(r"media\sasha.jpg", "rb") as sasha_pic:
                bot.send_photo(message.chat.id, sasha_pic, reply_markup=kbd)
        elif message.text.lower() == 'даша' or message.text.lower() == 'дарья':
            with open(r"media\dasha.jpg", "rb") as dasha_pic:
                bot.send_photo(message.chat.id, dasha_pic, reply_markup=kbd)
        elif message.text.lower() == 'колбаска' or message.text.lower() == 'колбасятина':
            with open(r"media\kolbasyatina.jpg", "rb") as nano_pic:
                bot.send_photo(message.chat.id, nano_pic, reply_markup=kbd)
        else:
            with open(r"media\text_error.jpg", "rb") as text_error_pic:
                bot.send_photo(message.chat.id, text_error_pic, caption='Увы, я не понимаю...', reply_markup=kbd)
    else:
        with open(r"media\text_error.jpg", "rb") as text_error_pic:
            bot.send_photo(message.chat.id, text_error_pic, caption='Увы, я не понимаю...', reply_markup=kbd)


if __name__ == '__main__':
    try:
        bot.polling(none_stop=True, interval=0, timeout=20)
        db.creating_general_table()  # пересоздавать таблицу при запуске кода, когда force=True
    except Exception as E:
        print(E.args)
        time.sleep(2)

