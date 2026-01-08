FROM python:3.14-slim
WORKDIR /app
COPY . .
CMD ["python", "student_grade.py"]
