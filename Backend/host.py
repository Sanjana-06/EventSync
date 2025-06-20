import redis
import json
import os
from dotenv import load_dotenv

load_dotenv()
r = redis.Redis(host=os.getenv("REDIS_HOST"), port=int(os.getenv("REDIS_PORT")), decode_responses=True)

event_name = input("Enter the event name: ")
invitation = {
    "event": event_name
}
r.publish("invitation", json.dumps(invitation))
print("Invitation sent...")

# Wait for summary
pubsub = r.pubsub()
pubsub.subscribe("summary")

for message in pubsub.listen():
    if message['type'] == 'message':
        summary = json.loads(message['data'])
        print(f"\nFinal Guest Summary for {summary['event']}")
        for guest in summary['responses']:
            print(f"{guest['guest']}: {guest['response']}")
        break
