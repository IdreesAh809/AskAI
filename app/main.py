from fastapi import FastAPI, Request
from .services import ask_gpt, send_whatsapp

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "AskAI WhatsApp bot running!"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    sender = data.get("from")       # WhatsApp number
    message = data.get("body")      # Received message

    if sender and message:
        reply = await ask_gpt(message)
        await send_whatsapp(sender, reply)

    return {"status": "success"}
