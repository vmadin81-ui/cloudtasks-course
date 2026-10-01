from fastapi import FastAPI

app = FastAPI(title="CloudTasks", version="0.1.0")


@app.get("/")
def root():
    return {"service": "CloudTasks", "version": "0.1.0"}


@app.get("/health")
def health():
    # Проверяет только обработку запроса процессом приложения.
    return {"status": "ok"}
