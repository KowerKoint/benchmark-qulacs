FROM nvidia/cuda:12.0.0-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV HOME /root
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/bin:$:$PATH

RUN apt-get update \
    && apt-get install -y cmake ninja-build libboost-dev g++ build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev git

RUN git clone https://github.com/pyenv/pyenv.git ~/.pyenv && \
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc
