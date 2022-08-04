

from fastapi import (
    APIRouter,
    UploadFile,
    HTTPException,
    File
)
import socketio
from service.verification import Verification
from datetime import datetime
from domain.model.payload import VerifySessionPayload

verification_api = APIRouter(
    prefix="/verification"
)
Verification = Verification()

sio = socketio.AsyncServer(async_mode="asgi")
socket_app = socketio.ASGIApp(sio)

@sio.event
def connect(sid, environ, auth):
    print('connect ', sid)

@verification_api.get("/generate")
async def generate_session():
    """
    Generate Session Token.

    This will generate TTL token and store on 

    in-memory database:

    * Generate Token.
    * Store Token into redis.
    """

    session_token = Verification.gennerate_session_code()

    return {
        "issure_at": datetime.now(),
        "session_token": session_token,
        "expire_at": int(datetime.timestamp(datetime.utcnow()) * 1000)
    }


@verification_api.post("/verify-session")
async def verify_session(data: VerifySessionPayload):
    """
    Verify Session Token.

    This will verify token is existed
    
    in-memory database:

    * Verify Token.
    """
    token = data.session_token
    session = Verification.verify_session_code(session_code=token)
    
    if not session:
        return {
            "status": "Invalid or Expired token",
        }
    else:
        return {
            "status": "Verified",
        }
        sio.emit(f'{token}',"Verify complete")


@verification_api.post("/verify-exist")
async def verify_exist(
        file: UploadFile=File(...),
):
    """
    Verify is exist Face Data in DB.

    in-memory database:

    * Receive face image convert to embedding vector.
    * Check is exist face data in DB.
    """
     
    if not file :
        raise HTTPException(status_code=400, detail="No file submit")
    else:
        query = await file.read()
        res = Verification.face_recognition(query_face=query)
        return res
        


@verification_api.post("/register-face")
async def register_face(
        file: UploadFile=File(...),
):
    """
    Verify is exist Face Data in DB.

    in-memory database:

    * Receive face image convert to embedding vector.
    * Check is exist face data in DB.
    """
     
    if not file :
        raise HTTPException(status_code=400, detail="No file submit")
    else:
        query = await file.read()
        try:
            Verification.register_face(query)
            return {
                "message":"face registed"
            }
        except:
            raise HTTPException(status_code=503, detail="Error Register")
