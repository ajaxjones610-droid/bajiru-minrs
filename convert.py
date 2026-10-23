import os
import pickle

# Create the cookies directory if it doesn't exist
os.makedirs('cookies', exist_ok=True)

# Save cookie structure matching TwitchLogin expectations
cookies_list = [
    {
        "domain": ".twitch.tv",
        "name": "auth-token",
        "value": "bjw1vx29ajqnub0l77c3f0jhy958yy",
        "path": "/",
        "secure": True
    },
    {
        "domain": ".twitch.tv",
        "name": "login",
        "value": "computergeek619",
        "path": "/",
        "secure": True
    }
]

with open('cookies/computergeek619.pkl', 'wb') as f:
    pickle.dump(cookies_list, f)

print("SUCCESS: Generated cookies/computergeek619.pkl")