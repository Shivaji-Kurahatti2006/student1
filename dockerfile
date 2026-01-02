FROM python:3.10-slim

WORKDIR /app

COPY . /app

# Install dependencies
RUN pip install --no-cache-dir pytest

# Run pytest
ENTRYPOINT ["sh", "-c"]
CMD ["python student.py && pytest test_student.py"]