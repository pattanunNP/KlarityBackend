from domain.base.Singleton import Singleton
from config.config import MilvusConfig
from pymilvus import connections


class MilvusConnector(metaclass=Singleton):
    ENV = MilvusConfig()

    milvus = connections.connect(
        alias=ENV.MILVUS_ALAIS,
        host=ENV.MILVUS_HOST,
        port=ENV.MILVUS_PORT
    )

    @classmethod
    def connect(cls):
        print("Milvus => Connected")
        return cls.milvus



