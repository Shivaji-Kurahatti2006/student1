FROM python:3.14-slim
WORKDIR docker/student
COPY . .
CMD ["python","student.py"]