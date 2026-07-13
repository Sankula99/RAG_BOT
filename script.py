import weaviate

client = weaviate.connect_to_local()
client.collections.delete("Documents")
client.close()
print("Wiped.")