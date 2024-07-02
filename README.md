# SD Dispensing Unit Command Interface

This repository contains individual Python scripts to control the SD dispensing unit using serial commands. Each script corresponds to a specific command that can be sent to the SD dispensing unit via a serial port.

## Prerequisites

- Python 3.x
- `pyserial` library

## Installation

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

## Commands

### Start Moving Up
**Script:** `up.py`

**Important:** The `tbps` speed must be set prior to using the `up` command to ensure proper manual control.

```bash
python up.py
```

## Start Moving Down

**Script:** `down.py`

**Important:** The `tbps` speed must be set prior to using the `down` command to ensure proper manual control.

```bash
python down.py
```

## Stop Movement
**Script:** `stop.py`

```bash
python stop.py
```


##  Set Syringe Size

**Script:** size.py

Usage: Provide the syringe size as a command line argument.

Value Limits: 3700000 for 30cc or 7400000 for 55cc syringes.

```bash
python size.py <size>
```

**Example:** 

```bash
python size.py 3700000
```

##  Set Dispensing Speed

**Script:**  speed.py

**Usage:** Provide the dispensing speed as a command line argument.

**Value Limits:** Normal values are between 0 - 100, but can be more.

```bash
python speed.py <speed>
```

**Example:**

```bash
python speed.py 50
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


# Move Home
**Script**: home.py

```bash
python home.py
```

# Check Connection
**Script**: ping.py

```bash
python ping.py
```

# Set Toolbar Speed
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

# Start Priming

**Script**: prime.py

```bash
python prime.py
```

# Example Commands

**Start moving up**:

```bash
python up.py
```

**Set syringe size to 3700000**:

```bash
python size.py 3700000
```

**Set dispensing speed to 50**:

```bash
python speed.py 50
```

**Stop movement**:

```bash
python stop.py
```

**Set toolbar speed to 100**:

```bash
python tbps.py 100
```

**Start priming**:

```bash
python prime.py
```
# Move Home
**Script**: home.py

```bash
python home.py
```

# Check Connection
**Script**: ping.py

```bash
python ping.py
```

# Set Toolbar Speed
**Script**: tbps.py

**Usage**: Provide the toolbar speed as a command line argument.

**Value Limits**: Values between 1 - 400.

```bash
python tbps.py <speed>
```

**Example**:

```bash
python tbps.py 100
```

**Important**: The tbps speed must be set before using the up and down commands as they rely on this speed setting for manual control.

# Start Priming
**Script**: prime.py

```bash
python prime.py
```

# Example Commands

**Start moving up**:

```bash
python up.py
```

**Set syringe size to 3700000**:

```bash
python size.py 3700000
```

**Set dispensing speed to 50**:

```bash
python speed.py 50
```

**Stop movement**:

```bash
python stop.py
```

**Set toolbar speed to 100**:

```bash
python tbps.py 100
```

**Start priming**:

```bash
python prime.py
```

**Set prefeed steps to 300**:

```bash
python feed.py 300
```

# Notes
- Ensure that the `SERIAL_PORT` in `common.py` is correctly set to match the connected USB port of your Arduino.
- The scripts expect the SD dispensing unit to respond with data. Ensure the unit is properly connected and configured.
- The tbps speed setting is crucial for the manual control commands (up and down). Make sure to set it appropriately before using these commands.
```



