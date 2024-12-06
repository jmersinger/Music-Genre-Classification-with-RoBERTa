import pandas as pd
import kagglehub

def download_and_clean():
    
    path = kagglehub.dataset_download("yamaerenay/spotify-dataset-19212020-600k-tracks")
    artists_path = path + '/artists.csv'
    tracks_path = path + '/tracks.csv'
    
    artists_df = pd.read_csv(artists_path)
    tracks_df = pd.read_csv(tracks_path)
    
    artists_df = artists_df.dropna().drop_duplicates()
    tracks_df = tracks_df.dropna().drop_duplicates()
    
    artists_df = artists_df[artists_df['genres'].apply(lambda x: len(eval(x)) > 0 if isinstance(x, str) else False)]
    
    valid_artists = set(artists_df['name'])
    tracks_df = tracks_df[tracks_df['artists'].apply(lambda x: all(artist in valid_artists for artist in eval(x)) if isinstance(x, str) else False)]
    
    artist_to_genres = dict(zip(artists_df['name'], artists_df['genres']))
    
    def get_genres_for_track(artists_list):
        if isinstance(artists_list, str):
            try:
                artists_list = eval(artists_list)
                genres = [genre for artist in artists_list if artist in artist_to_genres for genre in eval(artist_to_genres[artist])]
                return list(set(genres))
            except:
                return []
        return []
    
    tracks_df['genres'] = tracks_df['artists'].apply(get_genres_for_track)
    
    artists_df.to_csv('./data/cleaned_data/cleaned_artists.csv', index=False)
    tracks_df.to_csv('./data/cleaned_data/cleaned_tracks.csv', index=False)

    return artists_df, tracks_df
