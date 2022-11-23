from aiogram import executor
from aiogram.types import Message, CallbackQuery
from config import dp
from InlineMarkup import *
from ReplyKey import *


# MenuStart --->
@dp.message_handler(commands='start')
async def start(msg: Message):
    text = f"Assalomu alaykum {msg.from_user.full_name}!\nBizning Kutubxonamizga xush kelibsiz!\n" \
           f"Kitob turini tanlang!"
    img = open("Image/start1.jpg", 'rb')
    await msg.answer_photo(img, caption=text, reply_markup=menuStart)


@dp.message_handler(text="Menu")
async def start(msg: Message):
    await msg.answer_photo(open("Image/start1.jpg", "rb"), reply_markup=menuStart)


@dp.message_handler(commands='help')
async def help1(msg: Message):
    text = f"Yordam uchun https://t.me/Hello_this_isAbdurrohman profiliga bog'laning"
    img = open("Image/Help.jpg", 'rb')
    await msg.answer_photo(img, caption=text, reply_markup=menuStart)


@dp.callback_query_handler(text_contains='Aloqa')
async def help1(call: CallbackQuery):
    text = f"Yordam va takliflar uchun https://t.me/Hello_this_isAbdurrohman profiliga bog'laning"
    img = open("Image/Help.jpg", 'rb')
    await call.message.answer_photo(img, caption=text, reply_markup=menuStart)
    await call.message.delete()


@dp.callback_query_handler(text_contains="Badiiy Kitoblar")
async def start(call: CallbackQuery):
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=BadiiyMenu)
    await call.message.delete()


@dp.callback_query_handler(text_contains="Diniy Kitoblar")
async def start(call: CallbackQuery):
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Diniymenu)
    await call.message.delete()


@dp.callback_query_handler(text_contains="Biznes Kitoblar")
async def start(call: CallbackQuery):
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Biznesmenu)
    await call.message.delete()


@dp.callback_query_handler(text_contains="Mumtoz")
async def start(call: CallbackQuery):
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Mumtozmenu)
    await call.message.delete()


@dp.callback_query_handler(text_contains="Audio")
async def start(call: CallbackQuery):
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Audiouzmenu)
    await call.message.delete()


@dp.callback_query_handler(text_contains="Top")
async def start(call: CallbackQuery):
    await call.message.answer_document(open("Books/AudioKitob/Romanuz/100 kitob.txt", "rb"), reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=menuStart)
    await call.message.delete()


@dp.callback_query_handler(text_contains="Baholash")
async def start(call: CallbackQuery):
    await call.message.answer("Botni Baholang", reply_markup=baholash)
    await call.message.delete()


# DiniyMenu --->
@dp.callback_query_handler(text_contains="anbiyolar_qissasi")
async def diniy(call: CallbackQuery):
    await call.message.answer_document(open("Books/Diniy/Anbiyolar qissasi.pdf", "rb"),
                                       f"Alloh ilmingizni ziyoda qilsin", reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Diniymenu)
    await call.message.delete()


@dp.message_handler(text=["anbiyolar_qissasi", "Anbiyolar qissasi", "anbiyolar qissasi", "anbiyolar", "qissasi"])
async def diniy(message: Message):
    await message.answer_document(open("Books/Diniy/Anbiyolar qissasi.pdf", "rb"),
                                  f"Alloh ilmingizni ziyoda qilsin", reply_markup=menu)


@dp.callback_query_handler(text_contains="halol va harom")
async def diniy(call: CallbackQuery):
    await call.message.answer_document(open("Books/Diniy/Islomda halol va  harom.pdf", "rb"),
                                       f"Alloh ilmingizni ziyoda qilsin", reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Diniymenu)
    await call.message.delete()


@dp.message_handler(text=["halol va harom", "halol", "harom", "Halol va Harom"])
async def diniy(message: Message):
    await message.answer_document(open("Books/Diniy/Islomda halol va  harom.pdf", "rb"),
                                  f"Alloh ilmingizni ziyoda qilsin", reply_markup=menu)


@dp.callback_query_handler(text_contains="nasroniy_atirguli")
async def diniy(call: CallbackQuery):
    await call.message.answer_document(open("Books/Diniy/Nasroniy_atirguli.pdf", "rb"),
                                       f"Alloh ilmingizni ziyoda qilsin", reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Diniymenu)
    await call.message.delete()


@dp.message_handler(text=["nasroniy_atirguli", "Nasroniy atirguli", "nasroniy", "atirgul"])
async def diniy(message: Message):
    await message.answer_document(open("Books/Diniy/Nasroniy_atirguli.pdf", "rb"),
                                  f"Alloh ilmingizni ziyoda qilsin", reply_markup=menu)


@dp.callback_query_handler(text_contains="iymon va huzun")
async def diniy(call: CallbackQuery):
    await call.message.answer_document(open("Books/Diniy/Saida Chamlija_Iymon va huzun.pdf", "rb"),
                                       f"Alloh ilmingizni ziyoda qilsin", reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Diniymenu)
    await call.message.delete()


@dp.message_handler(text=["iymon va huzun", "Iymon va Huzun", "Iymon", "iymon"])
async def diniy(message: Message):
    await message.answer_document(open("Books/Diniy/Saida Chamlija_Iymon va huzun.pdf", "rb"),
                                  f"Alloh ilmingizni ziyoda qilsin", reply_markup=menu)


@dp.callback_query_handler(text_contains="tafsir")
async def diniy(call: CallbackQuery):
    await call.message.answer_document(open("Books/Diniy/Tafsir 1 juz.pdf", "rb"),
                                       f"Alloh ilmingizni")
    await call.message.answer_document(open("Books/Diniy/Tafsir 2 juz.pdf", "rb"),
                                       f"Alloh ilmingizni")
    await call.message.answer_document(open("Books/Diniy/Tafsir 3 juz.pdf", "rb"),
                                       f"Alloh ilmingizni")
    await call.message.answer_document(open("Books/Diniy/Tafsir 4 juz.pdf", "rb"),
                                       f"Alloh ilmingizni")
    await call.message.answer_document(open("Books/Diniy/Tafsir 5 juz.pdf", "rb"),
                                       f"Alloh ilmingizni")
    await call.message.answer_document(open("Books/Diniy/Tafsir 6 juz.pdf", "rb"),
                                       f"Alloh ilmingizni ziyoda qilsin", reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Diniymenu)
    await call.message.delete()


@dp.message_handler(text=["tafsir", "Tafsir"])
async def diniy(message: Message):
    await message.answer_document(open("Books/Diniy/Tafsir 1 juz.pdf", "rb"),
                                  f"Alloh ilmingizni", reply_markup=Iks)
    await message.answer_document(open("Books/Diniy/Tafsir 2 juz.pdf", "rb"),
                                  f"Alloh ilmingizni", reply_markup=Iks)
    await message.answer_document(open("Books/Diniy/Tafsir 3 juz.pdf", "rb"),
                                  f"Alloh ilmingizni", reply_markup=Iks)
    await message.answer_document(open("Books/Diniy/Tafsir 4 juz.pdf", "rb"),
                                  f"Alloh ilmingizni", reply_markup=Iks)
    await message.answer_document(open("Books/Diniy/Tafsir 5 juz.pdf", "rb"),
                                  f"Alloh ilmingizni", reply_markup=Iks)
    await message.answer_document(open("Books/Diniy/Tafsir 6 juz.pdf", "rb"),
                                  f"Alloh ilmingizni ziyoda qilsin", reply_markup=menu)


@dp.callback_query_handler(text_contains="uylanish")
async def diniy(call: CallbackQuery):
    await call.message.answer_document(open("Books/Diniy/Uylanish odobi [@kitoblar_pdf].pdf", "rb"),
                                       f"Alloh ilmingizni ziyoda qilsin", reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Diniymenu)
    await call.message.delete()


@dp.message_handler(text=["uylanish", "Uylanish"])
async def diniy(message: Message):
    await message.answer_document(open("Books/Diniy/Uylanish odobi [@kitoblar_pdf].pdf", "rb"),
                                  f"Alloh ilmingizni ziyoda qilsin", reply_markup=menu)


@dp.callback_query_handler(text_contains="vaqt qadri")
async def diniy(call: CallbackQuery):
    await call.message.answer_document(open("Books/Diniy/Ulamolar nazdida vaqtning qadri.pdf", "rb"),
                                       f"Alloh ilmingizni ziyoda qilsin", reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Diniymenu)
    await call.message.delete()


@dp.message_handler(text=["vaqt qadri", "Vaqt qadri", "Vaqt"])
async def diniy(message: Message):
    await message.answer_document(open("Books/Diniy/Ulamolar nazdida vaqtning qadri.pdf", "rb"),
                                  f"Alloh ilmingizni ziyoda qilsin", reply_markup=menu)


@dp.callback_query_handler(text_contains="baxtli xayot")
async def diniy(call: CallbackQuery):
    await call.message.answer_document(open("Books/Diniy/Tafsir/Baxtli hayot sari.pdf", "rb"),
                                       f"Alloh ilmingizni ziyoda qilsin", reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Diniymenu)
    await call.message.delete()


