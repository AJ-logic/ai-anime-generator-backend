from fastapi import FastAPI, Form
from fastapi.responses import StreamingResponse
import torch
from diffusers import StableDiffusionPipeline
from io import BytesIO
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

pipe = StableDiffusionPipeline.from_pretrained(
    # "hakurei/waifu-diffusion",
    "./waifu-diffusion",
    torch_dtype=torch.float32
).to('cpu')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
def generate_image(prompt: str = Form(...)):
    image = pipe(prompt, guidance_scale=8, num_inference_steps=50).images[0]
    buf = BytesIO()
    image.save(buf, format="PNG")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
