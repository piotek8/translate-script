FROM python:3.11

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

COPY . /app

CMD ["python", "main.py"]