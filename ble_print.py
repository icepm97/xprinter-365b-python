import asyncio
from bleak import BleakClient

# mac address of the printer
mac_address = "DC:0D:30:F9:A5:A3"

# characteristic to write to
print_characteristic = 'bef8d6c9-9c21-4c9e-b632-bd58c1009f9f'


async def main():
    ble_address = "DC:0D:30:F9:A5:A3"

    # connect to the printer
    async with BleakClient(ble_address) as client:
        print("Connected to the printer")
        print(client.is_connected)   

        # write to ble device
        await client.write_gatt_char(print_characteristic, b'Hello, World!\n', response=False)

        # disconnect from the printer
        await client.disconnect()

asyncio.run(main())
