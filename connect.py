import asyncio
from bleak import BleakClient

async def main():
    ble_address = "DC:0D:30:F9:A5:A3"

    async with BleakClient(ble_address) as client:
        # we’ll do the read/write operations here
        print("Connected to BLE device")
        print(client.is_connected)        

asyncio.run(main())