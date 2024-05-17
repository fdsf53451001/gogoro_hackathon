from opensearchpy import OpenSearch
from cohere_embedding import cal_embedding
import os
from dotenv import load_dotenv

load_dotenv()

OPENSEARCH_HOST = os.getenv("OPENSEARCH_HOST")
OPENSEARCH_USER = os.getenv("OPENSEARCH_USER")
OPENSEARCH_PWD = os.getenv("OPENSEARCH_PWD")

def get_client(cluster_url, username, password):

    client = OpenSearch(
        hosts=[cluster_url], http_auth=(username, password), verify_certs=True
    )
    return client

client = get_client(cluster_url=OPENSEARCH_HOST, username=OPENSEARCH_USER, password=OPENSEARCH_PWD)

def retrieve_data(query:str, top_k:int=3) -> list:

    query_embedding = cal_embedding(query)
    query_body = {
        "query": {"knn": {"embedding": {"vector": query_embedding, "k": 3}}},
        "_source": False,
        "fields": ["id", "title"],
    }

    index_name = "movies"
    results = client.search(
        body=query_body,
        index=index_name
    )
    return results["hits"]["hits"]

print(retrieve_data("test"))