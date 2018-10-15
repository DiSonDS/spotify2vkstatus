import spotipy
import spotipy.util as util
import vk_api
import time
import sys
from settings import *


def main():

    def get_spotify_token():
        token = util.prompt_for_user_token(SPOTIFY_USERNAME, SPOTIFY_SCOPE, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET,
                                           SPOTIFY_REDIRECT_URL)
        return token

    # Spotify init
    sp_session = get_spotify_token()

    # VK init
    vk_session = vk_api.VkApi(token=VK_USER_TOKEN)
    vk = vk_session.get_api()

    last_id = 0

    while True:
        if sp_session:
            spotify = spotipy.Spotify(auth=sp_session)
            try:
                results = spotify.current_user_playing_track()
            except spotipy.client.SpotifyException:
                print("Needs a new token")
                sp_session = get_spotify_token()
                continue
            if not results:
                if last_id:
                    last_id = 0
                    vk.status.set(text="")
                time.sleep(INTERVAL)
                continue
            is_playing = results['is_playing']
            track_id = results['item']['id']
            if is_playing:
                if track_id != last_id:
                    artist_name = results['item']['artists'][0]['name']
                    track_name = results['item']['name']
                    time_now = time.strftime("%H:%M", time.localtime())
                    status_text = f"🎧 Spotify | {artist_name} — «{track_name}»"
                    print(f"[{time_now}] {status_text}")
                    vk.status.set(text=status_text)
                    last_id = track_id
                    time.sleep(INTERVAL)
                else:
                    time.sleep(INTERVAL)
            else:
                last_id = 0
                vk.status.set(text="")
                time.sleep(INTERVAL)
        else:
            print(f"Can't get token {SPOTIFY_USERNAME}")
            sys.exit()


if __name__ == "__main__":
    main()