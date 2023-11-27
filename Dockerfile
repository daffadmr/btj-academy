FROM python:latest

WORKDIR /app

COPY . .

CMD ["python", "todo_list.py"]