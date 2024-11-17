import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from buttons import *

from dotenv import dotenv_values

secret_keys = dotenv_values('.env')

# Bot token can be obtained via https://t.me/BotFather
TOKEN = secret_keys['BOT_TOKEN']

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()


authenticator = IAMAuthenticator(secret_keys['AI_API'])  # Replace with your API key
assistant = AssistantV2(
    version='2021-11-27',
    authenticator=authenticator
)
assistant.set_service_url(secret_keys['SERVICE_URL'])  # Replace with your service instance URL
assistant_id = secret_keys['ASSISTANT_ID']  # Replace with your assistant ID

# Dictionary to store Watson Assistant contexts per user
user_contexts = {}


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello! How can I help you today?", reply_markup=main_buttons)


@dp.message()
async def handle_message(message: Message):
    user_id = message.from_user.id

    context = user_contexts.get(user_id, {})

    # Prepare message input
    message_input = {
        'message_type': 'text',
        'text': message.text
    }

    # Send message to Watson Assistant
    try:
        result = assistant.message_stateless(
            assistant_id=assistant_id,
            input=message_input,
            context=context
        ).get_result()

        # Update the user's context
        user_contexts[user_id] = result.get('context', {})

        # Send Watson Assistant's response(s) to the user
        responses = result['output']['generic']
        for response in responses:
            if response['response_type'] == 'text':
                if "types of jobs" in response['text'] or "Choose an area" in response['text']:
                    await message.answer(response['text'], reply_markup=job_types)
                elif "Do you have work experience" in response['text'] or "Should we start?" in response['text'] or "Want to start your application and general interview process?" in response['text'] or "Firstly, have you got it or you don't have a work experience at all?" in response['text'] or "Do you confirm all data stated by you is correct and agree the company is likely to delete your application due to wrong information provided?" in response['text'] or "Do you want to continue with the previous topic" in response['text']:
                    await message.answer(response['text'], reply_markup=yes_no)
                elif "What is your level of degree?" in response['text'] or "What is the level of your degree" in response['text']:
                    await message.answer(response['text'], reply_markup=levels_of_edu)
                elif "What is your sex?" in response['text']:
                    await message.answer(response['text'], reply_markup=sex)
                elif "Security" in response['text']:
                    await message.answer(response['text'], reply_markup=security)
                elif "Where are you based?" in response['text']:
                    await message.answer(response['text'], reply_markup=countries)
                elif "Cleaning staff" in response['text']:
                    await message.answer(response['text'], reply_markup=cleaning_staff)
                elif "Developers" in response['text']:
                    await message.answer(response['text'], reply_markup=devs)
                elif "SMM" in response['text']:
                    await message.answer(response['text'], reply_markup=SMM)
                elif "Designer" in response['text']:
                    await message.answer(response['text'], reply_markup=designer)
                elif "Bookkeeping" in response['text']:
                    await message.answer(response['text'], reply_markup=bookkeeping)
                else:
                    await message.answer(response['text'], reply_markup=main_buttons)

    except Exception as e:
        await message.answer(f"An error occurred: {str(e)}")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN)

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