@dp.message_handler(text=["baxtli xayot", "Baxtli xayot"])
async def diniy(message: Message):
    await message.answer_document(open("Books/Diniy/Tafsir/Baxtli hayot sari.pdf", "rb"),
                                  f"Alloh ilmingizni ziyoda qilsin", reply_markup=menu)


@dp.callback_query_handler(text_contains="istig'for")
async def diniy(call: CallbackQuery):
    await call.message.answer_document(open("Books/Diniy/Tafsir/Istig forning 40 xosiyati. Salovotlar.pdf", "rb"),
                                       f"Alloh ilmingizni ziyoda qilsin", reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Diniymenu)
    await call.message.delete()


@dp.message_handler(text=["istig'for", "Istig'for"])
async def diniy(msg: Message):
    await msg.answer_document(open("Books/Diniy/Tafsir/Istig forning 40 xosiyati. Salovotlar.pdf", "rb"),
                              f"Alloh ilmingizni ziyoda qilsin", reply_markup=menu)


@dp.callback_query_handler(text_contains="qur'on")
async def diniy(call: CallbackQuery):
    await call.message.answer_document(open("Books/Diniy/Tafsir/Ziyovuddin Rahim. Qur'on - qalblar shifosi.pdf", "rb"),
                                       f"Alloh ilmingizni ziyoda qilsin", reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Diniymenu)
    await call.message.delete()


@dp.message_handler(text=["qur'on", "Qur'on"])
async def diniy(msg: Message):
    await msg.answer_document(open("Books/Diniy/Tafsir/Ziyovuddin Rahim. Qur'on - qalblar shifosi.pdf", "rb"),
                              f"Alloh ilmingizni ziyoda qilsin", reply_markup=menu)


