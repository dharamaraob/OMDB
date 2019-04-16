FROM python:3.7
WORKDIR /omdb
COPY . /omdb
RUN pip install -r /omdb/prerequisites.txt
ENTRYPOINT [ "python",   "omdb.py", "--movie" ]
CMD ["i"]