import redis
import json
import random
import os
from dotenv import load_dotenv

load_dotenv()
r = redis.Redis(host=os.getenv("REDIS_HOST"), port=int(os.getenv("REDIS_PORT")), decode_responses=True)

guest_name = input("Enter guest name (guest1/guest2/guest3): ")
pubsub = r.pubsub()
pubsub.subscribe(guest_name)

options = ["Yes", "No", "Maybe"]
print(f"{guest_name} listening...")

for message in pubsub.listen():
    if message['type'] == 'message':
        invitation = json.loads(message['data'])
        print(f"{guest_name} received invitation to {invitation['event']}")
        response = {
            "guest": guest_name,
            "response": random.choice(options)
        }
        r.publish("guest_responses", json.dumps(response))
        break
