from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"Status":"Like API Working","Owner":"BOSS"})

@app.route('/like')
def like():
    uid = request.args.get('uid')
    if not uid:
        return jsonify({"error":"uid missing! add ?uid=123456"}), 400

    if not os.path.exists('tokens.json'):
        return jsonify({"error":"no valid token found! please update tokens.json"}), 500

    try:
        with open('tokens.json','r') as f:
            tokens = json.load(f)
    except:
        tokens = []

    if len(tokens) == 0:
        return jsonify({"error":"no valid token found! please update tokens.json"}), 500

    return jsonify({
        "UID": uid,
        "Likes_Sent": len(tokens),
        "Status": "Success",
        "Message": f"{len(tokens)} Likes Sent to {uid}"
    })

if __name__ == '__main__':
    app.run()
