from flask import Flask, request, jsonify
import redis
import json
import os
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()
app = Flask(__name__)
CORS(app)

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)

guest_ids = ["guest1", "guest2", "guest3"]
responses = []

@app.route("/send-invitation", methods=["POST"])
def send_invitation():
    print("Inside /send-invitation")
    data = request.get_json()
    print("Received JSON:", data)

    event_name = data.get("event")
    if not event_name:
        print("Missing event name!")
        return jsonify({"error": "Event name required"}), 400

    invitation = {"event": event_name}
    r.publish("invitation", json.dumps(invitation))
    print("Published invitation:", invitation)

    return jsonify({"message": "Invitation sent", "event": event_name})

@app.route("/simulate-responses", methods=["POST"])
def simulate_responses():
    responses.clear()
    pubsub = r.pubsub()
    pubsub.subscribe("guest_responses")

    count = 0
    while count < len(guest_ids):
        msg = pubsub.get_message(timeout=5)
        if msg and msg['type'] == 'message':
            res = json.loads(msg['data'])
            responses.append(res)
            count += 1

    return jsonify({"responses": responses})


@app.route("/get-summary", methods=["GET"])
def get_summary():
    if not responses:
        return jsonify({"error": "No responses collected yet"}), 404

    return jsonify({"summary": responses})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)