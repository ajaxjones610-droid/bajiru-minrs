import sys
import time
import threading
from TwitchChannelPointsMiner import TwitchChannelPointsMiner
from TwitchChannelPointsMiner.classes.entities.Streamer import StreamerSettings

# 1. Stop cleanly at 5 hours and 35 minutes (20,100 seconds) before GitHub's 6-hour cutoff
def auto_stop():
    time.sleep(20100)
    print("\n[!] Reached 5h 35m limit. Shutting down cleanly...")
    sys.exit(0)

threading.Thread(target=auto_stop, daemon=True).start()

# 2. Configure Miner with StreamerSettings: NO predictions/betting, YES to raids
twitch_miner = TwitchChannelPointsMiner(
    username="computergeek619",
    streamer_settings=StreamerSettings(
        make_predictions=False,  # Strictly disables gambling/predictions
        follow_raid=True,        # Stays and follows raids (+250 pts)
        claim_drops=True         # Auto-claims drops/bonuses
    )
)

# 3. Mine bajiru_en
twitch_miner.mine(["bajiru_en"])
