from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

load_dotenv()

model = ChatOpenAI()


# #Schema
# class Review(TypedDict):

#     summary: str
#     sentiment: str

# structured_model = model.with_structured_output(Review)


# response = structured_model.invoke(
#     """The phone offers a good overall experience with a clean design, smooth performance, and a decent camera. 
#     The battery easily lasts through a normal day, although heavy usage may require charging sooner. 
#     The display is bright and responsive, while the software is easy to use. 
#     Some features could be improved, but overall, it provides a balanced experience for everyday use."""
# )

# print(response) 
# print(type(response)) 


# # after this we can get a structured output in the form of a Review TypedDict

# print(response['summary'])
# print(response['sentiment'])




#------------------< this is annotated typedDict  >-------------------

# class Review(TypedDict):

#     summary: Annotated[str, "A brief summary of the review."] # here we give some Information about the summary sometimes in big projects just summary word is not enough.
#     sentiment: Annotated[str, "Return statement of the review either positive, negative or neutral"]

# structured_model = model.with_structured_output(Review)


# response = structured_model.invoke(
#     """The phone offers a good overall experience with a clean design, smooth performance, and a decent camera. 
#     The battery easily lasts through a normal day, although heavy usage may require charging sooner. 
#     The display is bright and responsive, while the software is easy to use. 
#     Some features could be improved, but overall, it provides a balanced experience for everyday use."""
# )

# print(response) 
# print(type(response)) 

## ---------------< Annotated more in detail >--------------------------

class Review(TypedDict):

    key_themes: Annotated[list[str], "List of key themes discussed in the review in a list ."]
    summary: Annotated[str, "A brief summary of the review."] # here we give some Information about the summary sometimes in big projects just summary word is not enough.
    sentiment: Annotated[str, "Return statement of the review either positive, negative or neutral"]
    pros: Annotated[Optional[list[str]], "List of pros mentioned in the review."] # we are using Optional to indicate that this field might not be present in all instances
    cons: Annotated[Optional[list[str]], "List of cons mentioned in the review."] # we are using Optional to indicate that this field might not be present in all instances

structured_model = model.with_structured_output(Review)


response = structured_model.invoke(
    """I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.
The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.
However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.
Pros:
- Insanely powerful processor (great for gaming and productivity)
- Stunning 200MP camera with incredible zoom capabilities
- Long battery life with fast charging
- S-Pen support is unique and useful
Cons:
- Bulky and heavy—not great for one-handed use
- Bloatware still exists in One UI
- Expensive compared to competitors"""
)

print(response) 
print(response['summary'])
print(response['sentiment'])

