from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your actual API key and endpoint
INSTAGRAM_API_KEY = 'X-RapidAPI-Key
3f5f3e8930msh682c2ae4decd574p1738dbjsn9fbef46524a7
'
INSTAGRAM_API_ENDPOINT = 'https://api.example.com/instagram/download'

@app.route('/download', methods=['POST'])
def download_video():
    data = request.json
    url = data.get('url')
    
    try:
        # Connect to Instagram API
        response = requests.post(
            INSTAGRAM_API_ENDPOINT,
            headers={'Authorization': f'Bearer {INSTAGRAM_API_KEY}'},
            json={'url': url}
        )
        
        response_data = response.json()
        
        if not response.ok:
            return jsonify({'error': response_data.get('message', 'Download failed')}), 400
            
        return jsonify({
            'videoUrl': response_data['video_url'],
            'thumbnail': response_data['thumbnail']
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
