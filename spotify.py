import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = 'df66bca8951d4992b4cb34f70b5900e8'
SPOTIPY_CLIENT_SECRET = '24efeccdd4b540a0b3e4b3a2d1a9f349'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="user-library-read user-top-read"))

def get_user_favorites():
    
    results = sp.current_user_top_artists(limit=5)
    favorite_artists = []

    print("Favori sanatçılarınız:")
    for idx, artist in enumerate(results['items']):
        print(f"{idx + 1}: {artist['name']}")
        favorite_artists.append(artist['id'])

    return favorite_artists

def get_recommendations_based_on_artists(artist_ids):
    
    recommendations = sp.recommendations(seed_artists=artist_ids, limit=10)
    print("\nSanatçılarınıza göre önerilen şarkılar:")
    
    for idx, track in enumerate(recommendations['tracks']):
        print(f"{idx + 1}: {track['name']} by {track['artists'][0]['name']}")

def main():
    print("Spotify Müzik Öneri Uygulamasına Hoş Geldiniz!")
    
    
    favorite_artists = get_user_favorites()
    
    
    get_recommendations_based_on_artists(favorite_artists)

if __name__ == "__main__":
    main()
