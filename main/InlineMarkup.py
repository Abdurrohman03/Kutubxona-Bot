from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menuStart = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📞 Aloqa", callback_data="Aloqa")
        ],
        [
            InlineKeyboardButton(text="📚Diniy Kitoblar", callback_data="Diniy Kitoblar"),
            InlineKeyboardButton(text="📚Biznes Kitoblar", callback_data="Biznes Kitoblar")
        ],
        [
            InlineKeyboardButton(text="📚Badiiy Kitoblar", callback_data="Badiiy Kitoblar")
        ],
        [
            InlineKeyboardButton(text="📚Bolalar Adabiyoti", callback_data="j1"),
            InlineKeyboardButton(text="📚Mumtoz Adabiyot", callback_data="Mumtoz")
        ],
        [
            InlineKeyboardButton(text="🎧Audio Kitoblar", callback_data="Audio"),
            InlineKeyboardButton(text="💯 Top 100 Kitoblar", callback_data="Top")
        ],
        [
            InlineKeyboardButton(text="⭐ Botni Baholash", callback_data="Baholash")
        ]
    ]
)

Diniymenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Anbiyolar qissasi', callback_data="anbiyolar_qissasi"),
            InlineKeyboardButton(text='Islomda halol va harom', callback_data='halol va harom')
        ],
        [
            InlineKeyboardButton(text='Nasroniy atirguli', callback_data='nasroniy_atirguli'),
            InlineKeyboardButton(text='Iymon va huzun', callback_data='iymon va huzun')
        ],
        [
            InlineKeyboardButton(text='Tafsir 1 - 6 qismlar', callback_data='tafsir'),
            InlineKeyboardButton(text='Uylanish odobi', callback_data='uylanish')
        ],
        [
            InlineKeyboardButton(text='Ulamolar nazdida vaqtning qadri', callback_data='vaqt qadri')
        ],
        [
            InlineKeyboardButton(text='Baxtli hayot sari', callback_data='baxtli xayot'),
            InlineKeyboardButton(text="Istig'forning 40 xosiyati", callback_data="istig'for")
        ],
        [
            InlineKeyboardButton(text="Qur'on qalblar shifosi", callback_data="qur'on")
        ],
        [
            InlineKeyboardButton(text="Asosiy menu", callback_data='menu')
        ]
    ]
)
Biznesmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="10x Marta ko'proq", callback_data='10x'),
            InlineKeyboardButton(text="Alibaba", callback_data="Alibaba")
        ],
        [
            InlineKeyboardButton(text="Boy bola aqqli bola", callback_data='Boy bola'),
            InlineKeyboardButton(text="Boy ota, kambag'al ota", callback_data='Ota')
        ],
        [
            InlineKeyboardButton(text='Innovatorlar', callback_data="Innovatorlar"),
            InlineKeyboardButton(text="Jon kexo: Pul va siz", callback_data="Jon kexo")
        ],
        [
            InlineKeyboardButton(text="Million dollarlik xatolar", callback_data='Million dollar'),
            InlineKeyboardButton(text="Rework", callback_data="Rework")
        ],
        [
            InlineKeyboardButton(text="Stiv Jobs", callback_data="Stiv Jobs"),
            InlineKeyboardButton(text="Vavilonlik eng boy odam", callback_data="Vavilon")
        ],
        [
            InlineKeyboardButton(text="Zero to one", callback_data="0 to 1"),
            InlineKeyboardButton(text="Asosiy menu", callback_data='menu')
        ]
    ]
)
BadiiyMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 O'zbek adabiyoti 🇺🇿", callback_data="Uz adab")
        ],
        [
            InlineKeyboardButton(text="🌍 Jahon adabiyoti 🌍", callback_data="Johon adab")
        ],
        [
            InlineKeyboardButton(text="Asosiy menu", callback_data='menu')
        ]
    ]
)
BadiiyUzmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👤Abdulla Qodiriy", callback_data='Abdulla Qodiriy')
        ],
        [
            InlineKeyboardButton(text="👤Cho'lpon asarlari", callback_data="Cho'lpon"),
            InlineKeyboardButton(text="👤Oybek", callback_data='Oybek')
        ],
        [
            InlineKeyboardButton(text="👤G'afur G'ulom", callback_data="G'afur G'ulom"),
            InlineKeyboardButton(text="👤Abdulla Qahhor", callback_data="Abdulla Qahhor")
        ],
        [
            InlineKeyboardButton(text="👤Said Ahmad", callback_data='Said Ahmad'),
            InlineKeyboardButton(text="👤O'tkir Hoshimov", callback_data="O'tkir Hoshimov")
        ],
        [
            InlineKeyboardButton(text="⬅", callback_data="l1"),
            InlineKeyboardButton(text="➡", callback_data="r1")
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="b3"),
            InlineKeyboardButton(text="Asosiy menu", callback_data="menu")
        ]
    ]
)
BadiiyUz1menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👤Primqul Qodirov", callback_data="Primqul Qodirov"),
            InlineKeyboardButton(text="👤Asqad Muxtor", callback_data="Asqad Muxtor")
        ],
        [
            InlineKeyboardButton(text="👤Odil Yoqubov", callback_data="Odil Yoqubov"),
            InlineKeyboardButton(text="👤Tog'ay Murod", callback_data="Tog'ay Murod")
        ],
        [
            InlineKeyboardButton(text="👤Tohir Malik", callback_data="Tohir Malik"),
            InlineKeyboardButton(text="👤O'lmas Umarbekov", callback_data="O'lmas Umarbekov")
        ],
