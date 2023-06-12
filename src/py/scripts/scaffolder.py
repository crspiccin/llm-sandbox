from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    SystemMessage
)
import os
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(dotenv_path=Path("../.env"))

import argparse
 
parser = argparse.ArgumentParser(description="Just an example",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-a", "--archive", action="store_true", help="archive mode")
parser.add_argument("-v", "--verbose", action="store_true", help="increase verbosity")
args = parser.parse_args()



def run_chat_model():
    print('starting the model ')
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5)

    system_template = "Act as a seasoned senior software developer specialist in {language}"
    human_template = "Create a {entity} entity following hexagonal architecture with services layer covered by unit test including operations like create, update, read and delete following SQL ANSI on a repository layer, and expose it on adapter layer by a {api_type} api."

    chat_prompt = ChatPromptTemplate.from_messages([SystemMessagePromptTemplate.from_template(system_template), HumanMessagePromptTemplate.from_template(human_template)])

    messages = chat_prompt.format_prompt(language="python", entity="Transaction", api_type="REST").to_messages()

    messages.append(SystemMessage(content="On each file put BREAK at the beginning followed by filename"))

    content = chat(messages).content
    return content

def run_llm_chain_model():
    print('starting the llm model ')
    llm = OpenAI(temperature=0.7)
    chat = ChatOpenAI(temperature=0.7)

    prompt_template = """"
        Act as a senior software developer specialist in {language} and following the code conventions , 
        create a {entity} entity microservice following hexagonal architecture frameworks with services layer including operations like create, update, read and delete and following SQL ANSI on a repository layer, expose it on adapter layer by a {api_type} api,
        create unit test for the services layer,
        create the build file with the dependencies necessary to build the service,
        On each file put in the first line the word BREAK, on the second line the file name and on the remaining lines the source body 
    """

    prompt = PromptTemplate(
        template = prompt_template,
        input_variables=["language", "entity", "api_type"]
    )

    chain = LLMChain(llm=chat, prompt=prompt)

    return chain.run({"language":"typescript", "entity":"Payment", "api_type":"REST"})

output_dir =  "../../../output/"

def output_files(llm_output):
    files = llm_output.split("BREAK")
    for file in files:
        tokens = file.split("\n")
        for token in tokens:
            if token != '':
                print(token)
                # print(file.replace(token, ""))
                with open(output_dir + token, 'w+') as fp:
                    fp.write(file.replace(token, ""))
                    pass
                break



output_files(run_llm_chain_model())


