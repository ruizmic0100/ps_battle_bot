import asyncio
import json
import logging
import traceback
from datetime import datetime
from copy import deepcopy

import constants
from config import ShowdownConfig, init_logging

from teams import load_team
from run_battle import pokemon_battle
from websocket_client import PSWebsocketClient

from data import all_move_json
from data import pokedex

logger = logging.getLogger(__name__)

def check_dictionaries_are_unmodified(original_pokedex, original_move_json):
    # The bot should not modify the data dictionaries
    # this is a "just-in-case" check to make sure and will stop the bot if it mutates either of them.
    if original_move_json != all_move_json:
        logger.critical("Move JSON changed!\nDumping modified version to `modified_moves.json`")
        with open("modified_moves.json", 'w') as f:
            json.dump(all_move_json, f, indent=4)
        exit(1)