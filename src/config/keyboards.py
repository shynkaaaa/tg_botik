from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_inline_keyboard():
    stations = [
        ("Райымбек батыра", 0),
        ("Жибек жолы", 1),
        ("Алмалы", 2),
        ("Абая", 3),
        ("Байконыр", 4),
        ("Театр имени М. Ауэзова", 5),
        ("Алатау", 6),
        ("Сайран", 7),
        ("Москва", 8),
        ("Сарыарка", 9),
        ("Б. Момышулы", 10),
        ("Общее расписание🕰️", 11)
    ]
    buttons = []
    
    for station, id_ in stations:
        if station == "Общее расписание🕰️":
            buttons.append([InlineKeyboardButton(text=station, callback_data="general_schedule")])
        else:
            buttons.append([InlineKeyboardButton(text=station, callback_data=f"station_{id_}")])

    return InlineKeyboardMarkup(inline_keyboard=buttons)