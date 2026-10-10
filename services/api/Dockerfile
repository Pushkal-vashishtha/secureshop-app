FROM cgr.dev/chainguard/python:latest-dev@sha256:47b1a23ae387fc1d5264abd79c395827fcca7ef92afe086908b51ce0747e8e77 AS build
WORKDIR /app
RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir --require-hashes --only-binary :all: -r requirements.txt && pip uninstall -y pip

FROM cgr.dev/chainguard/python:latest@sha256:c26e4957fef58d936401b8e2bb9ccb6db0f404f51597a0d2c7586e1d0112df0a
WORKDIR /app
ENV PATH="/app/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
COPY --from=build /app/venv /app/venv
COPY app/ ./app/
EXPOSE 8080
USER 65532
ENTRYPOINT ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
