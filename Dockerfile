FROM public.ecr.aws/lambda/python:3.10

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy app
COPY main.py .

# Lambda handler
CMD ["main.handler"]
