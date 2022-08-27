from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

#------главное меню-------
make_note = KeyboardButton('Записать')
create_scedule = KeyboardButton('Составить рассписание')
showStr = KeyboardButton('/Показать_записи')
btndel = KeyboardButton('/Удалить_записи')

diaryMenu = ReplyKeyboardMarkup(resize_keyboard=True)
diaryMenu.add(newStr).add( showStr).add(btndel)

#----------------меню да или нет ---------------
yes1 =  KeyboardButton('Да')
no1 =  KeyboardButton('Нет')

yesno = ReplyKeyboardMarkup(resize_keyboard=True)
yesno.add(yes1,no1)

#------------меню показа записей---------------
show24 = KeyboardButton('Показать записи за последние 24 часа')
show31= KeyboardButton('Показать записи за последний месяц')
show7= KeyboardButton('Показать записи за последнюю неделю')
showall= KeyboardButton('Показать все записи')

showKeyboad = ReplyKeyboardMarkup(resize_keyboard=True)
showKeyboad.add(show24).add(show7).add(show31).add(showall).add(btnmain)
