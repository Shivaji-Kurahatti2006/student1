FROM python:3.10-slim
WORKDIR /app
COPY . .
CMD ["python", "student.py", "Shiva", "CSE", "3", "85", "90", "88"]