# MenuBiznes --->
@dp.callback_query_handler(text_contains="10x")
async def biznes(call: CallbackQuery):
    await call.message.answer_document(open("Books/Biznes/10x marta ko'proq [ @biznes_kitob ].pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Biznesmenu)
    await call.message.delete()


@dp.message_handler(text="10x")
async def biznes(msg: Message):
    await msg.answer_document(open("Books/Biznes/10x marta ko'proq [ @biznes_kitob ].pdf", "rb"),
                              reply_markup=menu)


@dp.callback_query_handler(text_contains="Alibaba")
async def biznes(call: CallbackQuery):
    await call.message.answer_document(open("Books/Biznes/Alibaba.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Biznesmenu)
    await call.message.delete()


@dp.message_handler(text="Alibaba")
async def biznes(msg: Message):
    await msg.answer_document(open("Books/Biznes/Alibaba.pdf", "rb"),
                              reply_markup=menu)


@dp.callback_query_handler(text_contains="Boy bola")
async def biznes(call: CallbackQuery):
    await call.message.answer_document(open("Books/Biznes/Boy bola aqlli bola.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Biznesmenu)
    await call.message.delete()


@dp.message_handler(text="Boy bola")
async def biznes(msg: Message):
    await msg.answer_document(open("Books/Biznes/Boy bola aqlli bola.pdf", "rb"),
                              reply_markup=menu)


@dp.callback_query_handler(text_contains="Ota")
async def biznes(call: CallbackQuery):
    await call.message.answer_document(open("Books/Biznes/Boy ota, kambag'al ota.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Biznesmenu)
    await call.message.delete()


@dp.message_handler(text="Ota")
async def biznes(msg: Message):
    await msg.answer_document(open("Books/Biznes/Boy ota, kambag'al ota.pdf", "rb"),
                              reply_markup=menu)


@dp.callback_query_handler(text_contains="Innovatorlar")
async def biznes(call: CallbackQuery):
    await call.message.answer_document(open("Books/Biznes/innovatorlar.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Biznesmenu)
    await call.message.delete()


@dp.message_handler(text="Innovatorlar")
async def biznes(msg: Message):
    await msg.answer_document(open("Books/Biznes/innovatorlar.pdf", "rb"),
                              reply_markup=menu)


@dp.callback_query_handler(text_contains="Jon kexo")
async def biznes(call: CallbackQuery):
    await call.message.answer_document(open("Books/Biznes/Jon Kexo Pul muvaffaqiyat va siz.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Biznesmenu)
    await call.message.delete()


@dp.message_handler(text="Jon kexo")
async def biznes(msg: Message):
    await msg.answer_document(open("Books/Biznes/Jon Kexo Pul muvaffaqiyat va siz.pdf", "rb"),
                              reply_markup=menu)


@dp.callback_query_handler(text_contains="Million dollar")
async def biznes(call: CallbackQuery):
    await call.message.answer_document(open("Books/Biznes/Million_dollarlik_xatolar.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Biznesmenu)
    await call.message.delete()


@dp.message_handler(text="Million dollar")
async def biznes(msg: Message):
    await msg.answer_document(open("Books/Biznes/Million_dollarlik_xatolar.pdf", "rb"),
                              reply_markup=menu)


@dp.callback_query_handler(text_contains="Rework")
async def biznes(call: CallbackQuery):
    await call.message.answer_document(open("Books/Biznes/REWORK [ @biznes_kitob ].pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Biznesmenu)
    await call.message.delete()


@dp.message_handler(text="Rework")
async def biznes(msg: Message):
    await msg.answer_document(open("Books/Biznes/REWORK [ @biznes_kitob ].pdf", "rb"),
                              reply_markup=menu)


@dp.callback_query_handler(text_contains="Stiv Jobs")
async def biznes(call: CallbackQuery):
    await call.message.answer_document(open("Books/Biznes/StiveJobs.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Biznesmenu)
    await call.message.delete()


@dp.message_handler(text="Stiv Jobs")
async def biznes(msg: Message):
    await msg.answer_document(open("Books/Biznes/StiveJobs.pdf", "rb"),
                              reply_markup=menu)


@dp.callback_query_handler(text_contains="Vavilon")
async def biznes(call: CallbackQuery):
    await call.message.answer_document(open("Books/Biznes/Vavilonlik eng boy odam - Vavilonlik eng boy odam.PDF", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Biznesmenu)
    await call.message.delete()


@dp.message_handler(text="Vavilon")
async def biznes(msg: Message):
    await msg.answer_document(open("Books/Biznes/Vavilonlik eng boy odam - Vavilonlik eng boy odam.PDF", "rb"),
                              reply_markup=menu)


@dp.callback_query_handler(text_contains="0 to 1")
async def biznes(call: CallbackQuery):
    await call.message.answer_document(open("Books/Biznes/Zero to One.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Biznesmenu)
    await call.message.delete()


@dp.message_handler(text="0 to 1")
async def biznes(msg: Message):
    await msg.answer_document(open("Books/Biznes/Zero to One.pdf", "rb"),
                              reply_markup=menu)


# MenuBadiiy --->
@dp.callback_query_handler(text_contains="Uz adab")
async def start(call: CallbackQuery):
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=BadiiyUzmenu)
    await call.message.delete()


@dp.callback_query_handler(text_contains="Johon adab")
async def start(call: CallbackQuery):
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=BadiiyJmenu)
    await call.message.delete()


# menuUzBadiiy --->
@dp.callback_query_handler(text_contains="Abdulla Qodiriy")
async def badiiy(call: CallbackQuery):
    await call.message.answer_document(open("Books/Badiiy/Abdulla Qodiriy. Jinlar bazmi (hikoyalar).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Abdulla Qodiriy. Diyori bakr.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/[@Elektron_kutubxona_kitoblarbot] Baxtsiz kuyov.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Abdulla Qodiriy. Mehrobdan chayon (roman).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jinlar bazmi(Abdulla Qodiriy).apk", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Abdulla Qodiriy. Ijod mashaqqati.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/O'tkan Kunlar (Abdulla Qodiriy).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=BadiiyUzmenu)
    await call.message.delete()


@dp.message_handler(text="Abdulla Qodiriy")
async def badiiy(msg: Message):
    await msg.answer_document(open("Books/Badiiy/Abdulla Qodiriy. Jinlar bazmi (hikoyalar).pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Abdulla Qodiriy. Diyori bakr.pdf", "rb"), reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/[@Elektron_kutubxona_kitoblarbot] Baxtsiz kuyov.pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Abdulla Qodiriy. Mehrobdan chayon (roman).pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Jinlar bazmi(Abdulla Qodiriy).apk", "rb"), reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Abdulla Qodiriy. Ijod mashaqqati.pdf", "rb"), reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/O'tkan Kunlar (Abdulla Qodiriy).pdf", "rb"), reply_markup=menu)


@dp.callback_query_handler(text_contains="Cho'lpon")
async def badiiy(call: CallbackQuery):
    await call.message.answer_document(open("Books/Badiiy/Kecha va kunduz (roman)_Sever.UZ.apk", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Cho'lpon. Kecha va kunduz (roman).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Abdulhamid Cho'lpon. Buloqlar quchog'ida.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/[@Elektron_kutubxona_kitoblarbot] Cho lpon. Hikoyalar, tarji.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyUzmenu)
    await call.message.delete()


@dp.message_handler(text="Cho'lpon")
async def badiiy(msg: Message):
    await msg.answer_document(open("Books/Badiiy/Kecha va kunduz (roman)_Sever.UZ.apk", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Cho'lpon. Kecha va kunduz (roman).pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Abdulhamid Cho'lpon. Buloqlar quchog'ida.pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(
        open("Books/Badiiy/[@Elektron_kutubxona_kitoblarbot] Cho lpon. Hikoyalar, tarji.pdf", "rb"), reply_markup=menu)


@dp.callback_query_handler(text_contains="Oybek")
async def badiiy(call: CallbackQuery):
    await call.message.answer_document(open("Books/Badiiy/Oybek. Bolalik (xotira-qissa).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Oybek. Bola Alisher (qissa).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Oybek. Quyosh qoraymas (roman).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/[@Elektron_kutubxona_kitoblarbot] Oltin vodiydan shabadalar.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/[@Elektron_kutubxona_kitoblarbot] Qutlug  qon.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Oybek. Ulug‘ yo‘l (roman).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyUzmenu)
    await call.message.delete()


@dp.message_handler(text="Oybek")
async def badiiy(msg: Message):
    await msg.answer_document(open("Books/Badiiy/Oybek. Bolalik (xotira-qissa).pdf", "rb"), reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Oybek. Bola Alisher (qissa).pdf", "rb"), reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Oybek. Quyosh qoraymas (roman).pdf", "rb"), reply_markup=Iks)
    await msg.answer_document(
        open("Books/Badiiy/[@Elektron_kutubxona_kitoblarbot] Oltin vodiydan shabadalar.pdf", "rb"), reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/[@Elektron_kutubxona_kitoblarbot] Qutlug  qon.pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Oybek. Ulug‘ yo‘l (roman).pdf", "rb"), reply_markup=menu)


@dp.callback_query_handler(text_contains="G'afur G'ulom")
async def badiiy(call: CallbackQuery):
    await call.message.answer_document(open("Books/Badiiy/[@Elektron_kutubxona_kitoblarbot] Shum bola.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/[@Elektron_kutubxona_kitoblarbot] Netay.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/G'afur G'ulom. Muxbir sudi (pyesa).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/G'afur G'ulom. Qayda baxt (komediya).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/G'afur G'ulom. Yodgor (qissa).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/G'afur G'ulom.pptx", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/XX_asr_ozbek_sheriyati_Gafur_Gulom._Sherlar.avi", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyUzmenu)
    await call.message.delete()


@dp.message_handler(text="G'afur G'ulom")
async def badiiy(msg: Message):
    await msg.answer_document(open("Books/Badiiy/[@Elektron_kutubxona_kitoblarbot] Shum bola.pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/[@Elektron_kutubxona_kitoblarbot] Netay.pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/G'afur G'ulom. Muxbir sudi (pyesa).pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/G'afur G'ulom. Qayda baxt (komediya).pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/G'afur G'ulom. Yodgor (qissa).pdf", "rb"), reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/G'afur G'ulom.pptx", "rb"), reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/XX_asr_ozbek_sheriyati_Gafur_Gulom._Sherlar.avi", "rb"),
                              reply_markup=menu)


@dp.callback_query_handler(text_contains="Abdulla Qahhor")
async def badiiy(call: CallbackQuery):
    await call.message.answer_document(open("Books/Badiiy/Abdulla Qahhor. Oltin yulduz (qissa).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Abdulla Qahhor. Sinchalak (qissa).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Abdulla Qahhor. O'tmishdan ertaklar (qissa).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Abdulla Qahhor. Sarob (roman).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Adabiyotimiz faxri (Abdulla Qahhor).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/10.Abdulla Qahhor - Hikoyalar to'plami.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Abdulla Qahhor. Tanlangan asarlar. 4-jild.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Ozod Sharafiddinov. Abdulla Qahhor.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Abdulla Qahhor - Sarob (roman).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Abdulla Qahhor Asarlar 3-jild.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyUzmenu)
    await call.message.delete()


@dp.message_handler(text="Abdulla Qahhor")
async def badiiy(msg: Message):
    await msg.answer_document(open("Books/Badiiy/Abdulla Qahhor. Oltin yulduz (qissa).pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Abdulla Qahhor. Sinchalak (qissa).pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Abdulla Qahhor. O'tmishdan ertaklar (qissa).pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Abdulla Qahhor. Sarob (roman).pdf", "rb"), reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Adabiyotimiz faxri (Abdulla Qahhor).pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/10.Abdulla Qahhor - Hikoyalar to'plami.pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Abdulla Qahhor. Tanlangan asarlar. 4-jild.pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Ozod Sharafiddinov. Abdulla Qahhor.pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Abdulla Qahhor - Sarob (roman).pdf", "rb"), reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Abdulla Qahhor Asarlar 3-jild.pdf", "rb"), reply_markup=menu)


@dp.callback_query_handler(text_contains="Said Ahmad")
async def badiiy(call: CallbackQuery):
    await call.message.answer_document(open("Books/Badiiy/''Ufq''.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Said Ahmad. Sobiq o'g'ri (hikoyalar).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Said Ahmad. Ta'zim (hikoyalar).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Said Ahmad. Cho'l burguti (hikoyalar).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Said Ahmad. Jimjitlik (roman).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Kiprikda qolgan tong Java.UZ.apk", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Said Ahmad. Kiprikda qolgan tong (qissa).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Said Ahmad. Yo'qotganlarim va topganlarim_2.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/10-sinf Adabiyot slayd. Said Ahmad hayoti va ijodi.ppt", "rb"), reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyUzmenu)
    await call.message.delete()


@dp.message_handler(text="Said Ahmad")
async def badiiy(msg: Message):
    await msg.answer_document(open("Books/Badiiy/''Ufq''.pdf", "rb"), reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Said Ahmad. Sobiq o'g'ri (hikoyalar).pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Said Ahmad. Ta'zim (hikoyalar).pdf", "rb"), reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Said Ahmad. Cho'l burguti (hikoyalar).pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Said Ahmad. Jimjitlik (roman).pdf", "rb"), reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Kiprikda qolgan tong Java.UZ.apk", "rb"), reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Said Ahmad. Kiprikda qolgan tong (qissa).pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Said Ahmad. Yo'qotganlarim va topganlarim_2.pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(
        open("Books/Badiiy/10-sinf Adabiyot slayd. Said Ahmad hayoti va ijodi.ppt", "rb"), reply_markup=menu)


@dp.callback_query_handler(text_contains="O'tkir Hoshimov")
async def badiiy(call: CallbackQuery):
    await call.message.answer_document(open("Books/Badiiy/O'tkir Hoshimov. Nur borki, soya bor (roman).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/O'tkir Hoshimov. Sevgi qissalari.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Dunyoning ishlari bestfayl.net.apk", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Ikki eshik orasi O'tkir Hoshimov.apk", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/O'tkir Hoshimov Dunyoning ishlari.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/O'tkir Hoshimov. Sevgi qissalari.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Ikki eshik orasi O'tkir Hoshimov.apk", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyUzmenu)
    await call.message.delete()


@dp.message_handler(text="O'tkir Hoshimov")
async def badiiy(msg: Message):
    await msg.answer_document(open("Books/Badiiy/O'tkir Hoshimov. Nur borki, soya bor (roman).pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/O'tkir Hoshimov. Sevgi qissalari.pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Dunyoning ishlari bestfayl.net.apk", "rb"), reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Ikki eshik orasi O'tkir Hoshimov.apk", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/O'tkir Hoshimov Dunyoning ishlari.pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/O'tkir Hoshimov. Sevgi qissalari.pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Ikki eshik orasi O'tkir Hoshimov.apk", "rb"),
                              reply_markup=menu)


@dp.callback_query_handler(text_contains="Primqul Qodirov")
async def badiiy(call: CallbackQuery):
    await call.message.answer_document(open("Books/Badiiy/Pirimqul Qodirov. Erk (qissa).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Pirimqul Qodirov. Avlodlar dovoni (roman).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Pirimqul Qodirov. Ona lochin nidosi (roman).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Pirimqul Qodirov. Qora ko'zlar (roman).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Pirimqul Qodirov. Yulduzli tunlar (roman).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyUz1menu)
    await call.message.delete()


@dp.message_handler(text="Primqul Qodirov")
async def badiiy(msg: Message):
    await msg.answer_document(open("Books/Badiiy/Pirimqul Qodirov. Erk (qissa).pdf", "rb"), reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Pirimqul Qodirov. Avlodlar dovoni (roman).pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Pirimqul Qodirov. Ona lochin nidosi (roman).pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Pirimqul Qodirov. Qora ko'zlar (roman).pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Pirimqul Qodirov. Yulduzli tunlar (roman).pdf", "rb"),
                              reply_markup=Iks)


@dp.callback_query_handler(text_contains="Asqad Muxtor")
async def badiiy(call: CallbackQuery):
    await call.message.answer_document(open("Books/Badiiy/Asqad Muxtor. Ildizlar (qissa).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Asqad Muxtor. Ildizlar (qissalar va hikoyalar).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Asqad Muxtor. Jar yoqasidagi chaqmoq (qissa).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Asqad Muxtor. Bo'ronlarda bordek halovat (qissa).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyUz1menu)
    await call.message.delete()


@dp.message_handler(text="Asqad Muxtor")
async def badiiy(msg: Message):
    await msg.answer_document(open("Books/Badiiy/Asqad Muxtor. Ildizlar (qissa).pdf", "rb"), reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Asqad Muxtor. Ildizlar (qissalar va hikoyalar).pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Asqad Muxtor. Jar yoqasidagi chaqmoq (qissa).pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Asqad Muxtor. Bo'ronlarda bordek halovat (qissa).pdf", "rb"),
                              reply_markup=Iks)


@dp.callback_query_handler(text_contains="Odil Yoqubov")
async def badiiy(call: CallbackQuery):
    await call.message.answer_document(open("Books/Badiiy/[@kitoblar1] Urush va qismat.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Odil Yoqubov. Adolat manzili (roman).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Odil Yoqubov. Dastlabki qadam (hikoyalar).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Odil Yoqubov. Billur qandillar (qissa).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Odil Yoqubov. Muqaddas (qissa).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Odil Yoqubov. Ulug'bek xazinasi (roman).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyUz1menu)
    await call.message.delete()


@dp.message_handler(text="Odil Yoqubov")
async def badiiy(msg: Message):
    await msg.answer_document(open("Books/Badiiy/[@kitoblar1] Urush va qismat.pdf", "rb"), reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Odil Yoqubov. Adolat manzili (roman).pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Odil Yoqubov. Dastlabki qadam (hikoyalar).pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Odil Yoqubov. Billur qandillar (qissa).pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Odil Yoqubov. Muqaddas (qissa).pdf", "rb"), reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Odil Yoqubov. Ulug'bek xazinasi (roman).pdf", "rb"),
                              reply_markup=Iks)


@dp.callback_query_handler(text_contains="Tog'ay Murod")
async def badiiy(call: CallbackQuery):
    await call.message.answer_document(open("Books/Badiiy/Tog'ay Murod.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Tog'ay Murod. Qo'shiq (qissalar).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Tog'ay Murod. Ot kishnagan oqshom (qissa).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Tog'ay Murod. Otamdan qolgan dalalar (roman).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Tog'ay Murod. Oydinda yurgan odamlar (qissa).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyUz1menu)
    await call.message.delete()


@dp.message_handler(text="Tog'ay Murod")
async def badiiy(msg: Message):
    await msg.answer_document(open("Books/Badiiy/Tog'ay Murod.pdf", "rb"), reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Tog'ay Murod. Qo'shiq (qissalar).pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Tog'ay Murod. Ot kishnagan oqshom (qissa).pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Tog'ay Murod. Otamdan qolgan dalalar (roman).pdf", "rb"),
                              reply_markup=Iks)
    await msg.answer_document(open("Books/Badiiy/Tog'ay Murod. Oydinda yurgan odamlar (qissa).pdf", "rb"),
                              reply_markup=Iks)


@dp.callback_query_handler(text_contains="Tohir Malik")
async def badiiy(call: CallbackQuery):
    await call.message.answer_document(open("Books/Badiiy/Tohir Malik Nomus va Qasos.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Tohir Malik. Murdalar gapirmaydilar.apk", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Tohir Malik-Shaytanat 5-kitob.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Tohir Malik.(@KITOB) Davron (qissa).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Tohir Malik.(@KITOB)Eng kichik jinoyat (qissa).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyUz1menu)
    await call.message.delete()


@dp.message_handler(text="Tohir Malik")
async def badiiy(message: Message):
    await message.answer_document(open("Books/Badiiy/Tohir Malik Nomus va Qasos.pdf", "rb"), reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Tohir Malik. Murdalar gapirmaydilar.apk", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Tohir Malik-Shaytanat 5-kitob.pdf", "rb"), reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Tohir Malik.(@KITOB) Davron (qissa).pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Tohir Malik.(@KITOB)Eng kichik jinoyat (qissa).pdf", "rb"),
                                  reply_markup=Iks)


@dp.callback_query_handler(text_contains="O'lmas Umarbekov")
async def badiiy(call: CallbackQuery):
    await call.message.answer_document(open("Books/Badiiy/Odam bo'lish qiyin (O'lmas Umarbekov).apk", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyUz1menu)
    await call.message.delete()


@dp.message_handler(text="O'lmas Umarbekov")
async def badiiy(message: Message):
    await message.answer_document(open("Books/Badiiy/Odam bo'lish qiyin (O'lmas Umarbekov).apk", "rb"),
                                  reply_markup=Iks)


# BadiiyJMenu --->
@dp.callback_query_handler(text_contains="Lev Tolstoy")
async def jahon(call: CallbackQuery):
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Lev_Tolstoy_Tanlangan_asarlar_1.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Lev_Tolstoy_Tanlangan_asarlar_2.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Lev_Tolstoy_Tanlangan_asarlar_3.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Lev_Tolstoy_Tanlangan_asarlar_4.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Lev Tolstoy. Urush va tinchlik (1-kitob).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyJmenu)
    await call.message.delete()


@dp.message_handler(text="Lev Tolstoy")
async def jahon(message: Message):
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Lev_Tolstoy_Tanlangan_asarlar_1.pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Lev_Tolstoy_Tanlangan_asarlar_2.pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Lev_Tolstoy_Tanlangan_asarlar_3.pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Lev_Tolstoy_Tanlangan_asarlar_4.pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Lev Tolstoy. Urush va tinchlik (1-kitob).pdf", "rb"), reply_markup=Iks)


@dp.callback_query_handler(text_contains="Aleksandr Pushkin")
async def jahon(call: CallbackQuery):
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Aleksandr Pushkin. Dubrovskiy (qissa).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Aleksandr Pushkin. Kapitan qizi (qissa).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Aleksandr Pushkin. Poema va ertaklar.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Aleksandr Pushkin. Suv parisi.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Aleksandr Pushkin. Yevgeniy Onegin (Oybek tarjimasi).pdf", "rb"),
        reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyJmenu)
    await call.message.delete()


@dp.message_handler(text="Aleksandr Pushkin")
async def jahon(message: Message):
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Aleksandr Pushkin. Dubrovskiy (qissa).pdf", "rb"), reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Aleksandr Pushkin. Kapitan qizi (qissa).pdf", "rb"), reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Aleksandr Pushkin. Poema va ertaklar.pdf", "rb"), reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Aleksandr Pushkin. Suv parisi.pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Aleksandr Pushkin. Yevgeniy Onegin (Oybek tarjimasi).pdf", "rb"),
        reply_markup=Iks)


@dp.callback_query_handler(text_contains="Fyodor Dostoyevskiy")
async def jahon(call: CallbackQuery):
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Kulgili odamning tushi.apk", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Kulgili odamning tushi.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Fedor Dostoevskiy. Telba (roman).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Fedor Dostoyevskiy. Qimorboz (roman).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/''Jinoyat va jazo''.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyJmenu)
    await call.message.delete()


@dp.message_handler(text="Fyodor Dostoyevskiy")
async def jahon(message: Message):
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Kulgili odamning tushi.apk", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Kulgili odamning tushi.pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Fedor Dostoevskiy. Telba (roman).pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Fedor Dostoyevskiy. Qimorboz (roman).pdf", "rb"), reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/''Jinoyat va jazo''.pdf", "rb"),
                                  reply_markup=Iks)


@dp.callback_query_handler(text_contains="Mixail Bulgakov")
async def jahon(call: CallbackQuery):
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Mixail Bulgakov. Usta va Margarita (roman).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyJmenu)
    await call.message.delete()


@dp.message_handler(text="Mixail Bulgakov")
async def jahon(message: Message):
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Mixail Bulgakov. Usta va Margarita (roman).pdf", "rb"), reply_markup=Iks)


@dp.callback_query_handler(text_contains="Chingiz Aytmatov")
async def jahon(call: CallbackQuery):
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Chingiz Aytmatov.ppt", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Chingiz Aytmatov cho'qqida qolgan.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Chingiz Aytmatov. Birinchi muallim (qissa).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Chingiz Aytmatov. Erta qaytgan turnalar.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Chingiz Aytmatov. Bo'tako'z (qissa).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyJmenu)
    await call.message.delete()


@dp.message_handler(text="Chingiz Aytmatov")
async def jahon(message: Message):
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Chingiz Aytmatov.ppt", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Chingiz Aytmatov cho'qqida qolgan.pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Chingiz Aytmatov. Birinchi muallim (qissa).pdf", "rb"), reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Chingiz Aytmatov. Erta qaytgan turnalar.pdf", "rb"), reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Chingiz Aytmatov. Bo'tako'z (qissa).pdf", "rb"), reply_markup=Iks)


@dp.callback_query_handler(text_contains="Nodar Dumbadze")
async def jahon(call: CallbackQuery):
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Hislarimni qozgama.Nodar Dumbadze..pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Kukaracha.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyJmenu)
    await call.message.delete()


@dp.message_handler(text="Nodar Dumbadze")
async def jahon(message: Message):
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Hislarimni qozgama.Nodar Dumbadze..pdf", "rb"), reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Kukaracha.pdf", "rb"), reply_markup=Iks)


@dp.callback_query_handler(text_contains="Jek London")
async def jahon(call: CallbackQuery):
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Hayotga muhabbat (Jek London).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Jek London..doc", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Jek London. Martin Iden (roman).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Jek London. Oq so'yloq (qissa).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Jek London Hayotga muhabbat (hikoya)  Sever.UZ .apk", "rb"),
        reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyJ1Menu)
    await call.message.delete()


@dp.message_handler(text="Jek London")
async def jahon(message: Message):
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Hayotga muhabbat (Jek London).pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Jek London..doc", "rb"), reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Jek London. Martin Iden (roman).pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Jek London. Oq so'yloq (qissa).pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Jek London Hayotga muhabbat (hikoya)  Sever.UZ .apk", "rb"),
        reply_markup=Iks)


@dp.callback_query_handler(text_contains="Gabriel")
async def jahon(call: CallbackQuery):
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Yolg'izlikning yuz yili (Gabriel Garsia).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Gabriel Garsia Markes. Oshkora qotillik qissasi (qissa).pdf", "rb"),
        reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Ulug  onaning jazosi [@Elektron_kutubxona_kitoblarbot].pdf", "rb"),
        reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyJmenu)
    await call.message.delete()


@dp.message_handler(text="Gabriel")
async def jahon(message: Message):
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Yolg'izlikning yuz yili (Gabriel Garsia).pdf", "rb"), reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Gabriel Garsia Markes. Oshkora qotillik qissasi (qissa).pdf", "rb"),
        reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Ulug  onaning jazosi [@Elektron_kutubxona_kitoblarbot].pdf", "rb"),
        reply_markup=Iks)


@dp.callback_query_handler(text_contains="Alber Kamyu")
async def jahon(call: CallbackQuery):
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Alber Kamyu. Begona (qissa).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Alber Kamyu. Kaligula (pyesa).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Alber Kamyu. Vabo (roman).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/56.Alber Kamyu - Begona (qissa).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyJ1Menu)
    await call.message.delete()


@dp.message_handler(text="Alber Kamyu")
async def jahon(message: Message):
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Alber Kamyu. Begona (qissa).pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Alber Kamyu. Kaligula (pyesa).pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Alber Kamyu. Vabo (roman).pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/56.Alber Kamyu - Begona (qissa).pdf", "rb"),
                                  reply_markup=Iks)


@dp.callback_query_handler(text_contains="Kobo Abe")
async def jahon(call: CallbackQuery):
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Qumdagi xotin.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Yashik odam (roman).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyJ1Menu)
    await call.message.delete()


@dp.message_handler(text="Kobo Abe")
async def jahon(message: Message):
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Qumdagi xotin.pdf", "rb"), reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Yashik odam (roman).pdf", "rb"),
                                  reply_markup=Iks)


@dp.callback_query_handler(text_contains="Lao She")
async def jahon(call: CallbackQuery):
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/@Elektron_Kutubxona-Mushuklar shahri.pdf"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyJ1Menu)
    await call.message.delete()


@dp.message_handler(text="Lao She")
async def jahon(message: Message):
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/@Elektron_Kutubxona-Mushuklar shahri.pdf"),
                                  reply_markup=Iks)


@dp.callback_query_handler(text_contains="Artur")
async def jahon(call: CallbackQuery):
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Artur Konan Doyl. Baskervillar iti (qissa).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Artur Konan Doyl. Sherlok Xolms haqida hikoyalar.pdf", "rb"),
        reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Artur Konan Doyl-Sherlok Xolms va doktor Uotsonning sarguzas.pdf", "rb"),
        reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/sh_xolms_hikoya.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyJ1Menu)
    await call.message.delete()


@dp.message_handler(text="Artur")
async def jahon(message: Message):
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Artur Konan Doyl. Baskervillar iti (qissa).pdf", "rb"), reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Artur Konan Doyl. Sherlok Xolms haqida hikoyalar.pdf", "rb"),
        reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Artur Konan Doyl-Sherlok Xolms va doktor Uotsonning sarguzas.pdf", "rb"),
        reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/sh_xolms_hikoya.pdf", "rb"), reply_markup=Iks)


@dp.callback_query_handler(text_contains="Agata Kristi")
async def jahon(call: CallbackQuery):
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Ustasi faranglar (Agata Kristi).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Izquvar Puaro (Agata Kristi).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Agata Kristi (Puaro) @Kutubxona_Elektron.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Agata Kristi - Bulbul oshiyoni.apk", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/O`g`irlangan million dollar (Agata Kristi).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/АГАТА_КРИСТИ_АЛИФБО_БЎЙИЧА_ҚОТИЛЛИК.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Detektiv.apk", "rb"), reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/60.Agata Kristi - O'nta negr bolasi.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Agata Kristi - Tilsimli shahmat.mp3", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyJ1Menu)
    await call.message.delete()


@dp.message_handler(text="Agata Kristi")
async def jahon(message: Message):
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Ustasi faranglar (Agata Kristi).pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Izquvar Puaro (Agata Kristi).pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Agata Kristi (Puaro) @Kutubxona_Elektron.pdf", "rb"), reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Agata Kristi - Bulbul oshiyoni.apk", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/O`g`irlangan million dollar (Agata Kristi).pdf", "rb"), reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/АГАТА_КРИСТИ_АЛИФБО_БЎЙИЧА_ҚОТИЛЛИК.pdf", "rb"), reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Detektiv.apk", "rb"), reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/60.Agata Kristi - O'nta negr bolasi.pdf", "rb"), reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Agata Kristi - Tilsimli shahmat.mp3", "rb"),
                                  reply_markup=Iks)


@dp.callback_query_handler(text_contains="Gi De Mopassan")
async def jahon(call: CallbackQuery):
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Sadoqat qurboni. Gi de Mopassan (hikoya) [@KitobL].txt", "rb"),
        reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Gi de Mopassan. Novellalar.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Gi de Mopassan. Azizim (roman).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Gi de Mopassan.Marjon shodasi (hikoya).epub", "rb"), reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Gi de Mopassan.Murdaning qo'li(hikoya).epub", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Gi de Mopassan. Azizim (roman).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyJ1Menu)
    await call.message.delete()


@dp.message_handler(text="Gi De Mopassan")
async def jahon(message: Message):
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Sadoqat qurboni. Gi de Mopassan (hikoya) [@KitobL].txt", "rb"),
        reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Gi de Mopassan. Novellalar.pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Gi de Mopassan. Azizim (roman).pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Gi de Mopassan.Marjon shodasi (hikoya).epub", "rb"), reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Gi de Mopassan.Murdaning qo'li(hikoya).epub", "rb"), reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Gi de Mopassan. Azizim (roman).pdf", "rb"),
                                  reply_markup=Iks)


@dp.callback_query_handler(text_contains="Onor De Balzak")
async def jahon(call: CallbackQuery):
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/@Kutubxona_Olami-Gobsek.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/@Kutubxona_Elektron-Dahriyning ibodati.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/@Kutubxona_Elektron-Atirgulning tikoni.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/ONORE DE BALZAK- chin sevgi.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Onore de Balzak. Sag'ri teri tilsimi (roman).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyJ1Menu)
    await call.message.delete()


@dp.message_handler(text="Onor De Balzak")
async def jahon(message: Message):
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/@Kutubxona_Olami-Gobsek.pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/@Kutubxona_Elektron-Dahriyning ibodati.pdf", "rb"), reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/@Kutubxona_Elektron-Atirgulning tikoni.pdf", "rb"), reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/ONORE DE BALZAK- chin sevgi.pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Onore de Balzak. Sag'ri teri tilsimi (roman).pdf", "rb"), reply_markup=Iks)


@dp.callback_query_handler(text_contains="Ernest Xeminguey")
async def jahon(call: CallbackQuery):
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Ernest Xeminguey. Dahshatli kutish (hikoya).docx", "rb"), reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Ernest Xeminguey. Maestro bilan muloqot.docx", "rb"), reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Ernest Xeminguey. Yomgirda qolgan mushuk.epub", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Ernest Xeminguey__Alvido qurol.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Ernest Xeminguey. Chol va dengiz (qissa).mhtml", "rb"), reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Ernest Xeminguey. Ko‘prikdagi chol (hikoya).docx", "rb"), reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyJ1Menu)
    await call.message.delete()


@dp.message_handler(text="Ernest Xeminguey")
async def jahon(message: Message):
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Ernest Xeminguey. Dahshatli kutish (hikoya).docx", "rb"), reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Ernest Xeminguey. Maestro bilan muloqot.docx", "rb"), reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Ernest Xeminguey. Yomgirda qolgan mushuk.epub", "rb"), reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Ernest Xeminguey__Alvido qurol.pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Ernest Xeminguey. Chol va dengiz (qissa).mhtml", "rb"), reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Ernest Xeminguey. Ko‘prikdagi chol (hikoya).docx", "rb"), reply_markup=Iks)


@dp.callback_query_handler(text_contains="Jeyms Joys")
async def jahon(call: CallbackQuery):
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Jeyms_Joys_Musavvirning_yoshlikdagi.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Jeyms Joys. Uliss sarguzashtlari (roman).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyJ1Menu)
    await call.message.delete()


