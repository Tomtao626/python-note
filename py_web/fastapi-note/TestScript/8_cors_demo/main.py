import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tomtao626.com",
    "https://localhost.tomtao626.com",
    "http://localhost",
    "http://localhost:8088",
]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

@app.get('/')
async def main():
    return dict(msg='hello cors')


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8088, reload=True, debug=True)