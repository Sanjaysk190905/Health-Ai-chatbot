# 🧠 Health AI Chatbot

An AI-powered Health Assistant that helps users understand symptoms and provides simple medical guidance like possible conditions, advice, and precautions.

---

## 🚀 Features

### 🔐 Authentication System
- User Signup & Login using Firebase Authentication
- Secure user session handling
- Logout functionality

### 💬 AI Chat System
- Users can enter symptoms (e.g., fever, headache)
- AI generates:
  - Possible Condition
  - Advice
  - Precautions
- Clean structured output format

### 🧠 AI Integration
- Uses Ollama (LLaMA 3 model) for local AI processing
- Fast and offline AI responses

### 🎤 Voice Features
- Voice Input (Speech Recognition)
- Voice Output (Text-to-Speech reply)

### 🌗 Dark / Light Mode
- Toggle between Dark and Light themes
- User preference saved in local storage

### 🗂️ Chat History
- Multiple chat sessions
- Save chats using localStorage
- Load previous conversations
- Delete chats

### 🎨 Modern UI
- ChatGPT-style interface
- Sidebar navigation
- Responsive design

---

## 🛠️ Tech Stack

### Frontend
- React.js
- CSS (Custom Styling)

### Backend
- Flask (Python)
- REST API

### AI Model
- Ollama (LLaMA 3)

### Authentication
- Firebase Authentication

### Storage
- LocalStorage (Chat History)

---

## 📂 Project Structure

health-ai/
│
├── backend/
│   ├── app.py
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── Login.js
│   │   ├── firebase.js
│   │   ├── App.css
│
└── README.md

---

## ⚙️ Setup Instructions

### 🔹 Backend Setup

cd backend
pip install flask flask-cors requests
python app.py

---

### 🔹 Frontend Setup

cd frontend
npm install
npm start

---

### 🔹 Ollama Setup

ollama run llama3

---

## 🌐 API Endpoint

POST /check

### Request:
{
  "symptoms": "fever"
}

### Response:
{
  "result": "AI generated response"
}

---

## 🎯 Future Improvements

- Cloud database (Firebase / MongoDB)
- Google Login
- Mobile responsive UI
- Deployment (Render / Vercel)
- Doctor consultation integration

---

## ⚠️ Disclaimer

This project is for educational purposes only and should not be considered as a substitute for professional medical advice.

---

## 👨‍💻 Author

Sanjay Kumar  
B.Tech AI & Data Science

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
