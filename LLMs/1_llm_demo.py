# now a days no one is using this llm based every thing is transformed to ChatModels.
# the bwloe code will be the a text input and give the text oupput


from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")

result = llm.invoke("what is the capital of USA")

print(result)
