FROM python:3.7.5
COPY . ./app
WORKDIR /app
EXPOSE 8000
RUN "./build.sh"
# ENTRYPOINT ["./start.sh"]
