import config
import telebot
import time

bot = telebot.TeleBot(config.TOKEN)  # Создание экземпляра класса TeleBot
bot.delete_webhook()  # Удаление вэбхука

#user_state = 0  # пользователь в главном меню (т.е. на верхнем уровне)

admin_id_list = [335672004, 377838656, 634780542]

get_old_anime = {
    'Вишневый переполох / Cherry no Manma': 'https://online.anidub.com/anime_ova/10837-vishnevyy-perepoloh-cherry-no-manma.html',
    'Водное поло на грани фола OVA / Hantsu x Trash [3 серия]': 'https://online.anidub.com/xxx/9628-vodnoe-polo-na-grani-fola-ova-hantsu-x-trash.html',
    'Вселенная милашки Хани / Cutie Honey Universe [с 8 серии]': 'https://online.anidub.com/anime/full/10474-vselennaya-milashki-hani-cutie-honey-universe-01-iz-12.html',
    'Геймеры! / Gamers! [с 7 серии]': 'https://online.anidub.com/anime/full/10245-geymery-gamers-01-iz-12.html',
    'Горничные Ханаукё: Истина / Hanaukyou Maid Tai: La Verite [с 10 серии]': 'https://online.anidub.com/anime/full/10512-gornichnye-hanauke-istina-hanaukyou-maid-tai-la-verite-02-iz-12.html'
}
get_movies = {
    'Кикуджиро / Kikujiro': 'https://online.anidub.com/dorama/japan_dorama/11097-kikudziro-kikujiro.html',
    'Отряд «Инфинити» / Gekijouban Infini-T Force: Gatchaman - Saraba Tomo yo': 'https://online.anidub.com/anime_movie/11002-otryad-infiniti-film-gekijouban-infini-t-force-gatchaman-saraba-tomo-yo-movie.html',
    'Годзилла против Разрушителя / Godzilla vs. Destroyer': 'https://online.anidub.com/dorama/japan_dorama/10976-godzilla-protiv-razrushitelya-godzilla-vs-destroyer.html',
    'Годзилла против Кинга Гидоры / Godzilla vs. King Ghidorah': 'https://online.anidub.com/dorama/japan_dorama/10975-godzilla-protiv-kinga-gidory-godzilla-vs-king-ghidorah.html',
    'Годзилла против Космогодзиллы / Godzilla vs. SpaceGodzilla': 'https://online.anidub.com/dorama/japan_dorama/10921-godzilla-protiv-kosmogodzilly-godzilla-vs-spacegodzilla.html',
    'Годзилла против Мехагодзиллы 2 / Godzilla vs. Mechagodzilla II': 'https://online.anidub.com/dorama/japan_dorama/10910-godzilla-protiv-mekagodzilly-2-godzilla-vs-mechagodzilla-ii.html',
    'Годзилла против Мотры: Битва за Землю / Godzilla and Mothra: The Battle for Earth': 'https://online.anidub.com/dorama/japan_dorama/10893-godzilla-protiv-motry-bitva-za-zemlyu-godzilla-and-mothra-the-battle-for-earth.html',
    'Годзилла против Биолланте / Godzilla vs. Biollante': 'https://online.anidub.com/dorama/japan_dorama/10884-godzilla-protiv-biollante-godzilla-vs-biollante.html',
    'Поп и Кью / Pop in Q': 'https://online.anidub.com/anime_movie/10900-pop-i-kyu-pop-in-q-movie.html',
    'Семерка Тринити: Вечная библиотека и Девушка алхимик / Trinity Seven Eternity Library & Alchemic Girl': 'https://online.anidub.com/anime_movie/10745-semerka-triniti-vechnaya-biblioteka-i-devushka-alhimik-trinity-seven-eternity-library-alchemic-girl-movie.html',
    'Макросс Дельта: Страсть Валькирий / Gekijouban Macross Delta: Gekijou no Walkure': 'https://online.anidub.com/anime_movie/10797-makross-delta-strast-valkiriy-gekijouban-macross-delta-gekijou-no-walkure-movie.html',
    'Яйцо ангела / Tenshi no Tamago': 'https://online.anidub.com/anime_ova/10829-yayco-angela-tenshi-no-tamago.html'
}
get_autumn2018 = {
    'Зомбилэнд Сага / Zombieland Saga': 'https://online.anidub.com/anime/full/10637-zombilend-saga-zombieland-saga-01-iz-12.html',
    'Джульетта из Элитной Академии / Kishuku Gakkou no Juliet': 'https://online.anidub.com/anime/full/10635-dzhuletta-iz-elitnoy-akademii-kishuku-gakkou-no-juliet-01-iz-12.html',
    'Девичьи Кричалки / Anima Yell!': 'https://online.anidub.com/anime/full/10652-devichi-krichalki-anima-yell-01-iz-12.html',
    'В итоге я стану твоей / Yagate Kimi ni Naru': 'https://online.anidub.com/anime/full/10639-v-itoge-ya-stanu-tvoey-yagate-kimi-ni-naru-01-iz-13.html',
    'Наша горничная слишком надоедлива! / Uchi no Maid ga Uzasugiru!': 'https://online.anidub.com/anime/full/10644-nasha-gornichnaya-slishkom-nadoedliva-uchi-no-maid-ga-uzasugiru-01-iz-12.html',
    'Агрессивная Рэцуко: Мы желаем вам метал-Рождества / Aggressive Retsuko: We Wish You a Metal Christmas': 'https://online.anidub.com/anime_ova/anime_ona/10710-agressivnaya-recuko-my-zhelaem-vam-metal-rozhdestva-aggressive-retsuko-we-wish-you-a-metal-christmas.html'
}
get_winter2019 = {
    'Ярость Бахамута: Друзья из Манарии / Shingeki no Bahamut: Manaria Friends': 'https://online.anidub.com/anime/full/10700-yarost-bahamuta-druzya-iz-manarii-shingeki-no-bahamut-manaria-friends.html',
    'Пять невест ТВ-1 / Go-Toubun no Hanayome TV-1': 'https://online.anidub.com/anime/full/10740-pyat-nevest-go-toubun-no-hanayome-01-iz-12.html',
    'Эндро! / Endro!': 'https://online.anidub.com/anime/full/10759-endro-endro-01-iz-12.html',
    'Оружейная лавка для леди и джентельменов ONA / Otona no Bouguya-san (Rimen)': 'https://online.anidub.com/anime_ova/anime_ona/10880-oruzheynaya-lavka-dlya-ledi-i-dzhentelmenov-ona-otona-no-bouguya-san-rimen-01-iz-03.html'
}
get_spring2019 = {
    '800 с Хвостиком! / Sewayaki Kitsune no Senko-san': 'https://online.anidub.com/anime/full/10781-800-s-hvostikom-sewayaki-kitsune-no-senko-san-aprel-2019.html',
    'Жизнь в стихах / Senryuu Shoujo': 'https://online.anidub.com/anime/full/10791-zhizn-v-stihah-senryuu-shoujo-aprel-2019.html',
    'Социофобия / Hitoribocchi no Marumaru Seikatsu': 'https://online.anidub.com/anime/full/10774-sociofobiya-hitoribocchi-no-marumaru-seikatsu-aprel-2019.html'
}
get_summer2019 = {
    'Ради своей дочки я даже готов одолеть владыку демонов / Uchi no Ko no Tame naraba, Ore wa Moshikashitara Maou mo Taoseru kamo Shirenai': 'https://online.anidub.com/anime/full/10948-radi-svoey-dochki-ya-dazhe-gotov-odolet-vladyku-demonov-uchi-no-ko-no-tame-naraba-ore-wa-moshikashitara-maou-mo-taoseru-kamo-shirenai-01-iz-12.html',
    'Астра, затерянная в космосе / Kanata no Astra': 'https://online.anidub.com/anime/full/10971-astra-zateryannaya-v-kosmose-kanata-no-astra-01-iz-12.html',
    'Гранбелм / Granbelm': 'https://online.anidub.com/anime/full/10951-granbelm-granbelm-01-iz-12.html',
    'Готов ли ты влюбиться в извращенку до тех пор, пока она милая? / Kawaikereba Hentai demo Suki ni Natte Kuremasu ka?': 'https://online.anidub.com/anime/full/10972-gotov-li-ty-vlyubitsya-v-izvraschenku-do-teh-por-poka-ona-milaya-kawaikereba-hentai-demo-suki-ni-natte-kuremasu-ka-01-iz-12.html',
    'Ментовское ремесло / Cop Craft': 'https://online.anidub.com/anime/ls/10962-mentovskoe-remeslo-cop-craft-01-iz-12.html'
}
get_autumn2019 = {
    'Лазурный путь / Azur Lane': 'https://online.anidub.com/anime/ls/11047-morskoy-gorizont-azur-lane-01-iz-12.html',
    'Ты единственная, кто любит Великого Меня?! / Ore wo Suki na no wa Omae Dake ka yo': 'https://online.anidub.com/anime/ls/11045-ty-edinstvennaya-kto-lyubit-velikogo-menya-ore-o-suki-na-no-wa-omae-dake-ka-yo-01-iz-12.html',
    'Жизнь без оружия / No Guns Life': 'https://online.anidub.com/anime/ls/11077-zhizn-bez-oruzhiya-no-guns-life-01-iz-12.html',
    'Дорога зверя / Hataage! Kemono Michi': 'https://online.anidub.com/anime/ls/11041-doroga-zverya-hataage-kemono-michi-01-iz-13.html',
    'Власть книжного червя: Чтобы стать библиотекарем, все средства хороши ТВ-1 / Honzuki no Gekokujou: Shisho ni Naru Tame ni wa Shudan o Erande Iraremasen TV-1': 'https://online.anidub.com/anime/full/11048-vlast-knizhnogo-chervya-chtoby-stat-bibliotekarem-vse-sredstva-horoshi-honzuki-no-gekokujou-shisho-ni-naru-tame-ni-wa-shudan-o-erande-iraremasen-01-iz-12.html',
    'Гордость убийцы / Assassins Pride': 'https://online.anidub.com/anime/full/11075-gordost-ubiycy-assassins-pride-01-iz-12.html',
    'Разве я не просила, чтобы в ином мире мои навыки были самыми обычными? / Watashi, Nouryoku wa Heikinchi dette Itta yo ne!': 'https://online.anidub.com/anime/full/11068-razve-ya-ne-prosila-chtoby-v-inom-mire-moi-navyki-byli-samymi-obychnymi-watashi-nouryoku-wa-heikinchi-dette-itta-yo-ne-01-iz-12.html',
    'БАНАНЬКА!!! / Bananya: Fushigi na Nakamatachi': 'https://online.anidub.com/anime/full/11049-bananka-bananya-fushigi-na-nakamatachi-13-iz-13.html'
}
get_winter2020 = {
    'Записи о магии: Девочка-волшебница Мадока Волшебство — Гайдэн / Magia Record: Mahou Shoujo Madoka Magica Gaiden': 'https://online.anidub.com/anime/ls/11108-zapisi-o-magii-devochka-volshebnica-madoka-volshebstvo-gayden-magia-record-mahou-shoujo-madoka-magica-gaiden.html',
    'Из тянки в танки: Я не люблю боль, поэтому вложу всё в защиту / Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu': 'https://online.anidub.com/anime/ls/11150-iz-tyanki-v-tanki-ya-ne-lyublyu-bol-poetomu-vlozhu-vse-v-zaschitu-itai-no-wa-iya-nano-de-bougyoryoku-ni-kyokufuri-shitai-to-omoimasu-01-iz-12.html',
    'Древо Безграничного Развития / Infinite Dendrogram': 'https://online.anidub.com/anime/ls/11118-beskonechnyy-dendrogram-infinite-dendrogram-anons.html',
    'Кошачий рай / Nekopara': 'https://online.anidub.com/anime/ls/11151-koshachiy-ray-nekopara-01-iz-12.html',
    '22/7 / Nanabun no Nijuuni': 'https://online.anidub.com/anime/ls/11128-22-7-nanabun-no-nijuuni-01-iz-12.html',
    'Ода "Синнабон" Нобунага / Oda Cinnamon Nobunaga': 'https://online.anidub.com/anime/anime_ongoing/11132-oda-sinnamon-nobunaga-oda-cinnamon-nobunaga-anons.html',
    'Межвидовые рецензенты / Ishuzoku Reviewers': 'https://online.anidub.com/anime/ls/11155-mezhvidovye-recenzenty-ishuzoku-reviewers-01-iz-12.html'
}

