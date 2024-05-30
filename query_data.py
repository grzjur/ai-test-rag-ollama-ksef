from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from get_embedding_function import get_embedding_function
from dotenv import load_dotenv

load_dotenv()

MODEL = "llama3"
MODEL_URL = "http://localhost:11434"
THRESHOLD = 380
CHROMA_PATH = "chroma"
PROMPT_TEMPLATE = """
Zastanów się zanim odpowiesz

Kontekst:
---

{context}

---

Odpowiadaj zwięźle
Odpowiadasz w języku Polskim
Jeśli kontekst nie jest wystarczający, aby udzielić odpowiedzi, zgodnie z prawdą mówię: „Nie wiem”.

W oparciu o powyższy kontekst, odpowiedz na pytanie:

###

{question}

###
"""

def main():
    set_model("mistral")
    print(query_rag("Czym różni się wersja KSeF testowa od produkcyjnej?"))


def set_model(pModel: str):
    global MODEL
    MODEL = pModel

def query_rag(query_text: str):
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    results = db.similarity_search_with_score(query_text, k=10)

    context_text = "\n\n---\n\n"
    if results:
        first_document, first_score = results[0]
        if first_score < THRESHOLD:
            context_text = "\n\n---\n\n".join([f"Pytanie: {doc.page_content}\nOdpowieź: {doc.metadata['answer']}" for doc, _score in results])


    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = Ollama(model=MODEL, base_url=MODEL_URL)
    response = model.invoke(prompt)
    return response


if __name__ == "__main__":
    main()