# Jaaz AI Configuration Guide

## ✅ Configured API Providers

Your Jaaz application is now configured with the following AI providers and models:

### 🤖 Text Generation Models

#### 1. **Gemini (Google AI Studio)** - Best for multimodal tasks and reasoning
- **Provider**: `gemini`
- **API Key**: Configured ✅
- **Models**:
  - `gemini-2.0-flash-exp` - Latest experimental model, fastest
  - `gemini-1.5-pro` - Best for complex reasoning tasks
  - `gemini-1.5-flash` - Fast and efficient
- **Use Cases**: 
  - Complex reasoning and analysis
  - Multimodal understanding (text + images)
  - Long context tasks (up to 2M tokens)

#### 2. **Perplexity** - Best for research and online information
- **Provider**: `perplexity`
- **API Key**: Configured ✅
- **Models**:
  - `llama-3.1-sonar-large-128k-online` - Best for research, has internet access
  - `llama-3.1-sonar-small-128k-online` - Faster, still has internet access
- **Use Cases**:
  - Real-time web search and research
  - Current events and news
  - Fact-checking with citations

#### 3. **OpenRouter** - Free text models with variety
- **Provider**: `openrouter`
- **API Key**: Configured ✅
- **Free Models**:
  - `meta-llama/llama-3.3-70b-instruct:free` - Excellent general-purpose model
  - `qwen/qwen3-235b-a22b:free` - Large Chinese/English model
  - `z-ai/glm-4.5-air:free` - Fast and efficient
  - `deepseek/deepseek-chat-v3.1:free` - Great for coding and reasoning
- **Use Cases**:
  - General chat and assistance
  - Code generation and debugging
  - Creative writing
  - Cost-free experimentation

### 🎨 Image Generation

#### ✅ Replicate - ACTIVE
- **Provider**: `replicate`
- **API Key**: Configured ✅
- **Available Tools**:
  - **Imagen 4** - Google's latest image generation model
  - **Recraft v3** - High-quality design and illustration
  - **Flux Kontext Pro** - Advanced context-aware generation
  - **Flux Kontext Max** - Maximum quality Flux model
- **Use Cases**:
  - Professional image generation
  - Design and illustration
  - Context-aware image creation
  - High-quality outputs

#### ImageRouter Configuration
⚠️ **Note**: ImageRouter models are configured but not integrated as tools (requires custom development).

**Your ImageRouter Models** (for future integration):
- `stabilityai/sdxl-turbo:free`
- `black-forest-labs/FLUX-1-schnell:free`
- `HiDream-ai/HiDream-I1-Full:free`
- `lodestones/Chroma:free`

#### Other Image Generation Options:
- **ComfyUI** (local) - Recommended for advanced users
- **Jaaz Platform** (SaaS) - Requires subscription

---

## 📋 Configuration File Location

**Path**: `./server/user_data/config.toml`

This TOML file contains all provider configurations, API keys, and model definitions.

---

## 🚀 How to Use the Models

### In the Application UI:

