# User Guide: Gemini 2.5 Flash Image (Nano Banana)

## 🎨 What is Gemini 2.5 Flash Image?

Gemini 2.5 Flash Image (nicknamed "Nano Banana") is Google's latest AI image generation model that excels at:

- **Photorealistic Images**: Creates highly realistic photos with proper lighting and detail
- **Text in Images**: Generates legible text in images (perfect for logos, posters, signs)
- **Image Editing**: Modify existing images with text prompts
- **Conversational Creation**: Refine images through multiple turns of conversation

All generated images include a SynthID watermark for authenticity verification.

---

## 📋 Prerequisites

Before you can use Gemini for image generation, you need:

1. **A Google AI Studio API Key** (free to get)
2. **Jazz app** installed and running

---

## 🔑 Step 1: Get Your Gemini API Key

### Option A: If You Already Have a Google Account

1. Go to [Google AI Studio](https://aistudio.google.com/apikey)
2. Click **"Get API key"** or **"Create API key"**
3. Select or create a Google Cloud project
4. Copy your API key (starts with `AIza...`)

### Option B: Create a New Account

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account (or create one)
3. Navigate to **API Keys** section
4. Click **"Create API key"**
5. Copy your API key

**Important**: Keep your API key secure! Don't share it publicly.

---

## ⚙️ Step 2: Configure Jazz to Use Gemini

### Method 1: Using the Settings UI (Recommended)

1. **Open Jazz** application
2. Click the **Settings** icon (⚙️) in the top-right corner
3. In the Settings dialog, select **"Providers"** from the sidebar
4. Scroll down to find **"Gemini"** section
5. Paste your API key in the **"API Key"** field
6. The URL should already be set to: `https://generativelanguage.googleapis.com/v1beta/`
7. Click **"Save Settings"** at the bottom

### Method 2: Manual Configuration (Advanced)

1. Navigate to your Jazz installation folder
2. Open `server/user_data/config.toml` in a text editor
3. Find or add the `[gemini]` section:

```toml
[gemini]
url = "https://generativelanguage.googleapis.com/v1beta/"
api_key = "YOUR_API_KEY_HERE"
max_tokens = 8192
is_custom = true

[gemini.models."gemini-2.5-flash-image"]
type = "image"
is_custom = true
```

4. Replace `YOUR_API_KEY_HERE` with your actual API key
5. Save the file
6. Restart the Jazz server

---

## ✅ Step 3: Verify the Tool is Available

After configuring your API key:

1. **Restart Jazz** (if you edited the config file manually)
2. Open or create a **new chat**
3. The AI should now have access to the Gemini image generation tool
4. You can verify by checking the Settings → Providers section

The tool will appear as: **"Gemini 2.5 Flash Image (Nano Banana)"**

---

## 🎨 Step 4: Generate Your First Image

### Basic Text-to-Image

Simply ask the AI to create an image:

**Example Prompts:**

```
Generate an image of a cozy coffee shop on a rainy day
```

```
Create a photorealistic portrait of a wise old wizard with a long white beard
```

```
Make me a poster for a music festival with the text "Summer Vibes 2025"
```

### Tips for Better Results

#### ✅ DO: Use Descriptive, Narrative Prompts

**Good Example:**
```
A photorealistic close-up of a steaming cup of coffee on a wooden table. 
The scene is illuminated by soft morning light streaming through a window, 
creating warm golden tones. The coffee has beautiful latte art in the shape 
of a heart. Shot with an 85mm lens with a blurred background.
```

#### ❌ DON'T: Use Keyword Lists

**Bad Example:**
```
coffee, table, wood, morning, light, latte art, heart
```

---

## 🎯 Advanced Usage

### 1. Photorealistic Images

For realistic photos, use photography terminology:

```
A photorealistic wide-angle shot of a modern minimalist living room. 
The space features floor-to-ceiling windows with natural daylight, 
a grey sectional sofa, and indoor plants. Captured with a 24mm lens, 
emphasizing the spaciousness. Architectural photography style.
```

**Key Elements:**
- Shot type: close-up, wide-angle, bird's eye view
- Lighting: golden hour, soft diffused, dramatic shadows
- Camera details: 85mm lens, bokeh background, shallow depth of field
- Mood: serene, dramatic, cheerful, moody

### 2. Text in Images

Gemini excels at generating legible text:

```
Create a vintage-style poster for a jazz club. The poster should have 
"Blue Note Jazz Club" in elegant art deco typography at the top, 
"Every Friday Night" in smaller text below, and "Live Music & Cocktails" 
at the bottom. Dark blue background with gold accents.
```

### 3. Image Editing

You can modify existing images (if supported by your setup):

```
[Upload an image of a room]
Change the wall color to sage green and add some framed artwork
```

### 4. Iterative Refinement

Have a conversation to perfect your image:

**Turn 1:**
```
Create a logo for a tech startup called "CloudSync"
```

**Turn 2:**
```
Make the colors more vibrant and add a cloud icon
```

**Turn 3:**
```
Perfect! Now make it work on a dark background
```

---

## 📐 Aspect Ratios

You can specify aspect ratios for your images:

- **1:1** - Square (Instagram posts, profile pictures)
- **16:9** - Landscape (YouTube thumbnails, presentations)
- **9:16** - Portrait (Instagram stories, mobile wallpapers)
- **4:3** - Standard landscape
- **3:4** - Standard portrait (posters, book covers)

**Example:**
```
Generate a 3:4 portrait poster for a coffee brand with the text "Morning Brew"
```

**Note**: Gemini may not strictly enforce aspect ratios, but it will try to match your request.

---

## 🎨 Prompt Templates

### Template 1: Product Photography
```
A photorealistic product shot of [product] on a [surface]. 
The scene is illuminated by [lighting type], creating a [mood] atmosphere. 
Captured with a [lens type], emphasizing [key features]. 
The background is [background description].
```

### Template 2: Character Portrait
```
A [art style] portrait of [character description] with [distinctive features]. 
They are [action/expression], set in [environment]. 
The lighting is [lighting description], creating a [mood] atmosphere. 
[Additional style notes].
```

### Template 3: Scene/Landscape
```
A [shot type] of [location/scene] during [time of day]. 
The scene features [key elements]. The atmosphere is [mood/weather]. 
Captured with a [camera/lens], emphasizing [focal points]. 
[Color palette or style notes].
```

---

## 🔧 Troubleshooting

### Tool Not Appearing

**Problem**: Gemini tool doesn't show up in the chat

**Solutions**:
1. Verify your API key is correctly entered in Settings
2. Make sure you clicked "Save Settings"
3. Restart the Jazz application
4. Check that the API key is valid (not expired or revoked)

### API Key Errors

**Problem**: "Gemini API key is not configured" error

**Solutions**:
1. Go to Settings → Providers → Gemini
2. Paste your API key
3. Click "Save Settings"
4. Restart Jazz

### Generation Fails

**Problem**: Image generation fails or returns an error

**Solutions**:
1. Check your API key has image generation enabled
2. Verify you haven't exceeded your API quota
3. Try a simpler prompt first
4. Check your internet connection
5. Review the prompt for any policy violations

### Poor Quality Results

**Problem**: Generated images don't match expectations

**Solutions**:
1. Use more descriptive, narrative prompts (not keyword lists)
2. Include photography terms (lighting, camera, mood)
3. Specify the style you want (photorealistic, artistic, etc.)
4. Try iterative refinement through conversation
5. Be specific about colors, composition, and details

---

## 💡 Best Practices

### 1. Start with Clear Descriptions
Instead of: "a cat"
Try: "A fluffy orange tabby cat sitting on a windowsill, looking out at a rainy street. Soft natural light from the window illuminates its fur."

### 2. Use Photography Language
- Mention lighting: "golden hour light", "soft diffused lighting"
- Specify camera: "85mm portrait lens", "wide-angle shot"
- Describe mood: "serene atmosphere", "dramatic and moody"

### 3. Iterate and Refine
Don't expect perfection on the first try. Have a conversation:
- Generate initial image
- Ask for specific changes
- Refine until satisfied

### 4. Leverage Text Generation
Gemini is excellent at text in images:
- Logos with company names
- Posters with event details
- Signs and labels
- Diagrams with annotations

### 5. Specify Composition
- "Centered composition"
- "Rule of thirds"
- "Subject in foreground, blurred background"
- "Bird's eye view"

---

## 📊 Comparison with Other Tools

| Feature | Gemini 2.5 Flash | Imagen 4 | Midjourney |
|---------|------------------|----------|------------|
| Text in Images | ⭐⭐⭐⭐⭐ Excellent | ⭐⭐⭐⭐ Good | ⭐⭐⭐ Fair |
| Photorealism | ⭐⭐⭐⭐⭐ Excellent | ⭐⭐⭐⭐⭐ Excellent | ⭐⭐⭐⭐ Good |
| Artistic Style | ⭐⭐⭐⭐ Good | ⭐⭐⭐⭐ Good | ⭐⭐⭐⭐⭐ Excellent |
| Speed | ⭐⭐⭐⭐⭐ Fast | ⭐⭐⭐⭐ Good | ⭐⭐⭐ Moderate |
| Conversational | ⭐⭐⭐⭐⭐ Excellent | ⭐⭐⭐ Fair | ⭐⭐ Limited |
| Cost | Free tier available | Pay per use | Subscription |

---

## 🎓 Example Workflows

### Workflow 1: Creating a Logo

**Step 1**: Initial generation
```
Create a modern logo for a tech company called "DataFlow". 
The logo should incorporate flowing lines suggesting data movement, 
use blue and purple colors, and work well on both light and dark backgrounds.
```

**Step 2**: Refine colors
```
Make the blue more vibrant, like a bright cyan
```

**Step 3**: Adjust composition
```
Make the text larger and the icon smaller
```

**Step 4**: Final touches
```
Perfect! Now show me how it looks on a dark background
```

### Workflow 2: Product Photography

**Step 1**: Basic shot
```
A photorealistic product shot of a sleek wireless headphone on a white surface. 
Soft studio lighting from the top-left, creating subtle shadows. 
Captured with a 100mm macro lens, emphasizing the premium materials and craftsmanship.
```

**Step 2**: Add context
```
Now show the same headphones on a wooden desk with a laptop in the blurred background
```

**Step 3**: Lifestyle shot
```
Show someone wearing these headphones in a modern coffee shop, natural lighting
```

### Workflow 3: Social Media Content

**Step 1**: Create main image
```
Create a 1:1 Instagram post for a fitness brand. Show a person doing yoga 
at sunrise on a beach. Include the text "Find Your Balance" in elegant 
typography at the top. Warm, inspiring colors.
```

**Step 2**: Story version
```
Now create a 9:16 version for Instagram stories with the same theme
```

**Step 3**: Variation
```
Create another version with a different yoga pose and "Morning Mindfulness" text
```

---

## 🔒 Privacy & Security

- **API Key Security**: Your API key is stored locally in your config file
- **Data Privacy**: Prompts and images are sent to Google's servers for processing
- **Watermarking**: All images include SynthID watermarks for authenticity
- **Local Storage**: Generated images are saved locally in your Jazz files directory

---

## 💰 Pricing & Limits

Gemini API pricing (as of 2025):
- **Free Tier**: Available with rate limits
- **Pay-as-you-go**: Charged per image generated
- **Rate Limits**: Check [Google AI Studio](https://aistudio.google.com/) for current limits

**Tip**: Start with the free tier to test and experiment before upgrading.

---

## 📚 Additional Resources

- **Official Documentation**: https://ai.google.dev/gemini-api/docs/image-generation
- **Google AI Studio**: https://aistudio.google.com/
- **Model Page**: https://aistudio.google.com/models/gemini-2-5-flash-image
- **Jazz Documentation**: See `GEMINI_IMAGE_INTEGRATION.md` for technical details

---

## 🆘 Getting Help

If you encounter issues:

1. **Check the logs**: Look for error messages in the Jazz console
2. **Verify configuration**: Settings → Providers → Gemini
3. **Test API key**: Try generating a simple image
4. **Community support**: Join the Jazz Discord or GitHub discussions
5. **Technical docs**: See `GEMINI_IMAGE_INTEGRATION.md` for troubleshooting

---

## 🎉 You're Ready!

You now have everything you need to create amazing images with Gemini 2.5 Flash Image. Start with simple prompts and experiment with different styles and techniques. Happy creating! 🎨✨
