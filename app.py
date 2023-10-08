import asyncio
import websockets
import door

async def handler(websocket):
    print(f"Client connected from {websocket.remote_address}")

    try:
        while True:

            state = door.getState()

            print(f"Door is {state}")

            if state is not None:
                await websocket.send(state)
                await asyncio.sleep(0.5)

    except websockets.exceptions.ConnectionClosedOK:
        print(f"Client {websocket.remote_address} disconnected")

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())