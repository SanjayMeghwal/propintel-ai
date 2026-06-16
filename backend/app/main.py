from fastapi import FastAPI

app = FastAPI(
    title="PropIntel AI",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "PropIntel AI Running"
    }