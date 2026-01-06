FROM mcr.microsoft.com/devcontainers/python:3.12-bookworm

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends postgresql-client redis-tools \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*