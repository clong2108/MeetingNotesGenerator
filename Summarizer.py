import os
from azure.ai.inference.models import SystemMessage, UserMessage
from dotenv import load_dotenv
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential



class Summarizer:
    def summarize_text(self, text):
        load_dotenv()
        client = ChatCompletionsClient(

            endpoint=os.environ["ENDPOINT_URL"],

            credential=AzureKeyCredential(os.environ["DEEPSEEK_KEY"])

        )

        completion = client.complete(
            model = "DeepSeek-R1",
            messages = [
                SystemMessage(content="You are a intelligent assistant meant to create a summary of a meeting using bullet points targeting important information, dates and days, and names."),
                UserMessage(content=text)
            ]
        )
        return completion.choices[0].message.content