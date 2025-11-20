import httpx
import os
from .config import OPENAI_API_KEY, ULTRAMSG_INSTANCE_ID, ULTRAMSG_TOKEN

async def ask_gpt(prompt: str) -> str:
    import openai
    openai.api_key = OPENAI_API_KEY

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

async def send_whatsapp(to_number: str, message: str):
    """
    Send WhatsApp message via UltraSMG
    to_number: e.g. "+923001234567"
    """
    url = f"https://api.ultramsg.com/{ULTRAMSG_INSTANCE_ID}/messages/chat"
    data = {
        "token": ULTRAMSG_TOKEN,
        "to": to_number,
        "body": message
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, data=data)
        return response.json()
