from autogen_ext.models.openai import OpenAIChatCompletionClient

# Centralized model client (easy to change in future)
model_client = OpenAIChatCompletionClient(
    model='gemini-2.0-flash',
    api_key='AIzaSyBr019iRxayVl6kdeh-J4IhS5hq_YgNP8c',
)
