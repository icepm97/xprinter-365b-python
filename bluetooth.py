from bleak import BleakScanner, BleakClient
import asyncio

import bleak


async def scan():
    devices = await BleakScanner.discover()

    for device in devices:
        print(device)

async def connect():
    device_address = 'DC:0D:30:F9:A5:A3'
    client = BleakClient(device_address)
    await client.connect()
    print(f"Connected to {device_address}")
    await client.disconnect()

if __name__ == "__main__":
    # asyncio.run(scan())
    asyncio.run(connect())


from bleak import BleakClient, BleakScanner 
devices = await BleakScanner.discover()
devices

from bleak import BleakClient, BleakScanner 
device = await BleakScanner.find_device_by_address('DC:0D:30:F9:A5:A3')
client = BleakClient(device)
await client.connect()

client.disconnect()