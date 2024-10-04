from flask import Flask, request, jsonify
from flask_cors import CORS

from analyzer import analyze_file

app = Flask(__name__)
CORS(app)  # Autorise les requêtes cross-origin

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Aucun fichier trouvé'}), 400

    file = request.files['file']
    
    analysis_result = analyze_file(file)

    # Pour cet exemple, nous allons simplement retourner un message de réussite
    return jsonify(analysis_result), 200

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

