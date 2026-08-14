from langchain_huggingface import HuggingFaceEmbeddings
#sentence-transformers/all-MiniLM-L6-v2

embedding = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

# text = "Delhi is the capital of india"

# result = embedding.embed_query(text)

# print(str(result))


#belo is for multiple sentance.

document = [
    "delhi is the capital of india",
        "Gandhinagar is the capital of Gujarat",
        "Washington DC is the capital of USA"
]

result = embedding.embed_documents(document)

print(str(result))