@dp.message_handler(text="Jeyms Joys")
async def jahon(message: Message):
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Jeyms_Joys_Musavvirning_yoshlikdagi.pdf", "rb"), reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Jeyms Joys. Uliss sarguzashtlari (roman).pdf", "rb"), reply_markup=Iks)


@dp.callback_query_handler(text_contains="Jonattan Swift")
async def jahon(call: CallbackQuery):
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Jonatan Svift. Gulliverning sayohatlari (roman).pdf", "rb"),
        reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyJ1Menu)
    await call.message.delete()


@dp.message_handler(text="Jonattan Swift")
async def jahon(message: Message):
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Jonatan Svift. Gulliverning sayohatlari (roman).pdf", "rb"),
        reply_markup=Iks)


@dp.callback_query_handler(text_contains="Jyul Vern")
async def jahon(call: CallbackQuery):
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Kapitan Grant bolalari.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Robinzonlar maktabi [@kitoblar1].pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Jyul Vern. Antifer tog'aning sarguzashtlari (roman).pdf", "rb"),
        reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Jyul Vern - Suv ostida 80 ming kilometr.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Jyul Vern - O'n besh yoshli kapitan (roman) .pdf", "rb"), reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyJ1Menu)
    await call.message.delete()


@dp.message_handler(text="Jyul Vern")
async def jahon(message: Message):
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Kapitan Grant bolalari.pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Robinzonlar maktabi [@kitoblar1].pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Jyul Vern. Antifer tog'aning sarguzashtlari (roman).pdf", "rb"),
        reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Jyul Vern - Suv ostida 80 ming kilometr.pdf", "rb"), reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Jyul Vern - O'n besh yoshli kapitan (roman) .pdf", "rb"), reply_markup=Iks)


