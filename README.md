# llm-sandbox

This is a repo for my studies on large language models using [langchain](https://python.langchain.com/en/latest/index.html#). There are use-case examples like using embeddings to turn private documents into a chat conversation and a script to code scaffolding for a microservice.  

In order to run python scripts:

1 - Create virutal env into the project folder ./py:
```bash
python -m venv ./env
```

2 - Activate the environment:
```bash
source ./env/bin/activate
```

3 - Install packages
```bash
pip install -r requirements.txt
```

For environment deactivation, run:
```bash
deactivate
```

> To run OpenAI API's you must have a secret key and put it on .env file like the following:
```
OPENAI_API_KEY="<key>"
```
