from typing import Callable

LEXICON_KEYBOARDS: dict[str, str | dict] = {
    'main_keyboard': {
        'continue': "继续阅读 📖",
        'my_books': "我的书籍 📕",
        'my_books_marks': "我的书签 🔖",
        'help_bot': "帮助 🆘"
    },
    'forward': "➡️",
    'backward': "⬅️",
    'edit': "❌编辑",
    'cancel': "取消"
}

LEXICON_RU: dict[str, str | Callable] = {
    'start': lambda name: f"<b>你好, {name}!</b>\n这是一个阅读机器人，可以阅读书籍！",
    LEXICON_KEYBOARDS['main_keyboard']['help_bot']: "<b>你好！</b>\n这个机器人可以帮助您在 Telegram 上直接阅读书籍。\n您随时可以将包含内容的文本文件发送到与机器人的聊天中，这就是一本书。\n该机器人将从文件名中提取书名，然后按页面将整个文本文件分割（每页包含1150个字符）\n<b>注意</b>\n书籍的最大尺寸为18MB\n文件格式应为：书名.txt",
    'empty_' + LEXICON_KEYBOARDS['main_keyboard']['my_books']: "你还没有任何书籍 :(\n要上传一本书，只需在此聊天中发送一个文本文件。",
    'exists_' + LEXICON_KEYBOARDS['main_keyboard']['my_books']: "<b>这是您的书籍</b>",
    'empty_' + LEXICON_KEYBOARDS['main_keyboard']['my_books_marks']: "您还没有任何书签 :(\n要添加书签，只需在阅读时点击屏幕中央的内联按钮即可，这样就能轻松保存书签。",
    'exists_' + LEXICON_KEYBOARDS['main_keyboard']['my_books_marks']: "<b>这是您的书签</b>",
    'enjoy_reading': "祝您阅读愉快😊",
    'if_book_not_read': "出现了错误，返回到书籍列表。",
    'exists_book_mark': "这本书已经有一个书签了。",
    'good_add_book_mark': "为这本书成功添加了书签！",
    'delete': "删除",
    'user_delete_book_and_book_not_exists': "没有这本书了，请尝试更新书单。",
    'good_book_deleted': "图书已成功删除！",
    'user_delete_book_mark_and_book_mark_not_exists': "书签不存在，请尝试更新书签列表。",
    'good_book_mark_deleted': "该书签已成功删除！",
    'no_continue_read_book': "您还没有阅读过任何一本书，或者您没有书籍。",
    'user_add_book_and_book_exists': "这本书已经存在了。",
    'book_add': "图书已成功添加。",
    'document_not_txt': "机器人只支持 .txt 格式的文件！",
    'big_size_file': "文件大小不能超过 18 MB！"
}

__all__ = (
    'LEXICON_KEYBOARDS',
    'LEXICON_RU'
)
