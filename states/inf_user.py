
from aiogram.dispatcher.filters.state import StatesGroup, State


class Register(StatesGroup):
    # создаем два объекта для хранения состояний
    m_name = State()
    m_yaer = State()
