from flask import Flask, request, jsonify
from flask_cors import CORS
from recommender import SongRecommender

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

# Inicializar el recomendador
recommender = SongRecommender()

@app.route('/')
def home():
    return "API de recomendación de canciones"

@app.route('/api/find-song', methods=['POST'])
def find_song():
    data = request.get_json()
    name = data.get('name', '')
    
    if not name:
        return jsonify({'error': 'Se requiere un nombre de canción'}), 400
        
    try:
        songs = recommender.find_songs(name)
        return jsonify(songs)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/get-recommendations', methods=['POST'])
def get_recommendations():
    data = request.get_json()
    song_idx = data.get('song_idx')
    
    if song_idx is None:
        return jsonify({'error': 'Se requiere un índice de canción'}), 400
        
    try:
        recommendations = recommender.get_recommendations(song_idx)
        return jsonify(recommendations)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 