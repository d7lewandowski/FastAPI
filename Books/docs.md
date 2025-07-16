To activate env:
source .fastapivenv/bin/activate

uvicorn main:app --host 0.0.0.0 --port 8

uvicorn books:app --reaload # to have active UI Swagger during development