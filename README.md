# 📅 EventSync

**EventSync** is a simple Pub/Sub-based event planning system that allows a host to send event invitations to guests and receive simulated responses in real time. The system includes a Flask backend with Redis and a mobile frontend built using React Native (Expo).

---

## 🧠 Key Features

- 📨 Send event invitations from a mobile app
- 🔁 Redis Pub/Sub used for real-time message publishing
- 🤖 Simulated guest responses using Redis
- 📋 View a summary of all responses
- 🔧 Cross-origin enabled (CORS) for frontend-backend interaction

---

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Node.js & npm
- Redis
- Expo Go app (on your phone)

---

## 🧠 Design Decisions
- Redis Pub/Sub was chosen for its simplicity and speed in message broadcasting.
- React Native enables easy mobile interface development and cross-platform support.
- The project is modular and can be extended to add real guest response handling.

