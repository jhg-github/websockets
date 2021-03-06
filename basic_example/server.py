#!/usr/bin/env python

# WS server example

# https://websockets.readthedocs.io/en/stable/intro.html
# It reads a name from the client, sends a greeting, and closes the connection.
# On the server side, websockets executes the handler coroutine hello once for 
# each WebSocket connection. It closes the connection when the handler coroutine returns.

import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()