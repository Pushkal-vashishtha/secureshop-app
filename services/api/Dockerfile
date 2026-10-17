FROM cgr.dev/chainguard/python:latest-dev@sha256:678b051d9daf61ab6c1eaad7f7eb7426e612a99b655b715a639a6f898318a6e7 AS build
WORKDIR /app
RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir --require-hashes --only-binary :all: -r requirements.txt && pip uninstall -y pip

FROM cgr.dev/chainguard/python:latest@sha256:d0a0ef8759e4da134c9848b9bba9aa9b7fec345427f093f1a37ca02434e685d8
WORKDIR /app
ENV PATH="/app/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
COPY --from=build /app/venv /app/venv
COPY app/ ./app/
EXPOSE 8080
USER 65532
ENTRYPOINT ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
