
from infarstructure.milvus import  MilvusConnector
from domain.base.repository import RepositoryAbstract

from pymilvus import (
    
    utility,
    FieldSchema,
    CollectionSchema,
    DataType,
    Collection,
)

class faceRepository(RepositoryAbstract):


    def __init__(self) -> None:
        self.Milvus = MilvusConnector.connect()

        fields = [
            
            FieldSchema(name="uuid",  dtype=DataType.VARCHAR, max_length=200, is_primary=True),
            FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=512)
        ]
        schema = CollectionSchema(fields, "hello_milvus is the simplest demo to introduce the APIs")
        self.collection = Collection("face_recogition5", schema)
        index = {
            "index_type": "IVF_FLAT",
            "metric_type": "L2",
            "params": {"nlist": 1024},
        }
        self.collection.create_index("embeddings", index)


    def save(self,entity):
        try:
            self.collection.insert(entity)
        except Exception as err:
            print(err)
            

    def search(self, query):

        self.collection.load()
        
        search_param = {
            "data": query,
            "anns_field":"embeddings", 
            "param": {"metric_type": "L2", "params": {"nprobe": 20}},
            "limit": 1
        }
        results = self.collection.search(**search_param)
        return results