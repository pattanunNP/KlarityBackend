
import numpy as np
from sklearn import preprocessing
import gdown
from pathlib import Path
from facenet_pytorch import MTCNN, InceptionResnetV1


class FaceEmbredding:
    def __init__(self) -> None:
 

        self.FaceDetector = MTCNN()
        self.resnet = InceptionResnetV1(pretrained='vggface2').eval()
        
        # model_path = Path("model_data/arcfaceresnet100-8.onnx")

        # if  model_path.exists():
        #     self.model = ort.InferenceSession(model_path.as_posix())
        # else: 
        #     url = "https://drive.google.com/file/d/1KhlLsqYOj9VnxO3UVP1TaMgi4O3S68Xz"
        #     output = "model_data/arcfaceresnet100-8.onnx"
        #     gdown.download(url, output, quiet=False)
        #     if  model_path.exists():
        #         self.model = ort.InferenceSession(model_path.as_posix())



    def detect_faces(self,face_image, crop_face=True):
        """
        Crop FaceImagePreprocessing
        params:
        ------
            - face_image  [Required] :  np.array of image (np.array)
        """
        
        # print(face_image.shape)

        
        return self.FaceDetector(face_image)
        

        
    
    def get_feature(self,aligned):
  
       
        # print(aligned[0].shape)
        
        # input_blob = np.resize(aligned[0].astype('float32'),(1,3,112,112))
        # # print(input_blob.shape)
     

        
        # ort_inputs = {self.model.get_inputs()[0].name:  input_blob }
        # embedding = self.model.run(None,ort_inputs)
        # Get cropped and prewhitened image tensor
        

        # Calculate embedding (unsqueeze to add batch dimension)
        img_embedding = self.resnet(aligned.unsqueeze(0))
        

        return  img_embedding


