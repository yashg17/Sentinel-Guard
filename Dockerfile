# Stage 1: Builder
FROM python:3.9-slim AS builder
WORKDIR /app
COPY requirements.txt .
# Install dependencies to a local folder
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Production
FROM python:3.9-slim
WORKDIR /app

# Copy only the installed dependencies and code
COPY --from=builder /root/.local /root/.local
COPY . .

# Update PATH to include the user-installed binaries
ENV PATH=/root/.local/bin:$PATH
ENV FLASK_ENV=production

EXPOSE 5000 8000
# Run the security miner and the app together using a shell
CMD python log_security.py & python app.py