[
            InlineKeyboardButton(text="⬅", callback_data="l2"),
            InlineKeyboardButton(text="➡", callback_data="r2")
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="b3"),
            InlineKeyboardButton(text="Asosiy menu", callback_data="menu")
        ]
    ]
)
BadiiyJmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👤Lev Tolstoy", callback_data="Lev Tolstoy"),
            InlineKeyboardButton(text="👤Aleksandr Pushkin", callback_data="Pushkin")
        ],
        [
            InlineKeyboardButton(text="👤Fyodor Dostoyevskiy", callback_data="Fyodor Dostoyevskiy"),
            InlineKeyboardButton(text="👤Mixail Bulgakov", callback_data="Mixail Bulgakov")
        ],
        [
            InlineKeyboardButton(text="👤Chingiz Aytmatov", callback_data="Chingiz Aytmatov"),
            InlineKeyboardButton(text="👤Nodar Dumbadze", callback_data="Nodar Dumbadze")
        ],
        [
            InlineKeyboardButton(text="👤Jek London", callback_data="Jek London"),
            InlineKeyboardButton(text="👤Gabriel Garsia Markes", callback_data="Gabriel")
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="b1"),
            InlineKeyboardButton(text="➡ Keyingi", callback_data="k1")
        ],
        [
            InlineKeyboardButton(text="Asosiy menu", callback_data="menu")
        ]
    ]
)
BadiiyJ1Menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👤Alber Kamyu", callback_data="Alber Kamyu"),
            InlineKeyboardButton(text="👤Kobo Abe", callback_data="Kobo Abe")
        ],
        [
            InlineKeyboardButton(text="👤Lao She", callback_data="Lao She"),
            InlineKeyboardButton(text="👤Artur Konan Doyl", callback_data="Artur")
        ],
        [
            InlineKeyboardButton(text="👤Agata Kristi", callback_data="Agata Kristi"),
            InlineKeyboardButton(text="👤Gi De Mopassan", callback_data="Gi De Mopassan")
        ],
        [
            InlineKeyboardButton(text="👤Onor De Balzak", callback_data="Onor De Balzak"),
            InlineKeyboardButton(text="👤Ernest Xeminguey", callback_data="Ernest Xeminguey")
        ],
        [
            InlineKeyboardButton(text="👤Jeyms Joys", callback_data="Jeyms Joys"),
            InlineKeyboardButton(text="👤Jonattan Swift", callback_data="Jonattan Swift")
        ],
        [
            InlineKeyboardButton(text="👤Jyul Vern", callback_data="Jyul Vern"),
            InlineKeyboardButton(text="👤Somerset Moem", callback_data="Somerset Moem")
        ],
        [
            InlineKeyboardButton(text="👤Robindranat Tagor", callback_data="Robindranat Tagor")
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="b2"),
            InlineKeyboardButton(text="⬅ Oldingisi", callback_data="o1")
        ],
        [
            InlineKeyboardButton(text="Asosiy menu", callback_data="menu")
        ]
    ]
)
Bolalarmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📚 Ertaklar", callback_data="Ertaklar")
        ],
        [
            InlineKeyboardButton(text="🤓 Qiziqarli kitoblar | Bolalar ensiklopediyasi", callback_data="Ensiklopedia")
        ],
        [
            InlineKeyboardButton(text="Asosiy menu", callback_data="menu")
        ]
    ]
)


