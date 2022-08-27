from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from bbot import BotDB1, dp
from config import *
import markups as nav
from admin import FSMAdmin, DELete, ShowNotes


#------------Идентификация Пользователя----------------
@dp.message_handler(commands = ("start"))
async def check(message: types.Message):
    print(type(str(message.from_user.id)))
    result = BotDB1.check_user(message.from_user.id)
    if result:
        await message.bot.send_message(message.from_user.id, f'Добрый день, {message.from_user.first_name}. Приятно снова тебя увидеть!', reply_markup=nav.diaryMenu)
    else:
        await message.bot.send_message(message.from_user.id, f'Добрый день, {message.from_user.first_name} . Мы еще не знакомы!')
        import time
        time.sleep(2)
        await message.bot.send_message(message.from_user.id, 'Я - бот помощник, буду рад помочь!', reply_markup=nav.diaryMenu)
        BotDB1.add_user(message.from_user.id)


# #------------Блок записи----------------
# @dp.message_handler(commands=('Новая_запись'), commands_prefix = "/!",  state=None)
# async def readyNote(message: types.Message):
#     await FSMAdmin.firstMsg.set()
#     await message.bot.send_message(message.from_user.id, 'Записываю:')
#
#
# @dp.message_handler(content_types=['text'],state=FSMAdmin.firstMsg)
# async def newNote(message: types.Message, state = FSMContext):
#
#     async with state.proxy() as data:
#         data['text'] = message.text
#         BotDB1.add_note(message.from_user.id, data['text'])
#     print(f'Запись добавленна пользователем - {message.from_user.first_name}, его id - {message.from_user.id}')
#     await message.bot.send_message(message.from_user.id, 'Запись добавлена' , reply_markup=nav.diaryMenu)
#
#     await state.finish()
#
#
#
# #------------Блок удаления----------------
# @dp.message_handler(commands=('Удалить_записи'), commands_prefix = "/!",  state=None)
# async def readyDelNote(message: types.Message):
#     await DELete.firstDelMsg.set()
#     await message.bot.send_message(message.from_user.id, 'Отменить это действие не получится')
#     await message.bot.send_message(message.from_user.id, 'Вы уверенны, что хотите удалить все записи ?', reply_markup= nav.yesno)
#
#
# @dp.message_handler(content_types=['text'],state=DELete.firstDelMsg)
# async def newNote(message: types.Message, state = FSMContext):
#     if message.text == 'Да':
#         print(f'Запись пользователя - {message.from_user.first_name}, его id - {message.from_user.id}, удалены')
#         await message.bot.send_message(message.from_user.id, 'Записи успешно удалены' , reply_markup=nav.diaryMenu)
#         BotDB1.del_notes(message.from_user.id)
#         await state.finish()
#
#     elif message.text == 'Нет':
#         await message.bot.send_message(message.from_user.id, 'Хорошо' , reply_markup=nav.diaryMenu)
#         await state.finish()
#
#
# #------------Блок показа записей----------------
# @dp.message_handler(commands=('Показать_записи'), commands_prefix = "/!",  state=None)
# async def readyDelNote(message: types.Message):
#     await ShowNotes.firstShowMsg.set()
#     if  BotDB1.check_notes(message.from_user.id):
#         await message.bot.send_message(message.from_user.id, 'За какое время показать записи?', reply_markup= nav.showKeyboad)
#     else:
#         await message.bot.send_message(message.from_user.id,'Записи не обнаружены' , reply_markup=nav.diaryMenu )
#
# @dp.message_handler(content_types=['text'],state=ShowNotes.firstShowMsg)
# async def newNote(message: types.Message, state = FSMContext):
#     if message.text == 'Показать записи за последние 24 часа':
#         result = BotDB1.show_notes(message.from_user.id, 24)
#         await message.bot.send_message(message.from_user.id, 'Записи за последние 24 часа:' )
#         await message.bot.send_message(message.from_user.id, '+----------------+' )
#         for i in result:
#             l = str(i)
#             await message.bot.send_message(message.from_user.id, l[2:-3:])
#         await message.bot.send_message(message.from_user.id,'+----------------+' , reply_markup=nav.diaryMenu )
#
#     elif message.text == 'Показать записи за последний месяц':
#         result = BotDB1.show_notes(message.from_user.id, 31)
#         await message.bot.send_message(message.from_user.id, 'Записи за последний месяц:' )
#         await message.bot.send_message(message.from_user.id, '+----------------+' )
#         for i in result:
#             l = str(i)
#             await message.bot.send_message(message.from_user.id, l[2:-3:]  )
#         await message.bot.send_message(message.from_user.id,'+----------------+' , reply_markup=nav.diaryMenu )
#
#
#     elif message.text =='Показать записи за последнюю неделю':
#         result = BotDB1.show_notes(message.from_user.id, 7)
#         await message.bot.send_message(message.from_user.id, 'Записи за последнюю неделю:' )
#         await message.bot.send_message(message.from_user.id, '+----------------+' )
#         for i in result:
#             l = str(i)
#             await message.bot.send_message(message.from_user.id, l[2:-3:] )
#         await message.bot.send_message(message.from_user.id,'+----------------+' , reply_markup=nav.diaryMenu )
#
#
#     elif message.text =='Показать все записи':
#         result = BotDB1.show_notes(message.from_user.id, 0)
#         await message.bot.send_message(message.from_user.id, 'Все записи:' )
#         await message.bot.send_message(message.from_user.id, '+----------------+' )
#         for i in result:
#             l = str(i)
#             await message.bot.send_message(message.from_user.id, l[2:-3:] )
#         await message.bot.send_message(message.from_user.id,'+----------------+' , reply_markup=nav.diaryMenu )
#
#
#     elif message.text =='Назад':
#         await message.bot.send_message(message.from_user.id,'Возвращаюсь' , reply_markup=nav.diaryMenu )
        
        
#------------Блок отработки других сообщений----------------

@dp.message_handler()
async def ordinary(message: types.Message):
    if message.text == 'привет':
        await message.bot.send_message(message.from_user.id, 'привет', reply_markup= nav.diaryMenu)
    else:
        await message.bot.send_message(message.from_user.id, 'не знаю, что и сказать', reply_markup= nav.diaryMenu)





