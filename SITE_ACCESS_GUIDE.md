# Site Access Guide - Jazz Application

## 🔍 Current Status

### Backend Server
- ✅ **Running**: Python server on port `57988`
- ✅ **API Working**: `/api/list_tools` endpoint responding
- ✅ **Gemini Tool**: Registered and available

### Frontend
- ❌ **Not Built**: React dist folder doesn't exist
- ❌ **Dev Server**: Not currently running

---

## 🚀 How to Access the Application

### Option 1: Build and Serve Production (Recommended)

**Step 1: Build the React frontend**
```bash
cd react
npm install --force
npm run build
```

**Step 2: Access via backend server**
The backend will serve the built React app from `react/dist/`

**URL**: The server is running on port `57988`

### Option 2: Run Development Servers

**Terminal 1: Backend**
```bash
cd server
./venv/bin/python main.py
```

**Terminal 2: Frontend**
```bash
cd react
npm install --force
npm run dev
```

The dev server will run on port `5173` with hot reload.

---

## 🔧 Current Issue

The site links aren't working because:

1. **Frontend Not Built**: The `react/dist/` directory doesn't exist
2. **No Dev Server**: The Vite dev server isn't running
3. **Backend Only**: Only the Python API server is running

---

## ✅ Quick Fix

### Build the Frontend Now

```bash
cd react && npm install --force && npm run build
```

This will:
1. Install dependencies
2. Build the React app
3. Create `react/dist/` folder
4. Make the site accessible via the backend server

---

## 🌐 Accessing in Gitpod

### After Building

The application will be available at:
- **Backend Port**: `57988`
- **Gitpod URL**: Check the "Ports" tab in Gitpod for the public URL

### Port Forwarding

Gitpod automatically forwards ports. Look for:
- Port `57988` - Backend + Frontend (after build)
- Port `5173` - Frontend dev server (if running separately)

---

## 📊 Verification Steps

### 1. Check Backend
```bash
curl http://localhost:57988/api/list_tools
```

Expected: JSON list of tools including Gemini

### 2. Check Frontend Build
```bash
ls -la react/dist/
```

Expected: `index.html` and `assets/` folder

### 3. Check Full Site
```bash
curl http://localhost:57988/
```

Expected: HTML content (not "Internal Server Error")

---

## 🎯 Recommended Actions

### Immediate Fix
```bash
# Build the frontend
cd /workspaces/jazz/react
npm install --force
npm run build

# Verify
ls -la dist/

# Test
curl http://localhost:57988/
```

### For Development
```bash
# Terminal 1: Backend
cd /workspaces/jazz/server
./venv/bin/python main.py

# Terminal 2: Frontend (separate terminal)
cd /workspaces/jazz/react
npm run dev
```

---

## 🔍 Troubleshooting

### "Internal Server Error" on /

**Cause**: Frontend not built, `react/dist/index.html` missing

**Fix**: Build the frontend (see above)

### API Works But UI Doesn't

**Cause**: Frontend build issue

**Fix**: 
```bash
cd react
rm -rf dist node_modules
npm install --force
npm run build
```

### Port Not Accessible

**Cause**: Gitpod port forwarding

**Fix**: Check Gitpod "Ports" tab and make port public

---

## 📝 Summary

**Current State**:
- ✅ Backend API: Working
- ✅ Gemini Integration: Complete
- ❌ Frontend: Not built
- ❌ Site Access: Not available

**To Fix**:
1. Build React frontend: `cd react && npm run build`
2. Access via backend port: `57988`
3. Check Gitpod ports tab for public URL

**After Fix**:
- ✅ Full site accessible
- ✅ Settings UI available
- ✅ Can configure Gemini API key
- ✅ Can generate images

---

## 🎉 Next Steps

Once the frontend is built:

1. **Access the site** via Gitpod URL
2. **Open Settings** (⚙️ icon)
3. **Configure Gemini** API key
4. **Generate images** with the new tool!

The Gemini integration is complete and working - we just need the frontend built to access it through the UI.
