import sys
import time
import threading
from TwitchChannelPointsMiner import TwitchChannelPointsMiner
from TwitchChannelPointsMiner.logger import Logger
from TwitchChannelPointsMiner.classes.Settings import Settings, FollowersOrder

# 1. Background timer to stop execution cleanly after 5.5 hours (19,800 seconds)
def auto_stop():
    time.sleep(19800)  # 5 hours and 30 minutes
    print("\n[!] Reached maximum 5.5-hour runtime limit. Shutting down cleanly...")
    sys.exit(0)

# Start the auto-stop timer thread
threading.Thread(target=auto_stop, daemon=True).start()

# 2. Configure Twitch Channel Points Miner with point-saving safety settings
twitch_miner = TwitchChannelPointsMiner(
    username="computergeek619",
    settings=Settings(
        # Disable all automated betting/predictions so your points only go UP
        BET={"strategy": "none", "percentage": 0, "max_points": 0},
        # Optional: Adjust logging or collection speed if needed
    )
)

# 3. Start mining for bajiru_en safely
twitch_miner.mine(
    ["bajiru_en"]
)
