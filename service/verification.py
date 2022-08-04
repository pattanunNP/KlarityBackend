
from datetime import datetime
from uuid import uuid4
from repository.sessionRepository import sessionReposity
from repository.faceRepository import faceRepository
from utils.facedetection import FaceEmbredding
from PIL import Image
import numpy as np
import io
from fastapi import (
 
    HTTPException,

)


class Verification:

    
    def __init__(self) -> None:

        self.sessionReposity = sessionReposity()
        self.FaceEmbredding =  FaceEmbredding()
        self.faceRepository= faceRepository()
        

    def gennerate_session_code(self):
        session_token = str(uuid4())
        exp = int(datetime.timestamp(datetime.utcnow())*1000)

        try:

            self.sessionReposity.save(session_token, exp)
            return session_token
        except:
            print("Save Error")

    def verify_session_code(self,session_code):
        try:

            if self.sessionReposity.search(session_code) != None:
                return True
            else:
                return False

        except:
            print("Get Error")

    def register_face(self, face_image):
        image = Image.open(io.BytesIO(face_image))
        
        aligned_face = self.FaceEmbredding.detect_faces(image)
        result = self.FaceEmbredding.get_feature(aligned=aligned_face)
        print(result)
        uuid = str(uuid4())
        data = [
            [uuid],
            [result[0].cpu().detach().numpy()]
        ]
        print(data)
        try:

            self.faceRepository.save(data)
        except:
            raise HTTPException(status_code=400,detail="Register Face Error")
        
        

    def face_recognition(self,query_face):
        image = Image.open(io.BytesIO(query_face))
        
        aligned_face = self.FaceEmbredding.detect_faces(image)
        embedding = self.FaceEmbredding.get_feature(aligned=aligned_face)


        res = self.faceRepository.search(embedding.cpu().detach().numpy())
        print(res[0][0].distance, res[0][0].id)
        
        

        if float(res[0][0].distance) <= 0.8:
            return {
                "distance":res[0][0].distance,
                "match":res[0][0].id
            }
        else:
            raise HTTPException(status_code=404,detail="Not Match")
     
        
        
        
        
        
        
        
