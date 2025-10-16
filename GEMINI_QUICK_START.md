# Gemini 2.5 Flash Image - Quick Start Guide

## 🚀 5-Minute Setup

### 1. Get API Key (2 min)
Visit: [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)
- Sign in with Google
- Click "Create API key"
- Copy the key (starts with `AIza...`)

### 2. Configure Jazz (2 min)

**Settings UI:**
```
Settings → Providers → Gemini → Paste API Key → Save
```

**Or edit config file:**
```toml
[gemini]
api_key = "YOUR_API_KEY_HERE"
```

### 3. Generate Image (1 min)

Open chat and try:
```
Generate a cozy coffee shop with warm lighting
```

Done! 🎉

---

## 📝 Example Prompts

### Simple
```
A peaceful zen garden with cherry blossoms
```

### Detailed
```
A photorealistic close-up of a steaming coffee cup on a wooden table. 
Soft morning light creates warm golden tones. Shot with 85mm lens.
```

### With Text
```
Create a vintage poster with "Blue Note Jazz" in art deco typography. 
Dark blue background with gold accents.
```

---

## 💡 Quick Tips

**✅ DO:**
- Use descriptive, narrative prompts
- Mention lighting and camera details
- Specify mood and atmosphere
- Iterate through conversation

**❌ DON'T:**
- Use keyword lists
- Expect perfection first try
- Forget to specify aspect ratio
- Skip photography terms

---

## 🎯 Aspect Ratios

- `1:1` - Square (Instagram)
- `16:9` - Landscape (YouTube)
- `9:16` - Portrait (Stories)
- `3:4` - Portrait (Posters)

Example:
```
Generate a 3:4 poster for a coffee brand
```

---

## 🔧 Troubleshooting

**Tool not showing?**
- Check API key is saved
- Restart Jazz
- Verify key at [Google AI Studio](https://aistudio.google.com/)

**Generation fails?**
- Check internet connection
- Verify API quota
- Try simpler prompt

**Poor results?**
- Use more descriptive prompts
- Add photography terms
- Specify style and mood

---

## 📚 Full Documentation

- **User Guide**: `USER_GUIDE_GEMINI_IMAGE.md`
- **Technical Details**: `GEMINI_IMAGE_INTEGRATION.md`
- **Integration Summary**: `INTEGRATION_SUMMARY.md`

---

## 🎨 Prompt Template

```
A [style] [shot type] of [subject] [doing what]. 
The scene is illuminated by [lighting], creating a [mood] atmosphere. 
Captured with a [camera/lens], emphasizing [details]. 
[Additional style notes].
```

**Example:**
```
A photorealistic close-up of an elderly ceramicist inspecting a tea bowl. 
The scene is illuminated by soft golden hour light, creating a serene atmosphere. 
Captured with an 85mm portrait lens, emphasizing the texture of the clay. 
Warm, masterful mood.
```

---

## ✨ Features

- ⚡ Fast generation
- 📝 Excellent text rendering
- 🎨 Photorealistic quality
- 💬 Conversational refinement
- 🔒 SynthID watermarking
- 🆓 Free tier available

---

**Ready to create? Get your API key and start generating!** 🚀
