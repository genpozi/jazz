# Gemini 2.5 Flash Image Integration (Nano Banana)

## Overview

This integration adds support for Google's **Gemini 2.5 Flash Image** model (nicknamed "Nano Banana") to the Jazz image generation system. This model excels at:

- **Text-to-Image Generation**: Create high-quality images from descriptive prompts
- **Photorealistic Rendering**: Excellent at realistic scenes with proper lighting and detail
- **Text Rendering**: Accurately generates legible text in images (logos, posters, diagrams)
- **Image Editing**: Modify existing images with text prompts
- **Conversational Refinement**: Iteratively improve images through multi-turn conversations

All generated images include a SynthID watermark for authenticity verification.

## Configuration

### API Key Setup

The integration uses the **Google AI Studio API** (not Vertex AI). You need a Gemini API key:

1. Get your API key from [Google AI Studio](https://aistudio.google.com/apikey)
2. Add it to `server/user_data/config.toml`:

```toml
[gemini]
url = "https://generativelanguage.googleapis.com/v1beta/"
api_key = "YOUR_GEMINI_API_KEY_HERE"
max_tokens = 8192
is_custom = true

[gemini.models."gemini-2.5-flash-image"]
type = "image"
is_custom = true
```

### Fallback Provider

If users don't have a Gemini API key, the system can fall back to:
- **Replicate**: Already integrated with Imagen 4 support
- **Jaaz**: Alternative provider for various image models

## Usage

### Tool Name
`generate_image_by_gemini_flash_image`

### Display Name
"Gemini 2.5 Flash Image (Nano Banana)"

### Parameters

- **prompt** (required): Descriptive text prompt for image generation
  - Best practice: Use narrative descriptions rather than keyword lists
  - Example: "A photorealistic close-up of a nano banana dish in a fancy restaurant with Gemini constellation theme"
  
- **aspect_ratio** (required): Image aspect ratio
  - Supported values: `1:1`, `16:9`, `4:3`, `3:4`, `9:16`
  - Note: Gemini may not strictly enforce aspect ratios
  - Best for posters: `3:4`

### Example Prompts

#### Text-to-Image
```
A photorealistic close-up portrait of an elderly Japanese ceramicist with 
deep, sun-etched wrinkles and a warm, knowing smile. He is carefully 
inspecting a freshly glazed tea bowl. The setting is his rustic, 
sun-drenched workshop. The scene is illuminated by soft, golden hour light 
streaming through a window, highlighting the fine texture of the clay.
```

#### Image Editing
```
[Upload image of a cat]
Create a picture of my cat eating a nano-banana in a fancy restaurant 
under the Gemini constellation
```

## Implementation Details

### Files Created

1. **`server/tools/image_providers/gemini_provider.py`**
   - Provider class implementing `ImageProviderBase`
   - Handles API communication with Google AI Studio
   - Processes base64 image responses

2. **`server/tools/generate_image_by_gemini_flash_image.py`**
   - LangChain tool wrapper
   - Input schema validation
   - Integration with image generation core

### Files Modified

1. **`server/tools/utils/image_generation_core.py`**
   - Added `GeminiImageProvider` import
   - Registered provider in `IMAGE_PROVIDERS` dict

2. **`server/services/tool_service.py`**
   - Added tool import
   - Registered in `TOOL_MAPPING` with display name

3. **`server/user_data/config.toml`**
   - Added model configuration for `gemini-2.5-flash-image`

## API Details

### Endpoint
```
POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:generateContent
```

### Authentication
```
x-goog-api-key: YOUR_API_KEY
```

### Request Format
```json
{
  "contents": [{
    "parts": [
      {"text": "Your prompt here"},
      {
        "inline_data": {
          "mime_type": "image/png",
          "data": "base64_encoded_image_data"
        }
      }
    ]
  }]
}
```

### Response Format
```json
{
  "candidates": [{
    "content": {
      "parts": [
        {
          "inline_data": {
            "mime_type": "image/png",
            "data": "base64_encoded_generated_image"
          }
        }
      ]
    }
  }]
}
```

## Prompting Best Practices

### 1. Describe Scenes, Not Keywords
❌ Bad: "cat, restaurant, banana, fancy"
✅ Good: "A fluffy orange cat sitting at a white tablecloth table in an upscale French restaurant, delicately eating a small banana from a porcelain plate"

### 2. Use Photography Terms for Realism
- Mention camera angles: "close-up", "wide-angle", "bird's eye view"
- Specify lighting: "golden hour", "soft diffused light", "dramatic shadows"
- Include lens details: "85mm portrait lens", "bokeh background"

### 3. Specify Mood and Atmosphere
- "serene and peaceful"
- "dramatic and moody"
- "bright and cheerful"

### 4. Include Fine Details
- Textures: "rough clay", "smooth silk", "weathered wood"
- Colors: "warm amber tones", "cool blue hues"
- Composition: "rule of thirds", "centered subject"

## Testing

All components have been verified:
- ✅ Provider imports successfully
- ✅ Tool function imports successfully
- ✅ Provider registered in IMAGE_PROVIDERS
- ✅ Tool registered in TOOL_MAPPING
- ✅ Syntax validation passed

## Limitations

1. **Aspect Ratio**: Gemini may not strictly enforce the requested aspect ratio
2. **Image URLs**: The provider currently doesn't support direct image URLs as input (only base64)
3. **Rate Limits**: Subject to Google AI Studio API rate limits
4. **Watermarking**: All images include SynthID watermarks (cannot be disabled)

## References

- [Gemini API Image Generation Docs](https://ai.google.dev/gemini-api/docs/image-generation)
- [Google AI Studio](https://aistudio.google.com/)
- [Gemini 2.5 Flash Image Model](https://aistudio.google.com/models/gemini-2-5-flash-image)

## Support

For issues or questions:
1. Check that your Gemini API key is valid and has image generation enabled
2. Verify the API key is correctly configured in `config.toml`
3. Check server logs for detailed error messages
4. Ensure you're using descriptive prompts (not just keywords)
