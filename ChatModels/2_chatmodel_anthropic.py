from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(model="modelname", temperature=1, max_completion_tokens=10)

result = llm.invoke("what is the capital of Canada")

print(result.content)