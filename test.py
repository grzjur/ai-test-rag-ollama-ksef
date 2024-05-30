from query_data import query_rag
from query_data import set_model
import json

MODELS = ['aya','llama3', 'mistral', 'wizardlm2', 'phi3', 'gemma']
QUESTIONS = {
    'Czy faktury bez polskiego NIP trzeba zgłaszać do KSeF?',
    'Czy proformy mogą być wystawiane w KSeF?',
    'Czy wystawiając fakturę otrzymam zwrotnie nr nadany przez KSeF?',
    'Czym różni się wersja KSeF testowa od produkcyjnej?'
}
REPEAT=5


results = []
def main():
    for model in MODELS:
        set_model(model)

        model_data = {
            "model": model,
            "questions": []
        }

        print("-------------------------------------------------------------------------------------------------------")
        print(f"Model: {model}")
        for question in QUESTIONS:
            responses = []
            print(f"Pytanie: {question}")
            for x in range(REPEAT):
                response = query_rag(question)
                responses.append(response)
                print(f"Odpowiedź: {response}")

            question_data = {
                "question": question,
                "response": responses
            }
            model_data["questions"].append(question_data)
            print("-----------------------")

        results.append(model_data)

    results_json = json.dumps(results, indent=4, ensure_ascii=False)
    print(results_json)



if __name__ == "__main__":
    main()
