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


from dotenv import load_dotenv
load_dotenv("../.env")



def run_chat_model():
    print('starting the model ')
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

    system_template = "Act as a seasoned senior software developer specialist in {language}"
    human_template = "Create a {entity} entity following hexagonal architecture with services layer covered by unit test including operations like create, update, read and delete following SQL ANSI on a repository layer, and expose it on adapter layer by a {api_type} api."

    chat_prompt = ChatPromptTemplate.from_messages([SystemMessagePromptTemplate.from_template(system_template), HumanMessagePromptTemplate.from_template(human_template)])

    messages = chat_prompt.format_prompt(language="python", entity="Transaction", api_type="REST").to_messages()

    messages.append(SystemMessage(content="On each file put BREAK at the beginning followed by filename"))
    # print(messages)

    content = chat(messages).content
    return content

def run_llm_chain_model():
    print('starting the llm model ')
    llm = OpenAI(temperature=0.7)
    chat = ChatOpenAI(temperature=0.7)

    prompt_template = """"
        Act as a senior software developer specialist in {language}
        Create a {entity} entity microservice following hexagonal architecture frameworks and with services layer covered by unit tests including operations like create, update, read and delete and following SQL ANSI on a repository layer, expose it on adapter layer by a {api_type} api.
        On each file put in the first line the word BREAK, on the second line the file name and on the remaining lines the source body 
    """

    prompt = PromptTemplate(
        template = prompt_template,
        input_variables=["language", "entity", "api_type"]
    )

    chain = LLMChain(llm=chat, prompt=prompt)

    return chain.run({"language":"go", "entity":"Payment", "api_type":"GraphQL"})


def output_files(llm_output):
    files = llm_output.split("BREAK")
    for file in files:
        tokens = file.split("\n")
        for token in tokens:
            if token != '':
                print(token)
                # print(file.replace(token, ""))
                with open(r'../output/' + token, 'w') as fp:
                    fp.write(file.replace(token, ""))
                    pass
                break



output_files(run_llm_chain_model())


