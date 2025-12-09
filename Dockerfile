FROM python:3.10
COPY calc.py .
CMD ["python", "calc.py"]