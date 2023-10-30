from typing import Any, Dict, Optional

from pymongo import MongoClient


class MongoDBUtility:
    def __init__(
        self, db_uri: str = "mongodb://localhost:27017/", db_name: str = "DefaultDB"
    ):
        self.client = MongoClient(db_uri)
        self.db = self.client[db_name]

    def set_collection(self, collection_name: str) -> None:
        self.collection = self.db[collection_name]

    def insert_data(self, data: Dict[str, Any]) -> None:
        self.collection.insert_one(data)

    def fetch_data(self, query: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        result = self.collection.find_one(query)
        return result

    def update_data(self, query: Dict[str, Any], new_data: Dict[str, Any]) -> None:
        self.collection.update_one(query, {"$set": new_data})

    def delete_data(self, query: Dict[str, Any]) -> None:
        self.collection.delete_one(query)


# Example Usage
if __name__ == "__main__":
    db = MongoDBUtility(db_name="ResearchDB")
    db.set_collection("ResearchCollection")

    '''db.insert_data(
        {"Industry": "Tech", "Business": "Software", "Summary": "Some Summary"}
    )
    print(db.fetch_data({"Industry": "Tech", "Business": "Software"}))'''
