FROM nvidia/cuda:12.3.1-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y cmake ninja-build libboost-dev g++ build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev git

RUN curl https://pyenv.run | bash \
    && (echo 'export PYENV_ROOT="$HOME/.pyenv"'; echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"'; echo 'eval "$(pyenv init -)"') >> ~/.bashrc \
    && source ~/.bashrc

RUN pyenv install 3.12 \
    && pyenv virtualenv qulacs 3.12
