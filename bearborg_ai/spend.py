import os
import json
import requests

from jupyter_ai.chat_handlers.base import BaseChatHandler, SlashCommandRoutingType
from jupyter_ai.models import HumanChatMessage

class BearBorgSpendSlashCommand(BaseChatHandler):

    id = "spend"
    name = "BearBorg Budget Info"
    help = "Get spend and budget info for BearBorg User"
    routing_type = SlashCommandRoutingType(slash_id="spend")

    uses_llm = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def process_message(self, message: HumanChatMessage):

        key = os.environ.get('LITELLM_API_KEY')
	
        response = requests.get(os.environ.get('LITELLM_SERVER', 'https://bearborg.berkeley.edu:4433') + '/key/info', headers={ 'Authorization': 'Bearer ' + key })

        user_id = response.json()['info']['user_id']

        response = requests.get(os.environ.get('LITELLM_SERVER', 'https://bearborg.berkeley.edu:4433') + '/user/info', params={ 'user_id': user_id }, headers={ 'Authorization': 'Bearer ' + key })

        info = response.json()

        print(json.dumps(info, indent=4))

        self.reply(f"User ID: {user_id}\n* Spend: {info['user_info']['spend']}\n* Budget: {info['user_info']['max_budget']}\n* Budget Reset At: {info['user_info']['budget_reset_at']}")