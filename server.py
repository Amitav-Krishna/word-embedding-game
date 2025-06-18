from flask import Flask, jsonify, send_from_directory
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/embeddings.json')
def serve_embeddings():
    return send_from_directory('.', 'embeddings.json')

@app.route('/rerun-embeddings', methods=['POST'])
def rerun_embeddings():
    try:
        # Run the embeddings.py script
        result = subprocess.run(['python', 'embeddings.py'], capture_output=True, text=True)
        
        if result.returncode == 0:
            return jsonify({"status": "success", "message": result.stdout})
        else:
            return jsonify({"status": "error", "message": result.stderr}), 500
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)