@dp.callback_query_handler(text_contains="Somerset Moem")
async def jahon(call: CallbackQuery):
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Somerset Moem-Oy va sariq chaqa (roman)[@Zokki_bot].pdf", "rb"),
        reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyJ1Menu)
    await call.message.delete()


@dp.message_handler(text="Somerset Moem")
async def jahon(message: Message):
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Somerset Moem-Oy va sariq chaqa (roman)[@Zokki_bot].pdf", "rb"),
        reply_markup=Iks)


@dp.callback_query_handler(text_contains="Robindranat Tagor")
async def jahon(call: CallbackQuery):
    await call.message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Robindranat Tagor_Halokat_.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Nur va soyalar (Robindranat Tagor).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyJ1Menu)
    await call.message.delete()


@dp.message_handler(text="Robindranat Tagor")
async def jahon(message: Message):
    await message.answer_document(open("Books/Badiiy/Jahon adabiyoti/Robindranat Tagor_Halokat_.pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(
        open("Books/Badiiy/Jahon adabiyoti/Nur va soyalar (Robindranat Tagor).pdf", "rb"), reply_markup=Iks)


@dp.callback_query_handler(text_contains="k1")
async def start(call: CallbackQuery):
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=BadiiyJ1Menu)
    await call.message.delete()


