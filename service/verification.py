
from datetime import datetime
from uuid import uuid4
from repository.sessionRepository import sessionReposity
from repository.faceRepository import faceRepository
from utils.facedetection import FaceEmbredding
from PIL import Image
import numpy as np
import io


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
        image = np.asarray(Image.open(io.BytesIO(face_image)))
        
        aligned_face,_ = self.FaceEmbredding.detect_faces(image)
        result = self.FaceEmbredding.get_feature(aligned=aligned_face)
        
        


    def face_recognition(self,query_face):
        image = np.asarray(Image.open(io.BytesIO(query_face)))
        
        aligned_face,_ = self.FaceEmbredding.detect_faces(image)
        result = self.FaceEmbredding.get_feature(aligned=aligned_face)
        
        
        print(result[0].shape)
        
        
