from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return JSONResponse(
        status_code=200,
        content={"message": "API is running"}
    )

@app.get("/health")
def health():
    return JSONResponse(
        status_code=200,
        content={"message": "healthy", "cpu":"True","memory": 1300}
    )

@app.get("/me")
def me():
    return JSONResponse(
        status_code=200,
        content={
            "name": "Godand Brin Duburah",
            "email": "writearinze00@gmail.com",
            "github_url": "https://github.com/godhanded",
            "repo_name": "Devpos",
            "github": "https://github.com/godhanded"

        }
    )
