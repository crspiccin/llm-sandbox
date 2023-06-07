from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    SystemMessage
)
from langchain.output_parsers import PydanticOutputParser
# from pydantic import BaseModel, Field

from dotenv import load_dotenv
load_dotenv()
import re


# class File(BaseModel):
#     file_name: str = Field(description="file name")
#     file_body: str = Field(description="file body")


# parser = PydanticOutputParser(pydantic_object=File)

def run_model():
    print('starting the model ')
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

    system_template = "Act as a senior software development specialist in {language}"
    human_template = "Create a {entity} entity following hexagonal architecture with services layer covered by unit test including operations like create, update, read and delete following SQL ANSI on a repository layer, and expose it on adapter layer by a {api_type} api."

    chat_prompt = ChatPromptTemplate.from_messages([SystemMessagePromptTemplate.from_template(system_template), HumanMessagePromptTemplate.from_template(human_template)])

    messages = chat_prompt.format_prompt(language="typescript", entity="User", api_type="REST").to_messages()

    messages.append(SystemMessage(content="On each file put BREAK at the beginning followed by file name enclosed by {}"))
    # print(messages)

    content = chat(messages).content
    return content

print(run_model())


