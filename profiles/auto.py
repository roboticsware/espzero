"""
espzero/profiles/auto.py
Runtime board auto-detection.

Inspects sys.implementation._machine to identify the chip and returns
the matching board profile key used in espzero._PROFILE_MAP.
"""
import sys


def detect():
    """
    Detect the current board at runtime by inspecting sys.implementation._machine.

    Returns a board key string that corresponds to an entry in
    espzero._PROFILE_MAP (e.g. 'esp32_devkit_v1').
    Falls back to 'esp32_devkit_v1' (WROOM) if detection fails.
    """
    try:
        machine_str = sys.implementation._machine.lower()
    except AttributeError:
        machine_str = ""

    if "esp32s3" in machine_str or "esp32-s3" in machine_str:
        return "esp32_s3_devkit"
    elif "esp32c3" in machine_str or "esp32-c3" in machine_str:
        return "esp32_c3_mini"
    elif "esp32" in machine_str:
        return "esp32_devkit_v1"
    else:
        print("[espzero] WARNING: Could not auto-detect board. "
              "Falling back to 'esp32_devkit_v1' profile. "
              "Call espzero.begin('<board_name>') to specify your board.")
        return "esp32_devkit_v1"
