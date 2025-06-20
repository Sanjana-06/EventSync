import redis
import json
import os
from dotenv import load_dotenv

load_dotenv()
r = redis.Redis(host=os.getenv("REDIS_HOST"), port=int(os.getenv("REDIS_PORT")), decode_responses=True)

pubsub = r.pubsub()
pubsub.subscribe("invitation")

responses = []
guest_ids = ["guest1", "guest2", "guest3"]

print("Coordinator started and listening for invitations...")

for message in pubsub.listen():
    if message['type'] == 'message':
        data = json.loads(message['data'])
        print(f"Coordinator received invitation: {data}")

        # Forward to guests
        for guest in guest_ids:
            r.publish(guest, json.dumps(data))

        # Wait for responses
        guest_pubsub = r.pubsub()
        guest_pubsub.subscribe("guest_responses")

        while len(responses) < len(guest_ids):
            response = guest_pubsub.get_message(timeout=10)
            if response and response['type'] == 'message':
                guest_response = json.loads(response['data'])
                print(f"Received response: {guest_response}")
                responses.append(guest_response)

        # Send summary
        summary = {
            "event": data["event"],
            "responses": responses
        }
        r.publish("summary", json.dumps(summary))
        break
