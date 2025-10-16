# Gemini 2.5 Flash Image Integration

## Overview

Jazz now supports Google's Gemini 2.5 Flash Image model (nicknamed "Nano Banana") for AI-powered image generation. This integration provides high-quality text-to-image generation with excellent photorealism and text rendering capabilities.

## Key Features

- **Text-to-Image Generation**: Create images from descriptive text prompts
- **Photorealistic Quality**: Excellent at realistic scenes with proper lighting
- **Text Rendering**: Generates legible text in images (logos, posters, signs)
- **Image Editing**: Modify existing images with text prompts
- **Conversational Refinement**: Iterate on images through multi-turn conversations
- **SynthID Watermarking**: All images include authenticity watermarks

## Quick Start

### 1. Get API Key
Visit [Google AI Studio](https://aistudio.google.com/apikey) to get your free API key.

### 2. Configure
Add your API key in Settings → Providers → Gemini, or edit `config.toml`:

```toml
[gemini]
url = "https://generativelanguage.googleapis.com/v1beta/"
api_key = "YOUR_API_KEY_HERE"
max_tokens = 8192

[gemini.models."gemini-2.5-flash-image"]
type = "image"
is_custom = true
```

### 3. Generate
Open a chat and ask the AI to create images:

```
Generate a photorealistic image of a cozy coffee shop on a rainy day
```

## Documentation

- **Quick Start**: [`GEMINI_QUICK_START.md`](../GEMINI_QUICK_START.md)
- **User Guide**: [`USER_GUIDE_GEMINI_IMAGE.md`](../USER_GUIDE_GEMINI_IMAGE.md)
- **Technical Details**: [`GEMINI_IMAGE_INTEGRATION.md`](../GEMINI_IMAGE_INTEGRATION.md)
- **Integration Summary**: [`INTEGRATION_SUMMARY.md`](../INTEGRATION_SUMMARY.md)

## Example Prompts

### Basic
```
A peaceful zen garden with a small pond and cherry blossoms
```

### Photorealistic
```
A photorealistic close-up of a steaming cup of coffee on a wooden table. 
Soft morning light streams through a window, creating warm golden tones. 
The coffee has beautiful latte art. Shot with an 85mm lens.
```

### With Text
```
Create a vintage poster for a jazz club. Include the text "Blue Note Jazz" 
in elegant art deco typography. Dark blue background with gold accents.
```

## Best Practices

1. **Use Descriptive Prompts**: Narrative descriptions work better than keyword lists
2. **Include Photography Terms**: Mention lighting, camera angles, and mood
3. **Specify Aspect Ratios**: Choose from 1:1, 16:9, 9:16, 4:3, or 3:4
4. **Iterate Through Conversation**: Refine images by asking for specific changes
5. **Leverage Text Generation**: Gemini excels at rendering text in images

## Comparison

| Feature | Gemini 2.5 Flash | Other Models |
|---------|------------------|--------------|
| Text in Images | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Photorealism | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Speed | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Conversational | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Cost | Free tier | Varies |

## Troubleshooting

**Tool not appearing?**
- Verify API key is configured
- Restart Jazz application
- Check API key is valid

**Generation fails?**
- Check internet connection
- Verify API quota
- Try simpler prompts

**Poor results?**
- Use more descriptive prompts
- Add photography terminology
- Specify style and mood

## Technical Details

- **Model**: `gemini-2.5-flash-image`
- **API**: Google AI Studio (generativelanguage.googleapis.com)
- **Authentication**: API key
- **Response Format**: Base64 encoded images
- **Watermarking**: SynthID included in all images

## Resources

- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs/image-generation)
- [Model Page](https://aistudio.google.com/models/gemini-2-5-flash-image)

## Support

For issues or questions:
1. Check the troubleshooting section in the user guide
2. Verify your configuration
3. Review the technical documentation
4. Join the Jazz community for support

---

**Version**: 1.0.0  
**Last Updated**: October 2025  
**Status**: Production Ready ✅
