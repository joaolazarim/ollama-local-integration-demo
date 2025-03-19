from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests
import json

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str
    model: str = "llama3.2"

@app.post("/generate")
async def generate(prompt_request: PromptRequest):
    ollama_endpoint = "http://localhost:11434/api/generate"

    request_body = {
        "model": prompt_request.model,
        "prompt": prompt_request.prompt,
        "stream": False
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(ollama_endpoint, headers=headers, data=json.dumps(request_body))

    if response.status_code == 200:
        return {"response": response.text}
    else:
        return {"error": response.text, "status_code": response.status_code}