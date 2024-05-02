import asyncio
import websockets
import requests
import json
import time

import logging
logger = logging.getLogger(__name__)

class LoginError(Exception):
    pass

class SaveReplayError(Exception):
    pass

class PSWebsocketClient:

    websocket = None
    address = None
    login_uri = None
    username = None
    password = None
    last_message = None
    last_challenge_time = 0

    @classmethod
    async def create(cls, username, password, address):
        self = PSWebsocketClient()
        self.username = username
        self.password = 