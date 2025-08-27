# XPrinter Python

Python code to use XPrinter 365B USB+Bluetooth thermal printer.

# Bluetooth
We can use bleak library to connect with the printer over bluetooth. Then we can write raw text or ESC/POS commands to specific GATT characteristic to initiate the print.

Setup virtual environment and install python libraries.

    python -m venv .venv
    . .venv/bin/activate
    pip install bleak


Run `ble_scan.py` to discover devices and find mac address of the printer.

    python ble_scan.py

Set the mac address in the `ble_print.py`.
Run `ble_print.py` to print a sample.

    python ble_print.py
