
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
        self.Milvus = MilvusConnector()
        fields = [
            FieldSchema(name="pk", dtype=DataType.INT64, is_primary=True, auto_id=False),
            FieldSchema(name="uuid", dtype=DataType.DOUBLE),
            FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=8)
        ]
        schema = CollectionSchema(fields, "hello_milvus is the simplest demo to introduce the APIs")
        self.collection = Collection("face", schema)
        index = {
            "index_type": "IVF_FLAT",
            "metric_type": "L2",
            "params": {"nlist": 128},
        }
        self.collection.create_index("embeddings", index)


    def save(self,entity):
        return  self.insert(entity)

    def search(self, query):
        search_params = {"metric_type": "L2", "params": {"nprobe": 10}} 
        results = self.collection.search(
            data=query, 
            anns_field="embeddings", 
            param=search_params, 
            limit=10, 
            expr=None,
            consistency_level="Strong"
        )
        return results