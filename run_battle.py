import importlib
import json
import asyncio
import concurrent.futures
from copy import deepcopy
import logging

from websocket_client import PSWebsocketClient

logger = logging.getLogger(__name__)

async def start_random_battle(ps_websocket_client: PSWebsocketClient, pokemon_battle_type):
    battle, opponent_id, user_json = await initialize_battle_with_tag(ps_websocket_client)
    battle.battle_type = constants.RANDOM_BATTLE