1. **Open Jaaz** at: [https://5174--0199e4d7-fc95-7a8c-9647-8c615d5797aa.us-east-1-01.gitpod.dev](https://5174--0199e4d7-fc95-7a8c-9647-8c615d5797aa.us-east-1-01.gitpod.dev)

2. **Start a Chat**:
   - Click on the chat interface
   - Select a model from the dropdown
   - You'll see all configured models organized by provider

3. **Model Selection Strategy**:
   - **For general tasks**: Use OpenRouter free models (Llama 3.3, DeepSeek)
   - **For research/web search**: Use Perplexity models
   - **For complex reasoning**: Use Gemini 1.5 Pro
   - **For fast responses**: Use Gemini 2.0 Flash or Gemini 1.5 Flash

### Via API:

```bash
# List all available models
curl http://localhost:57988/api/list_models

# Example chat request (simplified)
curl -X POST http://localhost:57988/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [...],
    "model_info": {
      "text": [{
        "provider": "gemini",
        "model": "gemini-2.0-flash-exp",
        "url": "https://generativelanguage.googleapis.com/v1beta/",
        "type": "text"
      }]
    }
  }'
```

---

## 🔧 Model Recommendations by Task

### Best Models for Specific Tasks:

| Task | Recommended Model | Provider | Reason |
|------|------------------|----------|---------|
| **Code Generation** | `deepseek/deepseek-chat-v3.1:free` | OpenRouter | Specialized for coding |
| **Research & Facts** | `llama-3.1-sonar-large-128k-online` | Perplexity | Internet access + citations |
| **Creative Writing** | `meta-llama/llama-3.3-70b-instruct:free` | OpenRouter | Strong creative abilities |
| **Complex Reasoning** | `gemini-1.5-pro` | Gemini | Best reasoning capabilities |
| **Fast Responses** | `gemini-2.0-flash-exp` | Gemini | Fastest with good quality |
| **Multilingual** | `qwen/qwen3-235b-a22b:free` | OpenRouter | Excellent Chinese/English |
| **General Purpose** | `meta-llama/llama-3.3-70b-instruct:free` | OpenRouter | Well-balanced |

---

## 🔐 API Keys (Configured)

All API keys are securely stored in `config.toml`:

- ✅ **Gemini**: Configured (3 text models)
- ✅ **Perplexity**: Configured (2 text models)
- ✅ **OpenRouter**: Configured (4 free text models)
- ✅ **Replicate**: Configured (4 image generation tools)
- ⚠️ **ImageRouter**: Configured but not integrated (requires custom tool development)

---

## ⚙️ Optional Providers (Not Configured)

These providers are available but require API keys:

### Text Models:
- **OpenAI** - GPT-4o, GPT-4o-mini (requires API key)
- **Jaaz Platform** - Official platform models (requires API key)

### Local Options:
- **Ollama** - Run models locally (requires Ollama installation)
- **ComfyUI** - Local image generation (requires ComfyUI setup)

To add these, either:
1. Use the Settings UI in the application
2. Edit `config.toml` manually

---

## 🛠️ Troubleshooting

### Models Not Appearing?
1. Check that the server is running: `ps aux | grep "python main.py"`
2. Verify API keys in `config.toml`
3. Check server logs: `tail -f server/server.log`
4. Restart the server: 
   ```bash
   pkill -f "python main.py"
   cd server && nohup ./venv/bin/python main.py > server.log 2>&1 &
   ```

### API Errors?
1. Verify API keys are correct
2. Check rate limits on provider dashboards
3. Ensure internet connectivity
4. Check server logs for detailed error messages

### Image Generation Not Working?
- ImageRouter models are configured but not integrated as tools
- Use Jaaz platform, Replicate, or ComfyUI for image generation
- Or implement custom ImageRouter tool integration

---

## 📊 Current Status

✅ **Working**:
- **Text Generation**: 9 models across 3 providers
  - Gemini (3 models)
  - Perplexity (2 models)
  - OpenRouter (4 free models)
- **Image Generation**: 4 tools via Replicate
  - Imagen 4
  - Recraft v3
  - Flux Kontext Pro
  - Flux Kontext Max
- Model listing API
- Chat functionality
- Image generation tools

⚠️ **Limitations**:
- ImageRouter free models require custom tool integration
- Video generation requires Jaaz platform subscription or additional setup
- ComfyUI not configured (optional for local image generation)

---

## 🔄 Fallback Strategy

Since all models are free or have generous limits, here's the recommended fallback order:

**For General Tasks**:
1. `meta-llama/llama-3.3-70b-instruct:free` (OpenRouter)
2. `gemini-2.0-flash-exp` (Gemini)
3. `deepseek/deepseek-chat-v3.1:free` (OpenRouter)

**For Research**:
1. `llama-3.1-sonar-large-128k-online` (Perplexity)
2. `gemini-1.5-pro` (Gemini)

**For Speed**:
1. `gemini-2.0-flash-exp` (Gemini)
2. `z-ai/glm-4.5-air:free` (OpenRouter)

---

## 📝 Next Steps

### To Enable Image Generation:

1. **Option A: Use Jaaz Platform**
   - Get API key from [jaaz.app](https://jaaz.app)
   - Add to `config.toml` under `[jaaz]` section

2. **Option B: Use Replicate**
   - Get API key from [replicate.com](https://replicate.com)
   - Add new provider in Settings UI

3. **Option C: Install ComfyUI Locally**
   - Install ComfyUI: [github.com/comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI)
   - Start ComfyUI server on port 8188
   - Models will auto-detect

4. **Option D: Custom ImageRouter Integration**
   - Create custom tool in `server/tools/`
   - Register in `tool_service.py`
   - Use ImageRouter API key already configured

---

## 🌐 Access URLs

- **Frontend**: [https://5177--0199e4d7-fc95-7a8c-9647-8c615d5797aa.us-east-1-01.gitpod.dev](https://5177--0199e4d7-fc95-7a8c-9647-8c615d5797aa.us-east-1-01.gitpod.dev)
- **Backend API**: [https://57988--0199e4d7-fc95-7a8c-9647-8c615d5797aa.us-east-1-01.gitpod.dev](https://57988--0199e4d7-fc95-7a8c-9647-8c615d5797aa.us-east-1-01.gitpod.dev)
- **API Docs**: [https://57988--0199e4d7-fc95-7a8c-9647-8c615d5797aa.us-east-1-01.gitpod.dev/docs](https://57988--0199e4d7-fc95-7a8c-9647-8c615d5797aa.us-east-1-01.gitpod.dev/docs)

---

## 📞 Support

For issues or questions:
- Check server logs: `tail -f server/server.log`
- Check React logs: `tail -f react/react.log`
- Review API documentation at `/docs` endpoint
- Check provider status pages for outages

---

**Configuration Date**: October 14, 2025  
**Total Models Configured**: 9 text models + 4 image generation tools  
**Providers Active**: 4 (Gemini, Perplexity, OpenRouter, Replicate)
