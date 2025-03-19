# Demonstração de integração do ollama em python.

Rode o seguinte comando para baixar as dependências necessárias:

```
pip install fastapi uvicorn requests
```

Após isso, rode este comando para subir a aplicação:

```
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Assim fácil, a aplicação estará rodando na porta 8000!

Você pode fazer uma requisição seguindo este modelo:

```
curl --location --request POST 'http://127.0.0.1:8000/generate' \
--header 'Content-Type: application/json' \
--data '{
  "prompt": "Explique o que é uma LLM",
  "model": "llama3.2"
}'
```