@dp.callback_query_handler(text_contains="o1")
async def start(call: CallbackQuery):
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=BadiiyJmenu)
    await call.message.delete()


@dp.callback_query_handler(text_contains="menu")
async def start(call: CallbackQuery):
    await call.message.answer_photo(open("Image/start1.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=menuStart)
    await call.message.delete()


@dp.callback_query_handler(text_contains='❌')
async def x(call: CallbackQuery):
    await call.message.delete()


@dp.callback_query_handler(text_contains="j1")
async def c(call: CallbackQuery):
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Bolalarmenu)
    await call.message.delete()


@dp.callback_query_handler(text_contains="Ertaklar")
async def c(call: CallbackQuery):
    await call.message.answer_document(
        open("Books/Bolalar Adabiyoti/[@Elektron_kutubxona_kitoblarbot] Oltin beshik.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Bolalar Adabiyoti/[@Elektron_kutubxona_kitoblarbot] Suv qizi.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Bolalar Adabiyoti/[@Elektron_kutubxona_kitoblarbot] Kulsa gul - yig lasa dur.pdf", "rb"),
        reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Bolalar Adabiyoti/[@Elektron_kutubxona_kitoblarbot] O zbek xalq ertaklari.pdf", "rb"),
        reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Bolalarmenu)
    await call.message.delete()


@dp.message_handler(text="Ertaklar")
async def c(message: Message):
    await message.answer_document(
        open("Books/Bolalar Adabiyoti/[@Elektron_kutubxona_kitoblarbot] Oltin beshik.pdf", "rb"), reply_markup=Iks)
    await message.answer_document(
        open("Books/Bolalar Adabiyoti/[@Elektron_kutubxona_kitoblarbot] Suv qizi.pdf", "rb"), reply_markup=Iks)
    await message.answer_document(
        open("Books/Bolalar Adabiyoti/[@Elektron_kutubxona_kitoblarbot] Kulsa gul - yig lasa dur.pdf", "rb"),
        reply_markup=Iks)
    await message.answer_document(
        open("Books/Bolalar Adabiyoti/[@Elektron_kutubxona_kitoblarbot] O zbek xalq ertaklari.pdf", "rb"),
        reply_markup=Iks)


@dp.callback_query_handler(text_contains="Ensiklopedia")
async def c(call: CallbackQuery):
    await call.message.answer_document(
        open("Books/Bolalar Adabiyoti/[@Elektron_kutubxona_kitoblarbot] Astronomiya va koinot.pdf", "rb"),
        reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Bolalar Adabiyoti/[@Elektron_kutubxona_kitoblarbot] Aviatsiya.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Bolalar Adabiyoti/[@Elektron_kutubxona_kitoblarbot] Dinozavrlar.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Bolalar Adabiyoti/[@Elektron_kutubxona_kitoblarbot] Geografik kashfiyotlar.pdf", "rb"),
        reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Bolalar Adabiyoti/[@Elektron_kutubxona_kitoblarbot] Kashfiyot va ertaklar.pdf", "rb"),
        reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Bolalarmenu)
    await call.message.delete()


@dp.message_handler(text="Ensiklopedia")
async def c(message: Message):
    await message.answer_document(
        open("Books/Bolalar Adabiyoti/[@Elektron_kutubxona_kitoblarbot] Astronomiya va koinot.pdf", "rb"),
        reply_markup=Iks)
    await message.answer_document(
        open("Books/Bolalar Adabiyoti/[@Elektron_kutubxona_kitoblarbot] Aviatsiya.pdf", "rb"), reply_markup=Iks)
    await message.answer_document(
        open("Books/Bolalar Adabiyoti/[@Elektron_kutubxona_kitoblarbot] Dinozavrlar.pdf", "rb"), reply_markup=Iks)
    await message.answer_document(
        open("Books/Bolalar Adabiyoti/[@Elektron_kutubxona_kitoblarbot] Geografik kashfiyotlar.pdf", "rb"),
        reply_markup=Iks)
    await message.answer_document(
        open("Books/Bolalar Adabiyoti/[@Elektron_kutubxona_kitoblarbot] Kashfiyot va ertaklar.pdf", "rb"),
        reply_markup=Iks)


@dp.callback_query_handler(text_contains="Boburnoma")
async def mumtoz(call: CallbackQuery):
    await call.message.answer_document(open("Books/Mumtoz/Boburnoma.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(
        open("Books/Mumtoz/Boburnoma uchun qisqacha izohli lug'at (F.Ishoqov, 2008).pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Mumtoz/Zahiriddin Muhammad Bobur. Boburnoma.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Mumtozmenu)
    await call.message.delete()


@dp.message_handler(text="Boburnoma")
async def mumtoz(message: Message):
    await message.answer_document(open("Books/Mumtoz/Boburnoma.pdf", "rb"), reply_markup=Iks)
    await message.answer_document(
        open("Books/Mumtoz/Boburnoma uchun qisqacha izohli lug'at (F.Ishoqov, 2008).pdf", "rb"), reply_markup=Iks)
    await message.answer_document(open("Books/Mumtoz/Zahiriddin Muhammad Bobur. Boburnoma.pdf", "rb"),
                                  reply_markup=Iks)


@dp.callback_query_handler(text_contains="Shohnoma")
async def mumtoz(call: CallbackQuery):
    await call.message.answer_document(open("Books/Mumtoz/Abulqosim Firdavsiy. Shohnoma.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Mumtozmenu)
    await call.message.delete()


@dp.message_handler(text="Shohnoma")
async def mumtoz(message: Message):
    await message.answer_document(open("Books/Mumtoz/Abulqosim Firdavsiy. Shohnoma.pdf", "rb"), reply_markup=Iks)


@dp.callback_query_handler(text_contains="Zarbulmasal")
async def mumtoz(call: CallbackQuery):
    await call.message.answer_document(open("Books/Mumtoz/Gulxaniy. Zarbulmasal.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Mumtozmenu)
    await call.message.delete()


@dp.message_handler(text="Zarbulmasal")
async def mumtoz(message: Message):
    await message.answer_document(open("Books/Mumtoz/Gulxaniy. Zarbulmasal.pdf", "rb"), reply_markup=Iks)


@dp.callback_query_handler(text_contains="Ulus")
async def mumtoz(call: CallbackQuery):
    await call.message.answer_document(open("Books/Mumtoz/mirzo_ulugbek_4_ulus_tarixi_ziyouz_com.zip", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Mumtoz/To'rt ulus tarixi - Mirzo Ulug'bek.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Mumtoz/Mirzo Ulug'bek. To'rt ulus tarixi.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Mumtozmenu)
    await call.message.delete()


@dp.message_handler(text="Ulus")
async def mumtoz(message: Message):
    await message.answer_document(open("Books/Mumtoz/mirzo_ulugbek_4_ulus_tarixi_ziyouz_com.zip", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(open("Books/Mumtoz/To'rt ulus tarixi - Mirzo Ulug'bek.pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(open("Books/Mumtoz/Mirzo Ulug'bek. To'rt ulus tarixi.pdf", "rb"),
                                  reply_markup=Iks)


@dp.callback_query_handler(text_contains="Devon")
async def mumtoz(call: CallbackQuery):
    await call.message.answer_document(open("Books/Mumtoz/Devoni lug'otut turk. 1-jild (Mahmud Koshg'ariy).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Mumtoz/Devoni lug'otut turk. 2-jild (Mahmud Koshg'ariy).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Mumtoz/Devoni lug'otut turk. 3-jild (Mahmud Koshg'ariy).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Mumtozmenu)
    await call.message.delete()


@dp.message_handler(text="Devon")
async def mumtoz(message: Message):
    await message.answer_document(open("Books/Mumtoz/Devoni lug'otut turk. 1-jild (Mahmud Koshg'ariy).pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(open("Books/Mumtoz/Devoni lug'otut turk. 2-jild (Mahmud Koshg'ariy).pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(open("Books/Mumtoz/Devoni lug'otut turk. 3-jild (Mahmud Koshg'ariy).pdf", "rb"),
                                  reply_markup=Iks)


@dp.callback_query_handler(text_contains="Qutadg'u")
async def mumtoz(call: CallbackQuery):
    await call.message.answer_document(open("Books/Mumtoz/Yusuf Xos Hojib. Qutadg'u bilig.pdf", "rb"), reply_markup=Iks)
    await call.message.answer_document(open("Books/Mumtoz/Yusuf Xos Hojib. Qutadg'u bilig (nasriy bayoni).pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_document(open("Books/Mumtoz/4.Yusuf Xos Hojib - Qutadg'u bilig.pdf", "rb"),
                                       reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Mumtozmenu)
    await call.message.delete()


@dp.message_handler(text="Qutadg'u")
async def mumtoz(message: Message):
    await message.answer_document(open("Books/Mumtoz/Yusuf Xos Hojib. Qutadg'u bilig.pdf", "rb"), reply_markup=Iks)
    await message.answer_document(open("Books/Mumtoz/Yusuf Xos Hojib. Qutadg'u bilig (nasriy bayoni).pdf", "rb"),
                                  reply_markup=Iks)
    await message.answer_document(open("Books/Mumtoz/4.Yusuf Xos Hojib - Qutadg'u bilig.pdf", "rb"),
                                  reply_markup=Iks)


@dp.callback_query_handler(text_contains="audiouz")
async def audio(call: CallbackQuery):
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"),
                                    f"Sizga Qaysi JAnrdagi audio kitoblar kerak? Tanlang 👇!", reply_markup=Audiouzmenu)
    await call.message.delete()


@dp.callback_query_handler(text_contains="Romanlaruz")
async def audio(call: CallbackQuery):
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Taanlang! 👇", reply_markup=Romanuzmenu)
    await call.message.delete()


@dp.callback_query_handler(text_contains="Qissalaruz")
async def audio(call: CallbackQuery):
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Taanlang! 👇", reply_markup=Qissalaruz)
    await call.message.delete()


@dp.callback_query_handler(text_contains="Hikoyalaruz")
async def audio(call: CallbackQuery):
    await call.message.answer_audio(
        open("Books/AudioKitob/O'tkir Hoshimov - Urushning so'nggi qurboni (hikoya).mp3", "rb"), reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Abdulla Qahhor - Anor (hikoya).mp3", "rb"), reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Yoz yomg‘iri.mp3", "rb"), reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Abdulla Qahhor - Ming bir jon (hikoya).mp3", "rb"),
                                    reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Abdulla Qahhor - O'g'ri (hikoya).mp3", "rb"),
                                    reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Shamolni tutib bo'lmaydi.mp3", "rb"), reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Nazar Eshonqul - Maymun yetaklagan odam (hikoya).mp3", "rb"),
                                    reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Erkin A'zam - Anoyining jaydari olmasi.mp3", "rb"),
                                    reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Murod Muhammad Do'st - Dashtu dalalarda.mp3", "rb"),
                                    reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"),
                                    f"Sizga Qaysi JAnrdagi audio kitoblar kerak? Tanlang 👇!",
                                    reply_markup=Audiouzmenu)
    await call.message.delete()


@dp.message_handler(text="Hikoyalaruz")
async def audio(message: Message):
    await message.answer_audio(
        open("Books/AudioKitob/O'tkir Hoshimov - Urushning so'nggi qurboni (hikoya).mp3", "rb"), reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Abdulla Qahhor - Anor (hikoya).mp3", "rb"), reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Yoz yomg‘iri.mp3", "rb"), reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Abdulla Qahhor - Ming bir jon (hikoya).mp3", "rb"),
                               reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Abdulla Qahhor - O'g'ri (hikoya).mp3", "rb"),
                               reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Shamolni tutib bo'lmaydi.mp3", "rb"), reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Nazar Eshonqul - Maymun yetaklagan odam (hikoya).mp3", "rb"),
                               reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Erkin A'zam - Anoyining jaydari olmasi.mp3", "rb"),
                               reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Murod Muhammad Do'st - Dashtu dalalarda.mp3", "rb"),
                               reply_markup=Iks)


@dp.callback_query_handler(text_contains="O'tgan kunlarau")
async def audio(call: CallbackQuery):
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/001 - O'TKAN KUNLAR.mp3", "rb"), reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/002 - O'TKAN KUNLAR.mp3", "rb"), reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/03. Oʻtkan kunlar @audiokitob_ulashamiz.mp3", "rb"),
                                    reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/04. Oʻtkan kunlar @audiokitob_ulashamiz.mp3", "rb"),
                                    reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/05. Oʻtkan kunlar @audiokitob_ulashamiz.mp3", "rb"),
                                    reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Taanlang! 👇", reply_markup=Romanuzmenu)
    await call.message.delete()


@dp.message_handler(text="O'tgan kunlar")
async def audio(message: Message):
    await message.answer_audio(open("Books/AudioKitob/Romanuz/001 - O'TKAN KUNLAR.mp3", "rb"), reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Romanuz/002 - O'TKAN KUNLAR.mp3", "rb"), reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Romanuz/03. Oʻtkan kunlar @audiokitob_ulashamiz.mp3", "rb"),
                               reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Romanuz/04. Oʻtkan kunlar @audiokitob_ulashamiz.mp3", "rb"),
                               reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Romanuz/05. Oʻtkan kunlar @audiokitob_ulashamiz.mp3", "rb"),
                               reply_markup=Iks)


@dp.callback_query_handler(text_contains="Mehrobdan Chayonau")
async def audio(call: CallbackQuery):
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/01. Mehrobdan chayon.mp3", "rb"), reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/02. Mehrobdan chayon.mp3", "rb"), reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/03. Mehrobdan chayon.mp3", "rb"), reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/04. Mehrobdan chayon.mp3", "rb"), reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/05. Mehrobdan chayon.mp3", "rb"), reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Taanlang! 👇", reply_markup=Romanuzmenu)
    await call.message.delete()


@dp.message_handler(text="Mehrobdan Chayon")
async def audio(message: Message):
    await message.answer_audio(open("Books/AudioKitob/Romanuz/01. Mehrobdan chayon.mp3", "rb"), reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Romanuz/02. Mehrobdan chayon.mp3", "rb"), reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Romanuz/03. Mehrobdan chayon.mp3", "rb"), reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Romanuz/04. Mehrobdan chayon.mp3", "rb"), reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Romanuz/05. Mehrobdan chayon.mp3", "rb"), reply_markup=Iks)


@dp.callback_query_handler(text_contains="Navoiyau")
async def audio(call: CallbackQuery):
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/01. Navoiy @audiokitob_ulashamiz.mp3", "rb"),
                                    reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/02. Navoiy @audiokitob_ulashamiz.mp3", "rb"),
                                    reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/03. Navoiy @audiokitob_ulashamiz.mp3", "rb"),
                                    reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/04. Navoiy @audiokitob_ulashamiz.mp3", "rb"),
                                    reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/05. Navoiy @audiokitob_ulashamiz.mp3", "rb"),
                                    reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Taanlang! 👇", reply_markup=Romanuzmenu)
    await call.message.delete()


@dp.message_handler(text="Navoiy")
async def audio(message: Message):
    await message.answer_audio(open("Books/AudioKitob/Romanuz/01. Navoiy @audiokitob_ulashamiz.mp3", "rb"),
                               reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Romanuz/02. Navoiy @audiokitob_ulashamiz.mp3", "rb"),
                               reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Romanuz/03. Navoiy @audiokitob_ulashamiz.mp3", "rb"),
                               reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Romanuz/04. Navoiy @audiokitob_ulashamiz.mp3", "rb"),
                               reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Romanuz/05. Navoiy @audiokitob_ulashamiz.mp3", "rb"),
                               reply_markup=Iks)


@dp.callback_query_handler(text_contains="Yulduzli tunlar")
async def audio(call: CallbackQuery):
    await call.message.answer_audio(
        open("Books/AudioKitob/Romanuz/01. Yulduzli tunlar @audiokitob_ulashamiz.mp3", "rb"), reply_markup=Iks)
    await call.message.answer_audio(
        open("Books/AudioKitob/Romanuz/02. Yulduzli tunlar @audiokitob_ulashamiz.mp3", "rb"), reply_markup=Iks)
    await call.message.answer_audio(
        open("Books/AudioKitob/Romanuz/03. Yulduzli tunlar @audiokitob_ulashamiz.mp3", "rb"), reply_markup=Iks)
    await call.message.answer_audio(
        open("Books/AudioKitob/Romanuz/04. Yulduzli tunlar @audiokitob_ulashamiz.mp3", "rb"), reply_markup=Iks)
    await call.message.answer_audio(
        open("Books/AudioKitob/Romanuz/05. Yulduzli tunlar @audiokitob_ulashamiz.mp3", "rb"), reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Taanlang! 👇", reply_markup=Romanuzmenu)
    await call.message.delete()


@dp.message_handler(text="Yulduzli tunlar")
async def audio(message: Message):
    await message.answer_audio(
        open("Books/AudioKitob/Romanuz/01. Yulduzli tunlar @audiokitob_ulashamiz.mp3", "rb"), reply_markup=Iks)
    await message.answer_audio(
        open("Books/AudioKitob/Romanuz/02. Yulduzli tunlar @audiokitob_ulashamiz.mp3", "rb"), reply_markup=Iks)
    await message.answer_audio(
        open("Books/AudioKitob/Romanuz/03. Yulduzli tunlar @audiokitob_ulashamiz.mp3", "rb"), reply_markup=Iks)
    await message.answer_audio(
        open("Books/AudioKitob/Romanuz/04. Yulduzli tunlar @audiokitob_ulashamiz.mp3", "rb"), reply_markup=Iks)
    await message.answer_audio(
        open("Books/AudioKitob/Romanuz/05. Yulduzli tunlar @audiokitob_ulashamiz.mp3", "rb"), reply_markup=Iks)


@dp.callback_query_handler(text_contains="Ufqau")
async def audio(call: CallbackQuery):
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/01. Ufq (trilogiya).mp3", "rb"), reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/02. Ufq (trilogiya).mp3", "rb"), reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/03. Ufq (trilogiya).mp3", "rb"), reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/04. Ufq (trilogiya).mp3", "rb"), reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/05. Ufq (trilogiya).mp3", "rb"), reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Taanlang! 👇", reply_markup=Romanuzmenu)
    await call.message.delete()


@dp.message_handler(text="Ufqau")
async def audio(message: Message):
    await message.answer_audio(open("Books/AudioKitob/Romanuz/01. Ufq (trilogiya).mp3", "rb"), reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Romanuz/02. Ufq (trilogiya).mp3", "rb"), reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Romanuz/03. Ufq (trilogiya).mp3", "rb"), reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Romanuz/04. Ufq (trilogiya).mp3", "rb"), reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Romanuz/05. Ufq (trilogiya).mp3", "rb"), reply_markup=Iks)


@dp.callback_query_handler(text_contains="Shaytanat")
async def audio(call: CallbackQuery):
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/01. Shaytanat @audibleuzb.mp3", "rb"),
                                    reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/02. Shaytanat @audibleuzb.mp3", "rb"),
                                    reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/03. Shaytanat @audibleuzb.mp3", "rb"),
                                    reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/04. Shaytanat @audibleuzb.mp3", "rb"),
                                    reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/05. Shaytanat @audibleuzb.mp3", "rb"),
                                    reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Taanlang! 👇", reply_markup=Romanuzmenu)
    await call.message.delete()


@dp.message_handler(text="Shaytanat")
async def audio(message: Message):
    await message.answer_audio(open("Books/AudioKitob/Romanuz/01. Shaytanat @audibleuzb.mp3", "rb"),
                               reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Romanuz/02. Shaytanat @audibleuzb.mp3", "rb"),
                               reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Romanuz/03. Shaytanat @audibleuzb.mp3", "rb"),
                               reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Romanuz/04. Shaytanat @audibleuzb.mp3", "rb"),
                               reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Romanuz/05. Shaytanat @audibleuzb.mp3", "rb"),
                               reply_markup=Iks)


@dp.callback_query_handler(text_contains="Kechakunduz")
async def audio(call: CallbackQuery):
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/01. Kecha va kunduz.mp3", "rb"), reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/02. Kecha va kunduz.mp3", "rb"), reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/03. Kecha va kunduz.mp3", "rb"), reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/04. Kecha va kunduz.mp3", "rb"), reply_markup=Iks)
    await call.message.answer_audio(open("Books/AudioKitob/Romanuz/05. Kecha va kunduz.mp3", "rb"), reply_markup=Iks)
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Taanlang! 👇", reply_markup=Romanuzmenu)
    await call.message.delete()


