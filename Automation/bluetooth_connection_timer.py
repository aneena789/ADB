import subprocess
import re
from datetime import datetime

# Configuration
DEVICE_NAME = "Boult Audio Airbass"
TIME_FORMAT = "%m-%d %H:%M:%S.%f"

# Define connection indicators
start_keywords = [
    "Device name: " + DEVICE_NAME,
    "ACL connected",
]

end_keywords = [
    "a2dp=true",
    "Audio device added: " + DEVICE_NAME
]

start_time = None

print("📡 Listening to ADB logcat... Connect your Bluetooth device.\n")

# Start logcat
process = subprocess.Popen(
    ["adb", "logcat", "-v", "time"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    encoding="utf-8",
    errors="ignore"
)

try:
    for line in process.stdout:
        line = line.strip()

        # Match start line
        if any(kw in line for kw in start_keywords) and not start_time:
            timestamp_str = line[:18]
            start_time = datetime.strptime(timestamp_str, TIME_FORMAT)
            print(f" Connection started at: {timestamp_str} → {line}")

        # Match end line
        elif any(kw in line for kw in end_keywords) and start_time:
            timestamp_str = line[:18]
            end_time = datetime.strptime(timestamp_str, TIME_FORMAT)
            print(f" Connection completed at: {timestamp_str} → {line}")
            print(f" Total connection time: {end_time - start_time}")
            break

except KeyboardInterrupt:
    print("\nInterrupted by user.")
finally:
    process.terminate()
