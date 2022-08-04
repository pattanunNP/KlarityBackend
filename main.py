
from fastapi import FastAPI
from controller.verification_controller import verification_api
from fastapi.middleware.cors import CORSMiddleware
from metadata import tags_metadata

import uvicorn
from controller.verification_controller import socket_app

        
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


  
    app.include_router(verification_api, prefix="/api/v1",tags=["verification"])

    return app



app = create_fastapi_app()
    
# socket_manager = SocketManager(app=app)
if  __name__ == "__main__":
 
    kwargs = {"host": "0.0.0.0", "port": 5000}
    kwargs.update({"debug": True, "reload": True})
    uvicorn.run("main:app", **kwargs)


    
