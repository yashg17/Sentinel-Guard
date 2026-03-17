FROM python:3.11-slim
WORKDIR /app

# Copy ONLY requirements first
COPY requirements.txt .

# Install dependencies - this is now cached and won't rerun unless requirements change
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code LAST
COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
