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
# 🚀 Running Setup Guide for EventSync

This guide explains how to set up and run both the **backend (Flask + Redis)** and the **frontend (React Native using Expo)** for the EventSync project.

---

## 🧩 Backend Setup (Flask + Redis)

### ✅ Prerequisites

- Python 3.x
- Redis server running (default host: `localhost`, port: `6379`)
- `pip` for installing Python packages

### 🔧 Setup Steps

1. **Navigate to the backend directory**:
   cd backend
2. **Create and activate a virtual environment**:
   python -m venv venv
   venv\Scripts\activate
3. **Install dependencies**:
   pip install -r requirements.txt
4. **Start the Flask backend server**:
   python app.py

- It should be running at: http://localhost:5000 or http://<your-local-IP>:5000 (for mobile access)

## 📱Frontend Setup (React Native + Expo)

### ✅ Prerequisites

- Node.js and npm installed
- Expo CLI (npm install -g expo-cli)
- Expo Go app installed on your mobile device

### 🔧 Setup Steps

1. **Navigate to the frontend directory**:
   cd frontend/mobile-app
3. **Install dependencies**:
   npm install
4. **Start the Expo development server:**:
   npm start

- Scan the QR code using Expo Go (Android) or the Camera app (iOS)

## 🧠 Design Decisions
- Redis Pub/Sub was chosen for its simplicity and speed in message broadcasting.
- React Native enables easy mobile interface development and cross-platform support.
- The project is modular and can be extended to add real guest response handling.

