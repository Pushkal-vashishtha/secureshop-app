FROM cgr.dev/chainguard/python:latest-dev@sha256:83933e374c3c3250e5b1b5dcde789a2d4a7314b771618b5548adab01c54066a0 AS build
WORKDIR /app
RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM cgr.dev/chainguard/python:latest@sha256:38ba1cbf71702bacc5f5be22ea41e3d4ad1bfb2565413b0caf4bafde38e831f2
WORKDIR /app
ENV PATH="/app/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
COPY --from=build /app/venv /app/venv
COPY app/ ./app/
EXPOSE 8080
ENTRYPOINT ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
