# Jaaz - Self-Hosted Setup Guide

## 🎯 Overview

This is a **self-hosted, open-source** version of Jaaz - an AI-powered canvas creative agent. This installation is completely independent from the commercial jaaz.app platform.

---

## ✅ Current Status

**Status**: 🟢 Fully Operational  
**Environment**: Gitpod Workspace  
**Authentication**: Challenge-based (simple question)  
**Access URL**: [https://5175--0199e4d7-fc95-7a8c-9647-8c615d5797aa.us-east-1-01.gitpod.dev](https://5175--0199e4d7-fc95-7a8c-9647-8c615d5797aa.us-east-1-01.gitpod.dev)

---

## 🔐 Authentication

### **Challenge Question**
When you first open the app, you'll see:

```
"Jaaz is short for..."
```

**Answer**: `jasper` (case-insensitive)

This provides basic privacy protection for your self-hosted instance.

---

## 🤖 Configured AI Models

### **Text Generation (9 Models)**

| Provider | Models | Status |
|----------|--------|--------|
| **Gemini** | gemini-2.0-flash-exp, 1.5-pro, 1.5-flash | ✅ Active |
| **Perplexity** | sonar-large, sonar-small (with internet!) | ✅ Active |
| **OpenRouter** | Llama 3.3 70B, Qwen3 235B, GLM-4.5, DeepSeek v3.1 | ✅ Active |

### **Image Generation (4 Tools)**

| Provider | Tools | Status |
|----------|-------|--------|
| **Replicate** | Imagen 4, Recraft v3, Flux Kontext Pro/Max | ✅ Active |

**All models work without any subscription or additional authentication!**

---

## 🚀 Quick Start

### **1. Access the Application**
Open: [https://5175--0199e4d7-fc95-7a8c-9647-8c615d5797aa.us-east-1-01.gitpod.dev](https://5175--0199e4d7-fc95-7a8c-9647-8c615d5797aa.us-east-1-01.gitpod.dev)

### **2. Authenticate**
Enter `jasper` when prompted

### **3. Start Creating**
- **Chat**: Select a model and start chatting
- **Generate Images**: Ask AI to create images
- **Magic Canvas**: Sketch and let AI generate

---

## 📊 System Architecture

```
┌─────────────────────────────────────────────┐
│  Self-Hosted Jaaz (Open Source)            │
│  ┌──────────────┐      ┌─────────────────┐ │
│  │   Frontend   │◄────►│   Backend API   │ │
│  │  (React/UI)  │      │  (FastAPI/Py)   │ │
│  │  Port: 5175  │      │  Port: 57988    │ │
│  └──────────────┘      └─────────────────┘ │
│         │                      │            │
│         │                      ▼            │
│         │            ┌──────────────────┐  │
│         │            │  Configuration   │  │
│         │            │  - API Keys      │  │
│         │            │  - Models        │  │
│         │            └──────────────────┘  │
│         │                                   │
│         ▼                                   │
│  ┌─────────────────────────────────────┐  │
│  │  External AI Providers              │  │
│  │  - Gemini (Google AI Studio)       │  │
│  │  - Perplexity                       │  │
│  │  - OpenRouter                       │  │
│  │  - Replicate                        │  │
│  └─────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

---

## 🔧 Configuration

### **API Keys Location**
`./server/user_data/config.toml`

### **Configured Providers**
- ✅ Gemini (Google AI Studio)
- ✅ Perplexity
- ✅ OpenRouter (free models)
- ✅ Replicate

### **Settings**
`./server/user_data/settings.json`

---

## 🎨 Features

### **Available Now**
- ✅ Text generation with 9 models
- ✅ Image generation with 4 professional tools
- ✅ Magic Canvas (sketch-to-image)
- ✅ Infinite canvas workspace
- ✅ Real-time collaboration (WebSocket)
- ✅ File management
- ✅ Multi-language support

### **Not Included (SaaS Only)**
- ❌ Jaaz platform subscription features
- ❌ Video generation (requires additional setup)
- ❌ Billing/credits system

---

## 🔄 Service Management

### **Check Status**
```bash
ps aux | grep -E "(python main|npm run dev)" | grep -v grep
```

### **Restart Services**
```bash
# Stop all
pkill -f "python main.py"
pkill -f "npm run dev"

# Start backend
cd server && nohup ./venv/bin/python main.py > server.log 2>&1 &

# Start frontend
cd react && nohup npm run dev > react.log 2>&1 &
```

### **View Logs**
```bash
# Backend
tail -f server/server.log

# Frontend
tail -f react/react.log
```

---

## 📝 Important Notes

### **This is NOT jaaz.app**
- This is the **open-source version**
- Completely independent from the commercial platform
- No subscription required
- No connection to jaaz.app servers (except for optional features)

### **Authentication**
- Simple challenge-based authentication
- Session-based (cleared when browser closes)
- Perfect for personal/private use
- **Not suitable for public production deployment**

### **API Keys**
- Your API keys are stored locally
- Never sent to jaaz.app
- Used directly with AI providers (Gemini, Perplexity, etc.)

---

## 🆘 Troubleshooting

### **Can't Access the App**
1. Check if services are running: `ps aux | grep -E "(python|npm)"`
2. Check logs: `tail -f server/server.log` and `tail -f react/react.log`
3. Verify ports: `gitpod environment port list`

### **Challenge Dialog Not Appearing**
1. Clear browser cache and sessionStorage
2. Open in incognito/private window
3. Check browser console for errors (F12)

### **Models Not Working**
1. Verify API keys in `server/user_data/config.toml`
2. Check backend logs for API errors
3. Test API endpoints: `curl http://localhost:57988/api/list_models`

---

## 📚 Documentation Files

| File | Purpose |
|------|---------|
| `README_SELFHOSTED.md` | This file - Self-hosted setup guide |
| `AUTHENTICATION_COMPLETE.md` | Authentication implementation summary |
| `CHALLENGE_AUTH_SETUP.md` | Detailed auth technical docs |
| `AUTHENTICATION_REVIEW.md` | Original auth system analysis |
| `SERVICE_STATUS.md` | Current service status |
| `API_CONFIGURATION.md` | API keys and model configuration |
| `SETUP_SUMMARY.md` | Complete setup documentation |

---

## 🎯 Recommended Model Usage

### **For Speed**
- Gemini 2.0 Flash Exp
- GLM-4.5 Air (OpenRouter)

### **For Quality**
- Gemini 1.5 Pro
- Llama 3.3 70B (OpenRouter)

### **For Research**
- Perplexity Sonar Large (has internet access!)

### **For Coding**
- DeepSeek Chat v3.1 (OpenRouter)

### **For Images**
- Imagen 4 (photorealistic)
- Recraft v3 (design/illustration)
- Flux Kontext Max (highest quality)

---

## 🔐 Security Recommendations

### **Current Setup (Private Use)**
- ✅ Challenge authentication
- ✅ Gitpod workspace (hard to guess URL)
- ✅ Session-based access
- ✅ Perfect for personal use

### **For Public Deployment**
Consider adding:
- HTTP Basic Auth
- Rate limiting
- IP whitelisting
- Proper user management system
- HTTPS with valid certificate

---

## 🎉 You're All Set!

Your self-hosted Jaaz installation is:
- ✅ Fully configured
- ✅ All models working
- ✅ Authentication enabled
- ✅ Ready to use

**Start creating**: [https://5175--0199e4d7-fc95-7a8c-9647-8c615d5797aa.us-east-1-01.gitpod.dev](https://5175--0199e4d7-fc95-7a8c-9647-8c615d5797aa.us-east-1-01.gitpod.dev)

**Challenge Answer**: `jasper`

---

**Setup Date**: October 16, 2025  
**Status**: 🟢 Production Ready (Private Use)  
**Version**: Self-Hosted Open Source
