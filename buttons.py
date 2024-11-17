from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardBuilder

main_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Available vacancies"), KeyboardButton(text="Apply for a job")],
        [KeyboardButton(text="Vacancies for me"), KeyboardButton(text="Access my application")],
        [KeyboardButton(text="What can you do?"), KeyboardButton(text="About company")],
        [KeyboardButton(text="Other...")],
    ], resize_keyboard=True, one_time_keyboard=True
)


job_types = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Security"), KeyboardButton(text="Cleaning staff")],
        [KeyboardButton(text="Developers"), KeyboardButton(text="Bookkeeping")],
        [KeyboardButton(text="Designer"), KeyboardButton(text="SMM")],
    ], resize_keyboard=True, one_time_keyboard=True
)


security = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Indoors security")],
        [KeyboardButton(text="Checkpoint security")]
    ], resize_keyboard=True, one_time_keyboard=True
)

devs = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Data scientist")],
        [KeyboardButton(text="C++/C developer")],
        [KeyboardButton(text="Web developer")],
    ], resize_keyboard=True, one_time_keyboard=True
)

bookkeeping = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Bookkeeper")],
        [KeyboardButton(text="Secretary")],
    ], resize_keyboard=True, one_time_keyboard=True
)

designer = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Web-designer")],
        [KeyboardButton(text="UI/UX designer")],
        [KeyboardButton(text="Posts designer")],
    ], resize_keyboard=True, one_time_keyboard=True
)

countries = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Uzbekistan")],
        [KeyboardButton(text="Kazakhstan")],
        [KeyboardButton(text="Kyrgyzstan")],
        [KeyboardButton(text="Tajikistan")],
    ], resize_keyboard=True, one_time_keyboard=True
)

SMM = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="SMM manager")],
        [KeyboardButton(text="Mobilography")]
    ], resize_keyboard=True, one_time_keyboard=True
)

cleaning_staff = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Cleaner")]
    ], resize_keyboard=True, one_time_keyboard=True
)

proceed = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Follow the instructions")]
    ], resize_keyboard=True, one_time_keyboard=True
)



yes_no = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="YES"), KeyboardButton(text="NO")]
    ], resize_keyboard=True, one_time_keyboard=True
)

levels_of_edu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Secondary education")],
        [KeyboardButton(text="Bachelor's")],
        [KeyboardButton(text="Master's")],
        [KeyboardButton(text="PhD")],
    ], resize_keyboard=True, one_time_keyboard=True
)

sex = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Male")],
        [KeyboardButton(text="Female")],
    ], resize_keyboard=True, one_time_keyboard=True
)