@dp.message_handler(text="Kechakunduz")
async def audio(message: Message):
    await message.answer_audio(open("Books/AudioKitob/Romanuz/01. Kecha va kunduz.mp3", "rb"), reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Romanuz/02. Kecha va kunduz.mp3", "rb"), reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Romanuz/03. Kecha va kunduz.mp3", "rb"), reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Romanuz/04. Kecha va kunduz.mp3", "rb"), reply_markup=Iks)
    await message.answer_audio(open("Books/AudioKitob/Romanuz/05. Kecha va kunduz.mp3", "rb"), reply_markup=Iks)


# Back --->
@dp.callback_query_handler(text_contains="b1")
async def start(call: CallbackQuery):
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=BadiiyMenu)
    await call.message.delete()


@dp.callback_query_handler(text_contains="b2")
async def start(call: CallbackQuery):
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=BadiiyMenu)
    await call.message.delete()


@dp.callback_query_handler(text_contains="b3")
async def start(call: CallbackQuery):
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=BadiiyMenu)
    await call.message.delete()


@dp.callback_query_handler(text_contains="b4")
async def start(call: CallbackQuery):
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Diniymenu)
    await call.message.delete()


@dp.callback_query_handler(text_contains="b5")
async def start(call: CallbackQuery):
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Audiouzmenu)
    await call.message.delete()


