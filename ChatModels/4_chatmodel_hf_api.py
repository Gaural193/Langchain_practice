from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# we are using HugginFaceEndpoint because we are using HuggingFace API.

from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "openai/gpt-oss-20b:groq",
    # in repo_id we will write a name of model from HF.. 
    task="text-generation"
    # in task we will write what tast we want to do.  
)

model = ChatHuggingFace(llm=llm)


result = model.invoke("what is the capit of USA")

print(result.content)





