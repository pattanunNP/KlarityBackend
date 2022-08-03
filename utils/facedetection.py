
from mtcnn_cv2 import MTCNN
import numpy as np
from sklearn import preprocessing
import onnxruntime as ort 

class FaceEmbredding:
    def __init__(self) -> None:
 

        self.detector = MTCNN()
        self.model = ort.InferenceSession('model_data/arcfaceresnet100-8.onnx')



    def detect_faces(self,face_image, crop_face=True):
        """
        Crop FaceImagePreprocessing
        params:
        ------
            - face_image  [Required] :  np.array of image (np.array)
        """
        FaceDetector = MTCNN()
        # print(face_image.shape)

        result = FaceDetector.detect_faces(face_image)

        faces_pos = []
        faces = []

        if len(result) > 0:

            for face in result:

                face_pos = {
                    "bbox": {
                    "left": face["box"][0],
                    "top": face["box"][1],
                    "width": face["box"][2] - face["box"][0],
                    "height": face["box"][3] - face["box"][1],
                }}
                # print(face)
                if crop_face:
                    x, y, w, h = face["box"]

                    center = [x + (w / 2), y + (h / 2)]
                    max_border = max(w, h)

                    left = max(int(center[0] - (max_border / 2)), 0)

                    top = max(int(center[1] - (max_border / 2)), 0)

                    # print(top+max_border, left+max_border)

                    img_k = face_image[top: top + max_border, left: left + max_border]

                    faces.append(img_k)
                    faces_pos.append(face_pos)

            return faces, faces_pos
        else:
            return faces, faces_pos
    
    def get_feature(self,aligned):
  
       
        # print(aligned[0].shape)
        
        input_blob = np.resize(aligned[0].astype('float32'),(1,3,112,112))
        print(input_blob.shape)
     

        
        ort_inputs = {self.model.get_inputs()[0].name:  input_blob }
        embedding = self.model.run(None,ort_inputs)
        

        return  embedding


