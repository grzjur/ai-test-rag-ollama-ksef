# Wykorzystanie RAG w KSeF: Wyniki Testów Lokalnych Modeli Językowych


Celem przeprowadzonego testu modeli językowych było sprawdzenie, jak skutecznie różne modele radzą sobie z odpowiadaniem na pytania dotyczące funkcjonowania i zasad Krajowego Systemu e-Faktur (KSeF). Test miał na celu ocenę, które modele są najbardziej trafne i użyteczne w kontekście RAG (Retrieval-Augmented Generation)

Testowane modele:
- llama3
- mistral
- aya
- wizardlm2
- phi3
- gemma

Wyniki pokazują znaczące różnice w zdolności modeli do generowania dokładnych i adekwatnych odpowiedzi.

---
## llama3
Model daje poprawne odpowiedzi przy prostych pytaniach, jednak instrukcje, by "zastanowić się", mogą być mylące i nieprofesjonalne (instrukcja pochodzi z promptu). Mimo to, ogólny sens odpowiedzi jest zgodny z oczekiwaniami.

## mistral
Model dobrze poradził sobie z pytaniami, udzielając poprawnych odpowiedzi zgodnych z zasadami i informacjami dotyczącymi KSeF. Najlepiej odpowiedzi były udzielone na pytania o proformy i o numer KSeF w urzędowym poświadczeniu odbioru - były precyzyjne i zgodne z wymaganiami.

## aya
Podobnie jak mistral, dobrze radzi sobie z pytaniami. Odpowiedzi były precyzyjne i zgodne z wymaganiami. Były bardziej zwięzłe niż w modelu mistral - może to efekt 'zrozumienia' promptu "Odpowiadaj zwięźle"

## wizardlm2
W większości przypadków odpowiedzi były bliskie poprawnym, ale brakowało im jednoznaczności wymaganej do specjalistycznych zastosowań księgowych i podatkowych. Model nie 'zrozumiał' instrukcji "Odpowiadaj zwięźle"

## phi3
Odpowiedzi są często zbyt skomplikowane, niejasne, rozległe i nie odpowiadają bezpośrednio na pytania.

## gemma
Model radzi sobie dobrze z odpowiadaniem na proste i jednoznaczne pytania, ma wyraźne trudności z bardziej złożonymi pytaniami

---
## Wnioski
Modele **aya** i **mistral** najlepiej radziły sobie z generowaniem dokładnych odpowiedzi na zadane pytania. Model **llama3** również dobrze się spisał, choć wprowadzał nadmiarowe wstępy, które mogły zdezorientować użytkowników. Modele **wizardlm2, gemma i phi3** miały największe trudności z dostarczeniem poprawnych odpowiedzi, często wprowadzając błędne informacje i zbyt dużo niezwiązanych szczegółów.
