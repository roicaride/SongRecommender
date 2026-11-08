# SongRecommender 🎵

Content-based song recommender built on Spotify audio features. Search for a song and get similar tracks based on how they *sound* — tempo, danceability, acousticness, energy-related features — rather than on what other users listened to.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white)

## How it works

1. **Cleaning & normalisation** (`data/limpieza_datos.ipynb`) — removes nulls and duplicates from the Spotify dataset, scales numeric features to [0, 1] and keeps the original values for display.
2. **Clustering** — K-Means groups the catalogue into 100 clusters of acoustically similar songs.
3. **Nearest neighbours** — for a query song, a k-NN model (Euclidean distance) is built only inside its cluster and returns the 5 closest tracks. Restricting the search to one cluster keeps queries fast and recommendations relevant.

Features used: year, popularity, duration, loudness, tempo, danceability, acousticness, instrumentalness, liveness and speechiness.

## Project structure

```
SongRecommender/
├── backend/
│   ├── app_flask.py        # REST API (find song, get recommendations)
│   ├── recommender.py      # clustering + k-NN logic
│   └── requirements.txt
├── frontend/
│   └── index.html          # single-page search UI
└── data/
    ├── limpieza_datos.ipynb  # cleaning and clustering notebook
    ├── spotify.arff          # raw dataset
    └── datos_procesados.csv  # processed dataset used by the API
```

## Getting started

```bash
git clone https://github.com/roicaride/SongRecommender.git
cd SongRecommender
pip install -r backend/requirements.txt

cd backend
python app_flask.py
```

Then open `frontend/index.html` in your browser, search for a song and get recommendations.

### API

| Method | Endpoint | Description |
| --- | --- | --- |
| `POST` | `/api/find-song` | Look up a song by name |
| `POST` | `/api/get-recommendations` | Return the 5 most similar songs |

## License

MIT — see [LICENSE](LICENSE).
