from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMAdmin(StatesGroup):
    firstMsg = State()
    note = State()

class DELete(StatesGroup):
    firstDelMsg =  State()
    delition = State()

class ShowNotes(StatesGroup):
    firstShowMsg = State()
    showing = State()
    

