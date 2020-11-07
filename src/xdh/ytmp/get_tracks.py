import ytmusicapi

MAX_SONGS = 50000

ytmusic = ytmusicapi.YTMusic("headers_auth.json")

total_tracks = ytmusic.get_library_upload_songs(MAX_SONGS)
