from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from models import Login, Register

app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")


@app.get("/", response_class=HTMLResponse)
def home():
    return FileResponse("./static/index.html", status_code=200)


@app.get("/login", response_class=HTMLResponse)
def login_view() -> FileResponse:
    return FileResponse("./static/login.html", status_code=200)

@app.post("/login", response_class=JSONResponse)
def login(login: Login = Body(...)) -> JSONResponse:
    