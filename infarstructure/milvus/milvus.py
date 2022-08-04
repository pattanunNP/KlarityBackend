from domain.base.Singleton import Singleton
from config.config import MilvusConfig
from pymilvus import connections


class MilvusConnector(metaclass=Singleton):
    ENV = MilvusConfig()

    milvus = connections.connect(
        alias="default", 
        host='localhost', 
        port='19530'
    )


    @classmethod
    def connect(cls):
        print("Milvus => Connected")
        return cls.milvus



