# spotify2vkstatus

Use currently playing track to status in VK.com

## Requirements
- spotipy
- vk_api

⚠️ **Use the last version of [spotipy](https://github.com/plamere/spotipy)**

## Setup

### Spotify
1. Create Spotify app: https://developer.spotify.com/dashboard
2. Add "http://localhost:8888/callback/" in app redirect URIs
3. Complete the **settings.py** with app client_id, client_secret, username

### VK.com
1. Get access token: https://vk.cc/8Abj47
2. Complete the **settings.py** with token

## Usage

```
python3 spotify2vkstatus.py
```

## TODO
- [x] Spotify token auto refresh (every hour)
- [ ] Auth without browser