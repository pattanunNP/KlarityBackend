
from fastapi import FastAPI, WebSocket
from controller.verification_controller import verification_api
from fastapi.middleware.cors import CORSMiddleware
from metadata import tags_metadata


def create_fastapi_app() -> FastAPI:

    app: FastAPI = FastAPI(
        title="API for Klarity",
        description="API for Klarity",
        version="0.0.1",
        openapi_url="/api/v1/openapi.json",
        license_info={
            "name": "Apache 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        },
        openapi_tags=tags_metadata

    )
    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)

    @app.get("/")
    async def home():
        return "Hello This Klarity Backend"


    @app.websocket("/ws")
    async def websocket_endpoint(websocket: WebSocket):
        await websocket.accept()
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")

    app.include_router(verification_api, prefix="/api/v1",tags=["verification"])

    return app



app = create_fastapi_app()