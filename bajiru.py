import ssl
import time
import threading
import logging
import requests
import urllib3

# Suppress warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Monkey-patch default requests headers to mimic a real Windows web browser
original_session_init = requests.Session.__init__
def custom_session_init(self, *args, **kwargs):
    original_session_init(self, *args, **kwargs)
    self.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Client-Id': 'kimne78kx3ncx6brogo4mv6wki5h1ko',
    })
requests.Session.__init__ = custom_session_init

from TwitchChannelPointsMiner import TwitchChannelPointsMiner
from TwitchChannelPointsMiner.logger import LoggerSettings
from TwitchChannelPointsMiner.classes.Settings import Priority
from TwitchChannelPointsMiner.classes.entities.Streamer import Streamer, StreamerSettings

RUN_DURATION = 5400  # 1.5 hours in seconds

while True:
    print('\n--- Starting Dedicated Bajiru Miner Session ---')

    twitch_miner = TwitchChannelPointsMiner(
        username="computergeek619",
        password=None,  # Uses cookies/computergeek619.pkl
        claim_drops_startup=True,
        priority=[Priority.STREAK, Priority.DROPS, Priority.ORDER],
        logger_settings=LoggerSettings(
            save=True,
            console_level=logging.INFO,
            file_level=logging.DEBUG,
        )
    )

    bajiru_settings = StreamerSettings(
        make_predictions=False,
        follow_raid=True,
        claim_drops=True,
        watch_streak=True,
    )

    twitch_miner.mine(
        [
            Streamer("bajiru_en", settings=bajiru_settings),
        ]
    )

    def stop_session():
        time.sleep(RUN_DURATION)
        print('\n[Auto-Restart] 1.5 hours elapsed. Restarting Bajiru session...')
        try:
            twitch_miner.stop()
        except AttributeError:
            pass

    timer_thread = threading.Thread(target=stop_session, daemon=True)
    timer_thread.start()

    try:
        twitch_miner.run()
    except Exception as e:
        print(f"Bajiru session closed with error/restart: {e}")

    time.sleep(5)
