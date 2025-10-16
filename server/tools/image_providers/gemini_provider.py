import os
import base64
import traceback
from typing import Optional, Any
from .image_base_provider import ImageProviderBase
from ..utils.image_utils import get_image_info_and_save, generate_image_id
from services.config_service import FILES_DIR
from utils.http_client import HttpClient
from services.config_service import config_service


class GeminiImageProvider(ImageProviderBase):
    """Gemini image generation provider implementation (Nano Banana)"""

    def _build_url(self) -> str:
        """Build request URL for Gemini API"""
        config = config_service.app_config.get('gemini', {})
        base_url = config.get("url", "https://generativelanguage.googleapis.com/v1beta/")
        return f"{base_url}models/gemini-2.5-flash-image:generateContent"

    def _build_headers(self) -> dict[str, str]:
        """Build request headers"""
        config = config_service.app_config.get('gemini', {})
        api_key = config.get("api_key", "")

        if not api_key:
            raise ValueError("Gemini API key is not configured")
        
        return {
            "x-goog-api-key": api_key,
            "Content-Type": "application/json",
        }

    def _build_request_data(
        self,
        prompt: str,
        input_images: Optional[list[str]] = None,
    ) -> dict[str, Any]:
        """
        Build request data for Gemini API
        
        Args:
            prompt: Image generation prompt
            input_images: Optional input images for editing (base64 encoded or URLs)
            
        Returns:
            dict: Request payload for Gemini API
        """
        parts = []
        
        # Add text prompt
        parts.append({"text": prompt})
        
        # Add input images if provided (for editing)
        if input_images:
            for image_data in input_images:
                # Check if it's already base64 or needs to be read
                if image_data.startswith('data:'):
                    # Extract base64 data from data URL
                    mime_type = image_data.split(';')[0].split(':')[1]
                    b64_data = image_data.split(',')[1]
                    parts.append({
                        "inline_data": {
                            "mime_type": mime_type,
                            "data": b64_data
                        }
                    })
                elif image_data.startswith('http'):
                    # URL - Gemini doesn't support URLs directly, skip for now
                    print(f"Warning: Gemini provider doesn't support image URLs directly: {image_data}")
                else:
                    # Assume it's base64 data
                    parts.append({
                        "inline_data": {
                            "mime_type": "image/png",
                            "data": image_data
                        }
                    })
        
        return {
            "contents": [{
                "parts": parts
            }]
        }

    async def _make_request(self, url: str, headers: dict[str, str], data: dict[str, Any]) -> dict[str, Any]:
        """
        Send HTTP request and handle response
        
        Returns:
            dict[str, Any]: Response data from Gemini API
        """
        async with HttpClient.create_aiohttp() as session:
            print(f'🎨 Gemini API request: {url}')
            async with session.post(url, headers=headers, json=data) as response:
                json_data = await response.json()
                print('🎨 Gemini API response received')
                return json_data

    async def _process_response(self, res: dict[str, Any]) -> tuple[str, int, int, str]:
        """
        Process Gemini API response and save image
        
        Args:
            res: Response data from Gemini API
            
        Returns:
            tuple[str, int, int, str]: (mime_type, width, height, filename)
        """
        # Extract image data from response
        candidates = res.get('candidates', [])
        if not candidates:
            error_msg = res.get('error', {}).get('message', 'No candidates in response')
            raise Exception(f'Gemini image generation failed: {error_msg}')
        
        content = candidates[0].get('content', {})
        parts = content.get('parts', [])
        
        # Find the inline_data part (the generated image)
        image_data = None
        for part in parts:
            if 'inline_data' in part:
                image_data = part['inline_data'].get('data')
                break
        
        if not image_data:
            raise Exception('Gemini image generation failed: no image data found in response')
        
        image_id = generate_image_id()
        print('🎨 image generation image_id', image_id)
        
        # Save the base64 image
        mime_type, width, height, extension = await get_image_info_and_save(
            image_data, os.path.join(FILES_DIR, f'{image_id}'), is_b64=True
        )
        
        filename = f'{image_id}.{extension}'
        return mime_type, width, height, filename

    async def generate(
        self,
        prompt: str,
        model: str,
        aspect_ratio: str = "1:1",
        input_images: Optional[list[str]] = None,
        **kwargs: Any
    ) -> tuple[str, int, int, str]:
        """
        Generate image using Gemini API (Nano Banana)
        
        Args:
            prompt: Image generation prompt
            model: Model name (ignored, always uses gemini-2.5-flash-image)
            aspect_ratio: Image aspect ratio (note: Gemini doesn't directly support aspect ratio control)
            input_images: Optional input images for reference or editing
            **kwargs: Additional provider-specific parameters
            
        Returns:
            tuple[str, int, int, str]: (mime_type, width, height, filename)
        """
        try:
            url = self._build_url()
            headers = self._build_headers()
            
            # Build request data
            data = self._build_request_data(prompt, input_images)
            
            # Make request
            res = await self._make_request(url, headers, data)
            
            # Process response and return result
            return await self._process_response(res)
            
        except Exception as e:
            print('Error generating image with Gemini:', e)
            traceback.print_exc()
            raise e
