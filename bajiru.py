import threading
import time
import sys
from TwitchChannelPointsMiner import TwitchChannelPointsMiner
from TwitchChannelPointsMiner.classes.Settings import Priority

# 1. Function to auto-stop the script after 5.5 hours (19,800 seconds)
def auto_stop():
    time.sleep(19800)  # 5 hours and 30 minutes
    print("Reached maximum 5.5-hour runtime limit. Shutting down cleanly...")
    sys.exit(0)

# Start timer in background
threading.Thread(target=auto_stop, daemon=True).start()

# 2. Your standard miner setup
twitch_miner = TwitchChannelPointsMiner(
    username="computergeek619",
    claim_drops_startup=True
)

twitch_miner.mine(
    [
        ("bajiru_en", Priority.HIGH)
    ],
    get_dark_theme=True
)
