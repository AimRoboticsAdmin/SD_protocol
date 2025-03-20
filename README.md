# SD Dispensing Unit Command Interface

This repository contains individual Python scripts to control the SD dispensing unit using serial commands. Each script corresponds to a specific command that can be sent to the SD dispensing unit via a serial port.

# Prerequisites

- Python 3.x
- `pyserial` library

# Installation

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>

2. **Install the required library:**
   ```bash
    pip install pyserial



3. **Update the serial port:**

Modify the SERIAL_PORT variable in common.py to match your specific USB port (e.g., /dev/ttyUSB0).


# Usage
Each script can be executed independently from the command line to send specific commands to the SD dispensing unit.

## Common Functionality
All scripts use the `send_command` function defined in `common.py` to handle serial communication.

# Commands only used for manual toolbar changes in UI

## Set Toolbar Speed
**Script**: tbps.py

**Usage**: Provide the toolbar speed as a command line argument.

**Value Limits**: Values between 1 - 100.

```bash
python tbps.py <speed>
```

**Example**:

```bash
python tbps.py 100
```

**Important**: The tbps speed must be set before using the up and down commands as they rely on this speed setting for manual control.

## Start Moving Down

**Script:** `down.py`

**Important:** The `tbps` speed must be set prior to using the `down` command to ensure proper manual control.

```bash
python down.py
```
## Start Moving Up
**Script:** `up.py`

**Important:** The `tbps` speed must be set prior to using the `up` command to ensure proper manual control.

```bash
python up.py
```

## Stop Movement
**Script:** `stop.py`

```bash
python stop.py
```

# Commands used for dispensing

##  Set Syringe Size

**Script:** size.py

Usage: Provide the syringe size as a command line argument.

Value Limits: 4350000 for 30cc or 8000000 for 55cc syringes.

```bash
python size.py <size>
```

**Example:** 

```bash
python size.py 4350000
```

## Set Prefeed Steps
**Script:** feed.py

**Usage:** Provide the number of prefeed steps as a command line argument.

**Value Limits:** Values between 1 - 500.

```bash
python feed.py <steps>
```

**Example:**

```bash
python feed.py 300
```

##  Set Dispensing Speed

**Script:**  speed.py

**Usage:** Provide the dispensing speed as a command line argument.

**Value Limits:** Values are between 0 - 100.

```bash
python speed.py <speed>
```

**Example:**

```bash
python speed.py 50
```

##  Stop Dispensing

**Script:**  speed.py

```bash
python speed.py 0
```

##  Set Retraction Steps

**Script:**  retr.py

**Usage:**  Provide the number of retraction steps as a command line argument.

**Value Limits:**  Values between 1 - 500.

```bash
python retr.py <steps>
```

**Example:**

```bash
python retr.py 250
```

## Move Home
**Script**: home.py

```bash
python home.py
```

## Check Connection
**Script**: ping.py

```bash
python ping.py
```

**Important**: The tbps speed must be set before using the up and down commands as they rely on this speed setting for manual control.

## Start Priming

**Script**: prime.py

**Usage:** Piston will stop when he feels resistance of material

```bash
python prime.py
```


# Notes
- Ensure that the `SERIAL_PORT` in `common.py` is correctly set to match the connected USB port of the Tool.
- The scripts expect the SD dispensing unit to respond with data. Ensure the unit is properly connected and configured.
- The tbps speed setting is crucial for the manual control commands (up and down). Make sure to set it appropriately before using these commands.
```