@dp.callback_query_handler(text_contains="b6")
async def start(call: CallbackQuery):
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Audiouzmenu)
    await call.message.delete()


@dp.callback_query_handler(text_contains="b7")
async def start(call: CallbackQuery):
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                                    reply_markup=Audiouzmenu)
    await call.message.delete()


@dp.message_handler(
    text=["⭐️⭐️⭐️⭐️⭐️ | A'lo", "⭐️⭐️⭐️⭐️ | Yaxshi", "⭐️⭐️⭐️ | O'rtacha", "⭐️⭐️ | Qoniqarli", "⭐️ | Qoniqarsiz"])
async def baho(msg: Message):
    await msg.answer("Qabul qilindi! Baholaganingiz uchun raxmat.")
    await msg.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), f"Kitob turini tanlang",
                           reply_markup=menuStart)


# Left Right
@dp.callback_query_handler(text_contains='r1')
async def badiiy(call: CallbackQuery):
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyUz1menu)
    await call.message.delete()


@dp.callback_query_handler(text_contains='l2')
async def badiiy(call: CallbackQuery):
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyUzmenu)
    await call.message.delete()


@dp.callback_query_handler(text_contains='r2')
async def badiiy(call: CallbackQuery):
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=BadiiyJmenu)
    await call.message.delete()


@dp.callback_query_handler(text_contains='l1')
async def badiiy(call: CallbackQuery):
    await call.message.answer_photo(open("Image/BadiiyMenu.jpg", "rb"), "Kitob turini tanlang",
                                    reply_markup=Biznesmenu)
    await call.message.delete()


if __name__ == '__main__':
    executor.start_polling(dp)