main_anime_dict = {
    'Старые/дозвученные за кем-то аниме': 'get_old_anime',
    'Фильмы': 'get_movies',
    'Осенний аниме сезон 2018': 'get_autumn2018',
    'Зимний аниме сезон 2019': 'get_winter2019',
    'Весенний аниме сезон 2019': 'get_spring2019',
    'Летний аниме сезон 2019': 'get_summer2019',
    'Осенний аниме сезон 2019': 'get_autumn2019',
    'Зимний аниме сезон 2020': 'get_winter2020'
}


# Общие команды --------------------------------------------------------------------------------------------------------
@bot.message_handler(commands=['start'])
def start_command(message):
    kbd = telebot.types.InlineKeyboardMarkup()
    kbd.add(telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
    text = 'Привет! {0.first_name} на связи. Чтобы узнать о доступных командах, нажми "В главное меню"'.format(bot.get_me())
    with open(r"media\hello.jpg", "rb") as start_pic:
        if message.text == '/start':
            bot.send_photo(message.chat.id,
                           start_pic,
                           caption=text,
                           parse_mode='html',
                           reply_markup=kbd)
        else:
            bot.edit_message_media(chat_id=message.chat.id,
                                   media=telebot.types.InputMediaPhoto(start_pic),
                                   message_id=message.message_id)
            bot.edit_message_caption(caption=text,
                                     parse_mode='html',
                                     chat_id=message.chat.id,
                                     message_id=message.message_id,
                                     reply_markup=kbd)


@bot.message_handler(commands=['help'])
def help_command(message):
    kbd = telebot.types.InlineKeyboardMarkup()
    kbd.add(telebot.types.InlineKeyboardButton(text='Донаты', callback_data='donate'),
            telebot.types.InlineKeyboardButton(text='Мои соцсети', callback_data='references'))
    kbd.row(telebot.types.InlineKeyboardButton(text='Мой телеграмм-канал', callback_data='channel'))
    kbd.row(telebot.types.InlineKeyboardButton(text='Все релизы в Моей озвучке', callback_data='anime_list'))
    kbd.row(telebot.types.InlineKeyboardButton(text='Настройки (только для админов)', callback_data='settings'))
    kbd.row(telebot.types.InlineKeyboardButton(text='Написать разработчику', url='https://t.me/Jitterbug_Jemboree'))
    with open(r"media\help.jpg", "rb") as help_pic:
        if message.text == '/help':
            bot.send_photo(message.chat.id,
                           help_pic,
                           caption='Главное меню',
                           reply_markup=kbd)
        else:
            bot.edit_message_media(chat_id=message.chat.id,
                                   media=telebot.types.InputMediaPhoto(help_pic),
                                   message_id=message.message_id)
            bot.edit_message_caption(caption='Главное меню',
                                     chat_id=message.chat.id,
                                     message_id=message.message_id,
                                     reply_markup=kbd)


@bot.message_handler(commands=['donate'])  # Можно дописать платежи тг, но пока это невозможно в десктопной версии.
def donate_command(message):
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
            bot.send_photo(message.chat.id,
                           donate_pic,
                           caption=text,
                           parse_mode='html',
                           reply_markup=kbd)
        else:
            bot.edit_message_media(chat_id=message.chat.id,
                                   media=telebot.types.InputMediaPhoto(donate_pic),
                                   message_id=message.message_id)
            bot.edit_message_caption(caption=text,
                                     chat_id=message.chat.id,
                                     message_id=message.message_id,
                                     parse_mode='html',
                                     reply_markup=kbd)


@bot.message_handler(commands=['channel'])
def channel_command(message):
    kbd = telebot.types.InlineKeyboardMarkup()
    kbd.add(telebot.types.InlineKeyboardButton(text='Открыть канал', url='https://t.me/orrubaka'),
            telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
    text = 'Присоединяйся к моему <a href="https://t.me/orrubaka">каналу</a>, где публикуется самая свежая озвучка!'
    with open(r"media\channel.jpg", "rb") as channel_pic:
        if message.text == '/channel':
            bot.send_photo(message.chat.id,
                           channel_pic,
                           caption=text,
                           parse_mode='html',
                           reply_markup=kbd)
        else:
            bot.edit_message_media(chat_id=message.chat.id,
                                   media=telebot.types.InputMediaPhoto(channel_pic),
                                   message_id=message.message_id)
            bot.edit_message_caption(caption=text,
                                     chat_id=message.chat.id,
                                     message_id=message.message_id,
                                     parse_mode='html',
                                     reply_markup=kbd)


@bot.message_handler(commands=['references'])
def references_command(message):
    kbd = telebot.types.InlineKeyboardMarkup()
    kbd.add(telebot.types.InlineKeyboardButton(text='Страница ВК', url='https://vk.com/lenaivanova1998'),
            telebot.types.InlineKeyboardButton(text='Группа ВК', url='https://vk.com/orrubaka'))
    kbd.add(telebot.types.InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/orrubaka'),
            telebot.types.InlineKeyboardButton(text='Канал в Telegram', url='https://t.me/orrubaka'))
    kbd.row(telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
    with open(r"media\references.jpg", "rb") as references_pic:
        if message.text == '/references':
            bot.send_photo(message.chat.id,
                           references_pic,
                           caption='Я в соцсетях:',
                           reply_markup=kbd)
        else:
            bot.edit_message_media(chat_id=message.chat.id,
                                   media=telebot.types.InputMediaPhoto(references_pic),
                                   message_id=message.message_id)
            bot.edit_message_caption(caption='Я в соцсетях:',
                                     chat_id=message.chat.id,
                                     message_id=message.message_id,
                                     reply_markup=kbd)


@bot.message_handler(commands=['anime_list'])
def anime_list_command(message):
    kbd = telebot.types.InlineKeyboardMarkup()
    for i, j in main_anime_dict.items():
        kbd.row(telebot.types.InlineKeyboardButton(text=i, callback_data=j))
    kbd.row(telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
    text = 'Список озвученных тайтлов по категориям и сезонам с ссылками на сайт для просмотра.\n' \
           'ВНИМАНИЕ: перед переходом по ссылкам может потребоваться авторизация на сайте!\n' \
           'Со временем постараемся залить все серии сюда :)'
    with open(r"media\anime_list.jpg", "rb") as anime_list_pic:
        if message.text == '/anime_list':
            bot.send_photo(message.chat.id,
                           anime_list_pic,
                           caption=text,
                           reply_markup=kbd)
        else:
            bot.edit_message_media(chat_id=message.chat.id,
                                   media=telebot.types.InputMediaPhoto(anime_list_pic),
                                   message_id=message.message_id)
            bot.edit_message_caption(caption=text,
                                     chat_id=message.chat.id,
                                     message_id=message.message_id,
                                     reply_markup=kbd)


for val in main_anime_dict.values():
    @bot.message_handler(commands=[val])
    def value_command(message, num=None):
        get_anime(message, num)


# Команды только для админов -------------------------------------------------------------------------------------------
@bot.message_handler(commands=['settings'])
def settings_command(message, is_admin=None):
    if is_admin or message.from_user.id in admin_id_list:
        kbd = telebot.types.InlineKeyboardMarkup()
        kbd.row(telebot.types.InlineKeyboardButton(text='Панель админа', callback_data='admin_commands'))
        kbd.row(telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
        text = 'Добро пожаловать в админку!'
        with open(r"media\admin.jpg", "rb") as admin_pic:
            if message.text == '/settings':
                bot.send_photo(message.chat.id,
                               admin_pic,
                               caption=text,
                               reply_markup=kbd)
            else:
                bot.edit_message_media(chat_id=message.chat.id,
                                       media=telebot.types.InputMediaPhoto(admin_pic),
                                       message_id=message.message_id)
                bot.edit_message_caption(caption=text,
                                         chat_id=message.chat.id,
                                         message_id=message.message_id,
                                         reply_markup=kbd)
    else:
        accept_error(message)


@bot.message_handler(commands=['admin_commands'])
def admin_commands_command(message, is_admin=None):
    if is_admin or message.from_user.id in admin_id_list:
        kbd = telebot.types.InlineKeyboardMarkup()
        kbd.add(telebot.types.InlineKeyboardButton(text='Все команды бота', callback_data='all_commands'),
                telebot.types.InlineKeyboardButton(text='Добавить аниме', callback_data='add_new_anime'))
        kbd.row(telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
        with open(r"media\admin.jpg", "rb") as admin_pic:
            if message.text == '/admin_commands':
                bot.send_photo(message.chat.id,
                               admin_pic,
                               caption='Доступные команды',
                               reply_markup=kbd)
            else:
                bot.edit_message_media(chat_id=message.chat.id,
                                       media=telebot.types.InputMediaPhoto(admin_pic),
                                       message_id=message.message_id)
                bot.edit_message_caption(caption='Доступные команды',
                                         chat_id=message.chat.id,
                                         message_id=message.message_id,
                                         reply_markup=kbd)
    else:
        accept_error(message)


@bot.message_handler(commands=['all_commands'])
def all_commands_command(message, is_admin=None):
    if is_admin or message.from_user.id in admin_id_list:
        kbd = telebot.types.InlineKeyboardMarkup()
        kbd.row(telebot.types.InlineKeyboardButton(text='Панель админа', callback_data='admin_commands'))
        kbd.row(telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
        with open(r"media\admin.jpg", "rb") as admin_pic:
            mess = ''
            for v in main_anime_dict.values():
                mess += '  /' + v + '\n'
            text = 'Список всех команд\n\n' \
                   'Общие:\n\n' \
                   '  /start\n' \
                   '  /help\n' \
                   '  /donate\n' \
                   '  /channel\n' \
                   '  /references\n' \
                   '  /anime_list\n' + mess + '\n' + 'Админские:\n\n' \
                                                     '  /settings\n' \
                                                     '  /admin_commands\n' \
                                                     '  /all_commands\n' \
                                                     '  /add_new_anime'
            if message.text == '/all_commands':
                bot.send_photo(message.chat.id,
                               admin_pic,
                               caption=text,
                               reply_markup=kbd)
            else:
                bot.edit_message_media(chat_id=message.chat.id,
                                       media=telebot.types.InputMediaPhoto(admin_pic),
                                       message_id=message.message_id)
                bot.edit_message_caption(caption=text,
                                         chat_id=message.chat.id,
                                         message_id=message.message_id,
                                         reply_markup=kbd)
    else:  # если не админ
        accept_error(message)


@bot.message_handler(commands=['add_new_anime'])
def add_new_anime_command(message, is_admin=None):
    if is_admin or message.from_user.id in admin_id_list:
        kbd = telebot.types.InlineKeyboardMarkup()
        kbd.row(telebot.types.InlineKeyboardButton(text='Панель админа', callback_data='admin_commands'))
        kbd.row(telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
        text = 'Пришли мне название нового аниме'
        with open(r"media\admin.jpg", "rb") as admin_pic:
            if message.text == '/add_new_anime':
                send = bot.send_photo(message.chat.id,
                                      admin_pic,
                                      caption=text,
                                      reply_markup=kbd)
                bot.register_next_step_handler(message=send, callback=waiting_for_name)
            else:
                bot.edit_message_media(chat_id=message.chat.id,
                                       media=telebot.types.InputMediaPhoto(admin_pic),
                                       message_id=message.message_id)
                send = bot.edit_message_caption(caption=text,
                                                chat_id=message.chat.id,
                                                message_id=message.message_id,
                                                reply_markup=kbd)
                bot.register_next_step_handler(message=send, callback=waiting_for_name)
    else:  # если не админ
        accept_error(message)


# Прочие/дополнительные функции ----------------------------------------------------------------------------------------
def get_anime(message, num=None):
    for key, value in main_anime_dict.items():
        kbd = telebot.types.InlineKeyboardMarkup()
        for i, j in eval(value).items():
            kbd.row(telebot.types.InlineKeyboardButton(text=i, url=j))
        kbd.row(telebot.types.InlineKeyboardButton(text='Назад', callback_data='anime_list'))
        kbd.row(telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
        with open(r"media\anime_list.jpg", "rb") as anime_list_pic:
            if message.text == '/' + value:
                bot.send_photo(message.chat.id, anime_list_pic, caption=key, reply_markup=kbd)
            else:
                if value == num:
                    bot.edit_message_media(chat_id=message.chat.id,
                                           media=telebot.types.InputMediaPhoto(anime_list_pic),
                                           message_id=message.message_id)
                    bot.edit_message_caption(caption=key,
                                             chat_id=message.chat.id,
                                             message_id=message.message_id,
                                             reply_markup=kbd)


def accept_error(message):
    kbd = telebot.types.InlineKeyboardMarkup()
    kbd.row(telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
    with open(r"media\accept_error.jpg", "rb") as accept_error_pic:
        if message.text == '/settings':
            bot.send_photo(message.chat.id,
                           accept_error_pic,
                           caption='ТЫ НЕ  ̶А̶Д̶М̶И̶Н̶  ПРОЙДЕШЬ!!!',
                           reply_markup=kbd)
        else:
            bot.edit_message_media(chat_id=message.chat.id,
                                   media=telebot.types.InputMediaPhoto(accept_error_pic),
                                   message_id=message.message_id)
            bot.edit_message_caption(caption='ТЫ НЕ  ̶А̶Д̶М̶И̶Н̶  ПРОЙДЕШЬ!!!',
                                     chat_id=message.chat.id,
                                     message_id=message.message_id,
                                     reply_markup=kbd)


def waiting_for_name(message):
    if message.from_user.id in admin_id_list:
        global anime_name
        kbd = telebot.types.InlineKeyboardMarkup()
        kbd.row(telebot.types.InlineKeyboardButton(text='Панель админа', callback_data='admin_commands'))
        kbd.row(telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
        text = 'Теперь пришли ссылку на это аниме'
        with open(r"media\admin.jpg", "rb") as admin_pic:
            if message.text:
                anime_name = message.text
                send = bot.send_photo(message.chat.id,
                                      admin_pic,
                                      caption=text,
                                      reply_markup=kbd)
                bot.register_next_step_handler(send, waiting_for_url)
            '''else:
                send = bot.send_message(message.chat.id, 'Пришли название или ничего делать не буду.')
                bot.register_next_step_handler(send, waiting_for_name)'''
    else:
        accept_error(message)


def waiting_for_url(message):
    if message.from_user.id in admin_id_list:
        global anime_url
        kbd = telebot.types.InlineKeyboardMarkup()
        kbd.row(telebot.types.InlineKeyboardButton(text='Панель админа', callback_data='admin_commands'))
        kbd.row(telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
        text = 'Теперь пришли текст команды для вызова этого аниме (без /)'
        with open(r"media\admin.jpg", "rb") as admin_pic:
            if message.text.startswith('https://'):
                anime_url = message.text
                send = bot.send_photo(message.chat.id,
                                      admin_pic,
                                      caption=text,
                                      reply_markup=kbd)
                bot.register_next_step_handler(send, waiting_for_command)
            else:
                bot.send_photo(message.chat.id, admin_pic, 'Это не ссылка!!!', reply_markup=kbd)


def waiting_for_command(message):
    if message.from_user.id in admin_id_list:
        global anime_command
        kbd = telebot.types.InlineKeyboardMarkup()
        kbd.row(telebot.types.InlineKeyboardButton(text='Панель админа', callback_data='admin_commands'))
        kbd.row(telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
        mess = ''
        for k in main_anime_dict.keys():
            mess += '  ' + k + '\n'
        text = 'Теперь выбери категорию для этого аниме:\n\n' + \
               mess + \
               '\nЕсли это новая категория, то пришли мне её название'
        with open(r"media\admin.jpg", "rb") as admin_pic:
            if message.text:
                anime_command = message.text
                send = bot.send_photo(message.chat.id,
                                      admin_pic,
                                      caption=text,
                                      reply_markup=kbd)
                bot.register_next_step_handler(send, waiting_for_category)


def waiting_for_category(message):
    if message.from_user.id in admin_id_list:
        global anime_category
        kbd = telebot.types.InlineKeyboardMarkup()
        kbd.row(telebot.types.InlineKeyboardButton(text='Панель админа', callback_data='admin_commands'))
        kbd.row(telebot.types.InlineKeyboardButton(text='В главное меню', callback_data='help'))
        text = 'Аниме добавлено'
        with open(r"media\admin.jpg", "rb") as admin_pic:
            if message.text:
                for k, v in main_anime_dict.copy().items():
                    if message.text.lower() == k.lower():
                        eval(v)[anime_name] = anime_url
                    else:
                        anime_category = message.text
                        main_anime_dict[anime_category] = anime_command
                        dict(anime_command=anime_url)
                        break
                bot.send_photo(message.chat.id, admin_pic, text, reply_markup=kbd)


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
    if c.data == 'settings':
        if c.from_user.id in admin_id_list:
            settings_command(c.message, True)
        else:
            accept_error(c.message)
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

    for value in main_anime_dict.values():
        if c.data == value:
            value_command(c.message, value)


# Обработка сообщений --------------------------------------------------------------------------------------------------
@bot.message_handler(content_types=['text'])
def text_message(message):
    kbd = telebot.types.InlineKeyboardMarkup()
    kbd.add(telebot.types.InlineKeyboardButton(text='Меню', callback_data='help'))
    if message.text.lower() == 'пасхалка':
        bot.send_sticker(message.chat.id, data='CAACAgIAAxkBAAMiXjc3MHuW4Vhz_efkFQKeA8-ppKQAArgAA3uVzxo82SLLmUQS9hgE')
        bot.send_message(message.chat.id, text='Потерялся без кнопочек?)\nВведи /start или /help')
    elif message.text.lower() == 'лена' or message.text.lower() == 'елена':
        with open(r"media\lena.jpg", "rb") as lena_pic:
            bot.send_photo(message.chat.id, lena_pic, reply_markup=kbd)
    elif message.text.lower() == 'саша' or message.text.lower() == 'александр':
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
            bot.send_photo(message.chat.id, text_error_pic, caption='Увы, я не понимаю. Используй команды.', reply_markup=kbd)


if __name__ == '__main__':
    try:
        bot.polling(none_stop=True, interval=0, timeout=20)
    except Exception as E:
        print(E.args)
        time.sleep(2)


'''
Добавить для админов:
    - добавление кнопки нового аниме сезона;
Обработка прочего контента (+ доработать текстовую обработку)

категорию
название
команда вызова
ссылка
'''