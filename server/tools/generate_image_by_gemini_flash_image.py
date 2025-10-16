from typing import Annotated
from pydantic import BaseModel, Field
from langchain_core.tools import tool, InjectedToolCallId  # type: ignore
from langchain_core.runnables import RunnableConfig
from tools.utils.image_generation_core import generate_image_with_provider


class GenerateImageByGeminiFlashImageInputSchema(BaseModel):
    prompt: str = Field(
        description="Required. The prompt for image generation. Describe the scene in detail rather than just listing keywords. For editing, describe what you want to change."
    )
    aspect_ratio: str = Field(
        description="Required. Aspect ratio of the image, only these values are allowed: 1:1, 16:9, 4:3, 3:4, 9:16. Choose the best fitting aspect ratio according to the prompt. Best ratio for posters is 3:4. Note: Gemini may not strictly enforce aspect ratios."
    )
    tool_call_id: Annotated[str, InjectedToolCallId]


@tool("generate_image_by_gemini_flash_image",
      description="Generate an image using Google's Gemini 2.5 Flash Image model (aka Nano Banana). This model excels at photorealistic images, text rendering, and conversational image editing. Supports text-to-image generation and image editing when input images are provided. Use descriptive, narrative prompts for best results.",
      args_schema=GenerateImageByGeminiFlashImageInputSchema)
async def generate_image_by_gemini_flash_image(
    prompt: str,
    aspect_ratio: str,
    config: RunnableConfig,
    tool_call_id: Annotated[str, InjectedToolCallId],
) -> str:
    ctx = config.get('configurable', {})
    canvas_id = ctx.get('canvas_id', '')
    session_id = ctx.get('session_id', '')
    print(f'🛠️ canvas_id {canvas_id} session_id {session_id}')
    return await generate_image_with_provider(
        canvas_id=canvas_id,
        session_id=session_id,
        provider='gemini',
        model='gemini-2.5-flash-image',
        prompt=prompt,
        aspect_ratio=aspect_ratio,
    )


# Export the tool for easy import
__all__ = ["generate_image_by_gemini_flash_image"]
