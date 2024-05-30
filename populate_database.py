from langchain.schema.document import Document
from get_embedding_function import get_embedding_function
from langchain_community.vectorstores import Chroma
import os
import json

CHROMA_PATH = "chroma"
DATA_PATH = "data"

def main():
    document = load_document_json('questions.json')
    chunks = split_document(document)
    add_to_chroma(chunks)


def load_document_json(file: str):
    file_path = os.path.join(DATA_PATH, file)
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    documents = []
    for item in data['questions']:
        documents.append(Document(page_content=item['question'], metadata={'answer': item['answer']}))
    return documents


def split_document(documents: list[Document]):
    special_chunks = []
    for document in documents:
        question_text = document.page_content
        answer_text = document.metadata.get('answer', 'Brak odpowiedzi')
        chunk = Document(
            page_content=question_text,
            metadata={
                'source': document.metadata.get('source', 'unknown'),
                'page': document.metadata.get('page', 'unknown'),
                'answer': answer_text
            }
        )
        special_chunks.append(chunk)
    return special_chunks


def add_to_chroma(chunks: list[Document]):
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=get_embedding_function())
    chunks_with_ids = calculate_chunk_ids(chunks)

    existing_items = db.get(include=[])  # IDs are always included by default
    existing_ids = set(existing_items["ids"])
    print(f"Number of existing documents in DB: {len(existing_ids)}")

    new_chunks = []
    for chunk in chunks_with_ids:
        if chunk.metadata["id"] not in existing_ids:
            new_chunks.append(chunk)

    if len(new_chunks):
        print(f"👉 Adding: {len(new_chunks)} ...")
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        db.add_documents(new_chunks, ids=new_chunk_ids)
        print("✅ Completed")
    else:
        print("✅ Nothing to add")


def calculate_chunk_ids(chunks):
    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"
        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0
        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id
        chunk.metadata["id"] = chunk_id
    return chunks


if __name__ == "__main__":
    main()