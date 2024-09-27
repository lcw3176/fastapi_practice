from fastapi import FastAPI, Request, Response
from starlette.middleware.cors import CORSMiddleware
from domain.community.comment import comment_router
from domain.community.post import post_router
from domain.notice import notice_router
from starlette.types import Message
from starlette.background import BackgroundTask
import logging



app = FastAPI()

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(comment_router.router)
app.include_router(post_router.router)
app.include_router(notice_router.router)




logger = logging.getLogger("main")
logging.basicConfig(level=logging.DEBUG)
steam_handler = logging.FileHandler('info.log', mode='w')
logger.addHandler(steam_handler)

def log_info(req_body, res_body):
    logging.info(req_body)
    logging.info(res_body)

async def set_body(request: Request, body: bytes):
    async def receive() -> Message:
        return {'type': 'http.request', 'body': body}
    request._receive = receive
    
@app.middleware('http')
async def some_middleware(request: Request, call_next):
    req_body = await request.body()
    await set_body(request, req_body)
    response = await call_next(request)
    
    res_body = b''
    async for chunk in response.body_iterator:
        res_body += chunk
    
    task = BackgroundTask(log_info, req_body, res_body)
    return Response(content=res_body, status_code=response.status_code, 
        headers=dict(response.headers), media_type=response.media_type, background=task)
