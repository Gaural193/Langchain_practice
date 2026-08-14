# In this file we will see that how we generate a Embeddings for more than one string.

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)
#dimensions=32 means the number of numerical values in the embedding vector.

documents = [
    "delhi is the capital of india",
    "Gandhinagar is the capital of Gujarat",
    "Washington DC is the capital of USA"
]
result = embedding.embed_documents(documents)

print(str(result))