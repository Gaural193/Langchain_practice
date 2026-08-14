from langchain_openai import ChatOpenAI
# click ctr+on ChatOpenAi to see the base function
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4")


# model = ChatOpenAI(model= "gpt-4", temperature=0, max_completion_tokens=10)
#temperature is a variable we can pass the value between 0 and 2. 0 means a simple o/p and 2 means creativity O/p it can be like 0.1,1.2,1.8,etc
# max_completion_token means the output will contain only 10 words. like this is the restriction.

result = model.invoke("what is capital of USA")

print(result) # this will give the details with the metadata

print(result.content) # this will give direct answer.



