#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets
import json

async def send_data(websocket, path):
    while True:
        rd = random.random()
        data = json.dumps( {"data1": str(rd), "data2": str(rd + 1)} )        
        await websocket.send( str(data) )
        await asyncio.sleep( 1 )

start_server = websockets.serve(send_data, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()