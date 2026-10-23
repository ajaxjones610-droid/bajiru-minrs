import sys
import time
import threading
import logging
from TwitchChannelPointsMiner import TwitchChannelPointsMiner
from TwitchChannelPointsMiner.classes.Settings import Priority, Settings
from TwitchChannelPointsMiner.classes.Entities.Bet import Strategy

# 1. Background timer to stop execution cleanly after 5.5 hours (19,800 seconds)
def auto_stop():
    time.sleep(19800)  # 5 hours and 30 minutes
    print("\n[!] Reached maximum 5.5-hour runtime limit. Shutting down cleanly...")
    sys.exit(0)

# Start the auto-stop timer thread
threading.Thread(target=auto_stop, daemon=True).start()

# 2. Configure Twitch Channel Points Miner
twitch_miner = TwitchChannelPointsMiner(
    username="computergeek619",
    claim_drops_startup=True,
    enable_stream_predictions=False,  # Set to True if you want it to bet on predictions
    settings=Settings(
        get_dark_theme=True,
        log_file=False,               # Prints directly to GitHub Actions console logs
        disable_graphics=True          # Saves memory on cloud servers
    )
)

# 3. Target Streamer Configuration
twitch_miner.mine(
    [
        ("bajiru_en", Priority.HIGH)
    ]
)
