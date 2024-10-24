import aiogram
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio
import json
bot = Bot(token = '7713317853:AAHFrC1bKFKalrwFRwI_kSdLNomLpyZwofo')
dp = Dispatcher()
router = Router()


@router.message(Command('start'))
async def send_welcome(message: Message):
    kp = [
        [
            types.KeyboardButton(text = 'Запустить тест'),
        ],
        ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard = kp
    )
    global test_data
    test_data = {
        'm': 0,
        'b': 0,
        't': 0,
        'i': 0,
        'type': ''
    }
    await message.answer('Привет! Этот бот позволяет пройти MBTI тестирование, основаннjt на теории Карла Юнга о психологических типах.', reply_markup=keyboard)

@router.message(F.text.lower()=="запустить тест")
async def reply_builder(message: Message):
    kp = [
        [
            types.KeyboardButton(text='В компании друзей'),
            types.KeyboardButton(text='В одиночестве')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kp
    )
    await message.answer("Вы предпочитаете проводить время в компании друзей или в одиночестве?", reply_markup=keyboard)

@router.message(F.text.lower()=="в компании друзей")
async def reply_builder(message: Message):
    global test_data
    test_data['m'] += 1
    kp = [
        [
            types.KeyboardButton(text='Легко завожу знакомства'),
            types.KeyboardButton(text='Нужно время, чтобы привыкнуть')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kp
    )
    await message.answer("Вы легко заводите новые знакомства или вам нужно время, чтобы привыкнуть к новым людям?", reply_markup=keyboard)

@router.message(F.text.lower()=="в одиночестве")
async def reply_builder(message: Message):
    global test_data
    test_data['m'] -= 1
    kp = [
        [
            types.KeyboardButton(text='Легко завожу знакомства'),
            types.KeyboardButton(text='Нужно время, чтобы привыкнуть')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kp
    )
    await message.answer("Вы легко заводите новые знакомства или вам нужно время, чтобы привыкнуть к новым людям?", reply_markup=keyboard)

@router.message(F.text.lower()=="легко завожу знакомства")
async def reply_builder(message: Message):
    global test_data
    test_data['m'] += 1
    kp = [
        [
            types.KeyboardButton(text='Вслух'),
            types.KeyboardButton(text='Про себя')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kp
    )
    await message.answer("Вы предпочитаете выражать свои мысли вслух или про себя?", reply_markup=keyboard)

@router.message(F.text.lower()=="нужно время, чтобы привыкнуть")
async def reply_builder(message: Message):
    global test_data
    test_data['m'] -= 1
    kp = [
        [
            types.KeyboardButton(text='Вслух'),
            types.KeyboardButton(text='Про себя')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kp
    )
    await message.answer("Вы предпочитаете выражать свои мысли вслух или про себя?", reply_markup=keyboard)

@router.message(F.text.lower()=="вслух")
async def reply_builder(message: Message):
    global test_data
    test_data['m'] += 1
    kp = [
        [
            types.KeyboardButton(text='Конкретные факты.'),
            types.KeyboardButton(text='Более общие идеи.')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kp
    )
    await message.answer("Вы больше запоминаете конкретные факты или более общие идеи?", reply_markup=keyboard)

@router.message(F.text.lower()=="про себя")
async def reply_builder(message: Message):
    global test_data
    test_data['m'] -= 1
    kp = [
        [
            types.KeyboardButton(text='Конкретные факты.'),
            types.KeyboardButton(text='Более общие идеи.')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kp
    )
    await message.answer("Вы больше запоминаете конкретные факты или более общие идеи?", reply_markup=keyboard)

@router.message(F.text.lower()=="конкретные факты.")
async def reply_builder(message: Message):
    global test_data
    test_data['t'] += 1
    kp = [
        [
            types.KeyboardButton(text='В конкретных примерах'),
            types.KeyboardButton(text='Через абстрактные концепции')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kp
    )
    await message.answer("Вы лучше понимаете информацию, когда она представлена в конкретных примерах, или через абстрактные концепции?", reply_markup=keyboard)

@router.message(F.text.lower()=="более общие идеи.")
async def reply_builder(message: Message):
    global test_data
    test_data['t'] -= 1
    kp = [
        [
            types.KeyboardButton(text='В конкретных примерах'),
            types.KeyboardButton(text='Через абстрактные концепции')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kp
    )
    await message.answer("Вы лучше понимаете информацию, когда она представлена в конкретных примерах, или через абстрактные концепции?", reply_markup=keyboard)

@router.message(F.text.lower()=="в конкретных примерах")
async def reply_builder(message: Message):
    global test_data
    test_data['t'] += 1
    kp = [
        [
            types.KeyboardButton(text='Традиционными методами'),
            types.KeyboardButton(text='Искать новые решения')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kp
    )
    await message.answer("Вам больше нравится решать проблемы традиционными методами или искать новые решения?", reply_markup=keyboard)

@router.message(F.text.lower()=="через абстрактные концепции")
async def reply_builder(message: Message):
    global test_data
    test_data['t'] -= 1
    kp = [
        [
            types.KeyboardButton(text='Традиционными методами'),
            types.KeyboardButton(text='Искать новые решения')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kp
    )
    await message.answer("Вам больше нравится решать проблемы традиционными методами или искать новые решения?", reply_markup=keyboard)

@router.message(F.text.lower()=="традиционными методами")
async def reply_builder(message: Message):
    global test_data
    test_data['t'] += 1
    kp = [
        [
            types.KeyboardButton(text='Логику'),
            types.KeyboardButton(text='Чувства')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kp
    )
    await message.answer("В решениях вы больше учитываете логику или свои чувства?", reply_markup=keyboard)

@router.message(F.text.lower()=="искать новые решения")
async def reply_builder(message: Message):
    global test_data
    test_data['t'] -= 1
    kp = [
        [
            types.KeyboardButton(text='Логику'),
            types.KeyboardButton(text='Чувства')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kp
    )
    await message.answer("В решениях вы больше учитываете логику или свои чувства?", reply_markup=keyboard)

@router.message(F.text.lower()=="логику")
async def reply_builder(message: Message):
    global test_data
    test_data['b'] += 1
    kp = [
        [
            types.KeyboardButton(text='О фактах'),
            types.KeyboardButton(text='Об эмоциях')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kp
    )
    await message.answer("Вы предпочитаете говорить о фактах или о свои эмоциях?", reply_markup=keyboard)

@router.message(F.text.lower()=="чувства")
async def reply_builder(message: Message):
    global test_data
    test_data['b'] -= 1
    kp = [
        [
            types.KeyboardButton(text='О фактах'),
            types.KeyboardButton(text='Об эмоциях')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kp
    )
    await message.answer("Вы предпочитаете говорить о фактах или о свои эмоциях?", reply_markup=keyboard)


@router.message(F.text.lower() == "о фактах")
async def reply_builder(message: Message):
    global test_data
    test_data['b'] += 1
    kp = [
        [
            types.KeyboardButton(text='В эффективности'),
            types.KeyboardButton(text='В гармонии в отношениях')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kp
    )
    await message.answer("Вы больше заинтересованы в эффективности или в гармонии в отношениях?", reply_markup=keyboard)

@router.message(F.text.lower() == "об эмоциях")
async def reply_builder(message: Message):
    global test_data
    test_data['b'] -= 1
    kp = [
        [
            types.KeyboardButton(text='В эффективности'),
            types.KeyboardButton(text='В гармонии в отношениях')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kp
    )
    await message.answer("Вы больше заинтересованы в эффективности или в гармонии в отношениях?", reply_markup=keyboard)

@router.message(F.text.lower() == "в эффективности")
async def reply_builder(message: Message):
    global test_data
    test_data['b'] += 1
    kp = [
        [
            types.KeyboardButton(text='Завершать все дела сразу'),
            types.KeyboardButton(text='Оставлять все на потом')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kp
    )
    await message.answer("Вы предпочитаете завершать все дела сразу или оставлять все на потом?", reply_markup=keyboard)

@router.message(F.text.lower() == "в гармонии в отношениях")
async def reply_builder(message: Message):
    global test_data
    test_data['b'] -= 1
    kp = [
        [
            types.KeyboardButton(text='Завершать все дела сразу'),
            types.KeyboardButton(text='Оставлять все на потом')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kp
    )
    await message.answer("Вы предпочитаете завершать все дела сразу или оставлять все на потом?", reply_markup=keyboard)

@router.message(F.text.lower() == "завершать все дела сразу")
async def reply_builder(message: Message):
    global test_data
    test_data['i'] += 1
    kp = [
        [
            types.KeyboardButton(text='Планировать свои действия'),
            types.KeyboardButton(text='Я большой любитель сосасть блольшие хуи')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kp
    )
    await message.answer("Вы больше любите планировать свои действия или действовать спонтанно?", reply_markup=keyboard)

@router.message(F.text.lower() == "оставлять все на потом")
async def reply_builder(message: Message):
    global test_data
    test_data['i'] -= 1
    kp = [
        [
            types.KeyboardButton(text='Планировать свои действия'),
            types.KeyboardButton(text='Я большой любитель сосасть блольшие хуи')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kp
    )
    await message.answer("Вы больше любите планировать свои действия или действовать спонтанно?", reply_markup=keyboard)

@router.message(F.text.lower() == "планировать свои действия")
async def reply_builder(message: Message):
    global test_data
    test_data['i'] += 1
    kp = [
        [
            types.KeyboardButton(text='Строгий режим дня'),
            types.KeyboardButton(text='Более гибкий расписание')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kp
    )
    await message.answer("Вы предпочитаете строгий режим дня или более гибкий расписание?", reply_markup=keyboard)

@router.message(F.text.lower() == "я большой любитель сосасть блольшие хуи")
async def reply_builder(message: Message):
    global test_data
    test_data['i'] -= 1
    kp = [
        [
            types.KeyboardButton(text='Строгий режим дня'),
            types.KeyboardButton(text='Более гибкий расписание')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kp
    )
    await message.answer("Вы предпочитаете строгий режим дня или более гибкий расписание?", reply_markup=keyboard)

@router.message(F.text.lower() == "строгий режим дня")
async def reply_builder(message: Message):
    global test_data
    test_data['i'] += 1
    kp = [
        [
            types.KeyboardButton(text='Узнать результаты')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kp
    )
    await message.answer("Тестирование завершено", reply_markup=keyboard)

@router.message(F.text.lower() == "более гибкий расписание")
async def reply_builder(message: Message):
    global test_data
    test_data['i'] -= 1
    kp = [
        [
            types.KeyboardButton(text='Узнать результаты')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kp
    )
    await message.answer("Тестирование завершено", reply_markup=keyboard)

@router.message(F.text.lower() == "узнать результаты")
async def reply_builder(message: Message):
    global test_data
    if test_data['m']>0:
        test_data['type'] += 'E'
    else:
        test_data['type'] += 'I'
    if test_data['t']>0:
        test_data['type'] += 'S'
    else:
        test_data['type'] += 'N'
    if test_data['b']>0:
        test_data['type'] += 'T'
    else:
        test_data['type'] += 'F'
    if test_data['i']>0:
        test_data['type'] += 'J'
    else:
        test_data['type'] += 'P'
    await message.answer(test_data['type'])
    print(test_data['m'], test_data['b'], test_data['t'], test_data['i'])



async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
