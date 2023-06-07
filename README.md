# llm-sandbox

This is a repo for my studies on large language models. On */py* folder, it has jupyter notebook for prototyping. The notebook */py/llm.ipynb* has a study based on a pdf article, it shows how we can use private data with large language models. It's like a conversation with the document.

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
