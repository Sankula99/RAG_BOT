import weaviate
from weaviate.classes.config import Property, DataType
from weaviate.classes.config import Configure

def get_client():
    client = weaviate.connect_to_local()
    return client
def create_collection(client):
    if client.collections.exists("Documents"):
        return
    client.collections.create(
        name = "Documents",
        vectorizer_config = Configure.Vectorizer.none(),
        properties =[
            Property(name="content",data_type = DataType.TEXT),
            Property(name="source",data_type= DataType.TEXT)
            ],
        )
def store_documents(chunks,embeddings,client,source_filename):
    collection = client.collections.get("Documents")
    with collection.batch.dynamic()as batch:
        for chunk,embedding in zip(chunks,embeddings):
            try:
                batch.add_object(
                    properties={"content":chunk,"source":source_filename},
                    vector= embedding
                )
            except Exception as e:
                print(f"Error storing chunk: {e}")
            
    print(f"Stored{len(chunks)}chunks in Weaviate.")
