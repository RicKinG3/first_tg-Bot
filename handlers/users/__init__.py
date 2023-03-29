from .start import dp
from .help import dp

from .menu import dp
from .autor_inline_menu import dp

from .buttons import dp
from .buttons_evaluation_books import dp

from .register import dp
from .errors import dp  # обязательно в конце так как они выполняются по порядку

__all__ = ['dp']  # Список параметров которые можно импортировать
