# Sentence Transformer API

Prosty API do generowania embeddingów tekstu za pomocą SentenceTransformers i FastAPI.

## Uruchomienie lokalne

1. Zainstaluj wymagania:
   pip install -r requirements.txt

2. Uruchom serwer:
   uvicorn main:app --reload

3. Testuj na:
   http://localhost:8000/docs

## Autoryzacja

Do endpointa `/embed` wymagany jest nagłówek:
Authorization: Bearer <TOKEN>

Token ustaw w zmiennej środowiskowej `API_TOKEN`.
