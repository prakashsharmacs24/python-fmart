# Here is the build image
FROM python:3.8.0-slim as builder
RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean
COPY requirements.pip /app/requirements.pip
WORKDIR app
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --user -r requirements.pip
COPY . /app
# Here is the production image
FROM python:3.8.0-slim as app
WORKDIR app
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app/main.py .
COPY --from=builder /app/cart /app/cart

ENV PATH=/root/.local/bin:$PATH

CMD ["python", "main.py"]
