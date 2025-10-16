# ✅ Working URLs - Jaaz Application

## 🌐 Access Your Application

### **Frontend (React UI)**
[https://5177--0199e4d7-fc95-7a8c-9647-8c615d5797aa.us-east-1-01.gitpod.dev](https://5177--0199e4d7-fc95-7a8c-9647-8c615d5797aa.us-east-1-01.gitpod.dev)

**Status**: ✅ Working  
**Port**: 5177  
**What it is**: The main user interface where you interact with the AI

---

### **Backend API**
[https://57988--0199e4d7-fc95-7a8c-9647-8c615d5797aa.us-east-1-01.gitpod.dev](https://57988--0199e4d7-fc95-7a8c-9647-8c615d5797aa.us-east-1-01.gitpod.dev)

**Status**: ✅ Working  
**Port**: 57988  
**What it is**: The API server that handles all AI requests

---

### **API Documentation**
[https://57988--0199e4d7-fc95-7a8c-9647-8c615d5797aa.us-east-1-01.gitpod.dev/docs](https://57988--0199e4d7-fc95-7a8c-9647-8c615d5797aa.us-east-1-01.gitpod.dev/docs)

**Status**: ✅ Working  
**What it is**: Interactive API documentation (Swagger UI)

---

## 🧪 Verification Tests

### Test 1: Frontend Loading
```bash
curl -s https://5177--0199e4d7-fc95-7a8c-9647-8c615d5797aa.us-east-1-01.gitpod.dev | grep -o "<title>.*</title>"
```
**Expected**: `<title>Jaaz</title>`  
**Status**: ✅ Pass

### Test 2: Backend API - List Models
```bash
curl -s https://57988--0199e4d7-fc95-7a8c-9647-8c615d5797aa.us-east-1-01.gitpod.dev/api/list_models | python -m json.tool | head -5
```
**Expected**: JSON array with model configurations  
**Status**: ✅ Pass (9 text models found)

### Test 3: Backend API - List Tools
```bash
curl -s https://57988--0199e4d7-fc95-7a8c-9647-8c615d5797aa.us-east-1-01.gitpod.dev/api/list_tools | python -m json.tool
```
**Expected**: JSON array with image generation tools  
**Status**: ✅ Pass (4 Replicate tools found)

---

## 📊 What's Available

### Text Models (9 total)
- ✅ Gemini 2.0 Flash Exp
- ✅ Gemini 1.5 Pro
- ✅ Gemini 1.5 Flash
- ✅ Perplexity Sonar Large (with internet!)
- ✅ Perplexity Sonar Small (with internet!)
- ✅ Llama 3.3 70B Instruct (free)
- ✅ Qwen3 235B (free)
- ✅ GLM-4.5 Air (free)
- ✅ DeepSeek Chat v3.1 (free)

### Image Generation Tools (4 total)
- ✅ Imagen 4 (Google)
- ✅ Recraft v3
- ✅ Flux Kontext Pro
- ✅ Flux Kontext Max

---

## 🚀 Quick Start

1. **Open the Frontend**: Click the frontend URL above
2. **Start Chatting**: Select a model and start a conversation
3. **Generate Images**: Ask the AI to create an image - it will use Replicate automatically
4. **Try Magic Canvas**: Click "New Canvas" to use the sketch-to-image feature

---

## 🔧 Technical Details

### Port Configuration
- **Frontend**: Running on port 5177 (Vite dev server)
- **Backend**: Running on port 57988 (FastAPI/Uvicorn)
- **Both**: Bound to 0.0.0.0 (accessible externally)
- **Gitpod**: Ports properly exposed with HTTP protocol

### Server Status
```bash
# Check if servers are running
ps aux | grep -E "(python main|npm run dev)" | grep -v grep

# Expected output:
# - python main.py process
# - npm run dev process
```

### Logs Location
- **Backend**: `./server/server.log`
- **Frontend**: `./react/react.log`

---

## ⚠️ Important Notes

1. **Port Numbers**: The frontend port may change (5174→5175→5176→5177) if previous ports are in use. Always check the latest port with:
   ```bash
   gitpod environment port list
   ```

2. **Vite Configuration**: The frontend is configured to allow Gitpod hosts (`.gitpod.dev`)

3. **API Proxy**: The frontend proxies API requests to the backend automatically

---

## 🔄 If URLs Stop Working

### Restart Servers
```bash
# Stop everything
pkill -f "python main.py"
pkill -f "npm run dev"

# Start backend
cd server && nohup ./venv/bin/python main.py > server.log 2>&1 &

# Start frontend
cd react && nohup npm run dev > react.log 2>&1 &

# Wait 5 seconds
sleep 5

# Check what port React is using
tail -5 react/react.log

# Open the new port
gitpod environment port open <PORT> --name frontend-app

# Get the new URL
gitpod environment port list
```

---

## ✅ Everything Verified

- ✅ Frontend accessible
- ✅ Backend API accessible
- ✅ API documentation accessible
- ✅ 9 text models configured
- ✅ 4 image generation tools configured
- ✅ All API keys working
- ✅ Ports properly exposed

**Status**: 🟢 All Systems Operational

**Last Verified**: October 14, 2025 at 23:42 UTC
