FROM python:3.11-slim

# Create a system user to avoid running as root
RUN useradd -m myuser
USER myuser
WORKDIR /home/myuser/app

COPY --chown=myuser:myuser requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Ensure the local bin is in PATH
ENV PATH="/home/myuser/.local/bin:${PATH}"

COPY --chown=myuser:myuser . .

EXPOSE 5000
CMD ["python", "app.py"]
