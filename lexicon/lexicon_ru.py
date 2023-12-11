from typing import Callable

LEXICON_KEYBOARDS: dict[str, str | dict] = {
    'main_keyboard': {
        'continue': "Продолжить чтение 📖",
        'my_books': "Мои книги 📕",
        'my_books_marks': "Мои закладки 🔖",
        'help_bot': "Помощь по боту 🆘"
    },
    'forward': "➡️",
    'backward': "⬅️",
    'edit': "❌Редактировать",
    'cancel': "Отмена"
}

LEXICON_RU: dict[str, str | Callable] = {
    'start': lambda name: f"<b>Привет, {name}!</b>\nЭто бот, в котором ты можешь прочитать книги!",
    LEXICON_KEYBOARDS['main_keyboard']['help_bot']: "<b>Здравствуйте!</b>\nЭтот бот может помочь вам почитать книгу прямо в телеграмме.\nВы можете в любой момент отправить в чат к боту текстовый файл где содержимое это и есть книга\nИ бот возьмет название книги из названия файла и потом разделит весь текстовый файл по страницам (в одной странице будет по 1150 символов)\n<b>ПРИМЕЧАНИЕ</b>\nМаксимальный размер текстового файла - 18Мб\nФормат файла должен быть такой: НАЗВАНИЕ КНИГИ.txt",
    'empty_' + LEXICON_KEYBOARDS['main_keyboard']['my_books']: "У вас нет ни одной книги :(\nЧтобы добавить книгу, отправьте текстовый файл в этот чат.",
    'exists_' + LEXICON_KEYBOARDS['main_keyboard']['my_books']: "<b>Вот ваши книги</b>",
    'empty_' + LEXICON_KEYBOARDS['main_keyboard']['my_books_marks']: "У вас нет ни одной закладки :(\nЧтобы добавить закладку, во время чтения книги нажмите на среднюю инлайн-кнопку и у вас сохранится закладка.",
    'exists_' + LEXICON_KEYBOARDS['main_keyboard']['my_books_marks']: "<b>Вот ваши закладки</b>",
    'enjoy_reading': "Приятного чтения😊",
    'if_book_not_read': "Произошла ошибка. Мы вернули вас к списку ваших книг.",
    'exists_book_mark': "Такая закладка для этой книги уже существует.",
    'good_add_book_mark': "Закладка для этой книги успешно добавлена!",
    'delete': "Удалить",
    'user_delete_book_and_book_not_exists': "Такой книги уже не существует. Попробуйте обновить список книг.",
    'good_book_deleted': "Книга успешно удалена!",
    'user_delete_book_mark_and_book_mark_not_exists': "Такой закладки уже не существует. Попробуйте обновить список закладок для книг.",
    'good_book_mark_deleted': "Закладка для этой книги успешно удалена!",
    'no_continue_read_book': "Вы еще не читали ни одной книги или же у вас нету книг.",
    'user_add_book_and_book_exists': "Такая книга уже существует.",
    'book_add': "Книга успешно добавлена.",
    'document_not_txt': "Бот поддерживает только файлы .txt формата!",
    'big_size_file': "Размер файла не должен превышать 18 мб!"
}

__all__ = (
    'LEXICON_KEYBOARDS',
    'LEXICON_RU'
)
