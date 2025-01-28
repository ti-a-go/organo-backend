FROM python:3.12

WORKDIR /organo

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["fastapi", "run", "src/main.py", "--port", "8000"]