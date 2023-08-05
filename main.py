from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def hello():
    return 'hello docker!'

if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)

#로컬에서 백엔드 실행