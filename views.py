from bottery.message import Message, render
from bottery.platform.telegram.utils import BaseDecorator


class Reply(BaseDecorator):
    def prepare(self, message):
        return {'reply_to_message_id': message.id - 1}

@Reply()
async def reply_shrug(message):
    return '¯\\\_(ツ)\_/¯'

async def shrug(message):
    treated_msg = ' '.join(message.raw['message']['text'].split()[1:])
    print(treated_msg)
    shrug_emoji = '¯\\\_(ツ)\_/¯'
    return f'{treated_msg} {shrug_emoji}'
