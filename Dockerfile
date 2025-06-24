# ---- Base Image ----
FROM python:3.10-slim AS base

# Set working directory
WORKDIR /app

# Copy dependencies file first for layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ---- Final Image ----
FROM base AS final

# Copy the rest of the app
COPY . .

# Expose port (FastAPI default)
EXPOSE 8000

# Run with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