Iks = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="❌", callback_data="❌")
        ]
    ]
)
Mumtozmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📓 Boburnoma", callback_data="Boburnoma")
        ],
        [
            InlineKeyboardButton(text="📓 Shohnoma", callback_data="Shohnoma")
        ],
        [
            InlineKeyboardButton(text="📓 Zarbulmasal", callback_data="Zarbulmasal")
        ],
        [
            InlineKeyboardButton(text="📓 To'rt Ulus tarixi", callback_data="Ulus")
        ],
        [
            InlineKeyboardButton(text="📓 Devoni Lug'otut turk", callback_data="Devon")
        ],
        [
            InlineKeyboardButton(text="📓 Qutadg'u bilig", callback_data="Qutadg'u")
        ],
        [
            InlineKeyboardButton(text="Asosiy menu", callback_data="menu")
        ]
    ]
)
Audiouzmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 Romanlar", callback_data="Romanlaruz")
        ],
        [
            InlineKeyboardButton(text="🇺🇿 Hikoyalar", callback_data="Hikoyalaruz")
        ],
        [
            InlineKeyboardButton(text="Asosiy menu", callback_data="menu")
        ]
    ]
)
Romanuzmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Abdulla Qodiriy - \"O'tgan kunlar\"", callback_data="O'tgan kunlarau")
        ],
        [
            InlineKeyboardButton(text="Abdulla Qodiriy - \"Mehrobdan chayon\"", callback_data="Mehrobdan Chayonau")
        ],
        [
            InlineKeyboardButton(text="Oybek - \"Navoiy\"", callback_data="Navoiyau")
        ],
        [
            InlineKeyboardButton(text="Pirimqul Qodirov - \"Yulduzli tunlar\"", callback_data="Yulduzli tunlar")
        ],
        [
            InlineKeyboardButton(text="Said Ahmad - \"Ufq\"", callback_data="Ufqau")
        ],
        [
            InlineKeyboardButton(text="Tohir Malik - \"Shaytanat\"", callback_data="Shaytanat")
        ],
        [
            InlineKeyboardButton(text="Cho'lpon - \"Kecha va Kunduz\"", callback_data="Kechakunduz")
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="b6")
        ],
        [
            InlineKeyboardButton(text="Asosiy menu", callback_data="menu")
        ]
    ]
)
Qissalaruz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="G'afur G'ulom - \"Shum bola\"", callback_data="Shum bola")
        ],
        [
            InlineKeyboardButton(text="Tog'ay Murod - \"Yulduzlar Mangu Yoanadi\"", callback_data="Yulduzlar mangu yonadi")
        ],
        [
            InlineKeyboardButton(text="Tohir Malik - \"Alvido Bolalik\"", callback_data="Alvido bolalik")
        ],
        [
            InlineKeyboardButton(text="O'tkir Hoshimov - \"Dunyoning Ishlari\"", callback_data="Dunyoning Ishlari")
        ],
[
            InlineKeyboardButton(text="🔙 Ortga", callback_data="b7")
        ],
        [
            InlineKeyboardButton(text="Asosiy menu", callback_data="menu")
        ]
    ]
)

