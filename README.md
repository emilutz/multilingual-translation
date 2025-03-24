# multilingual-translation
This is a multilingual translation application based on HuggingFace transformer models.

## How to run

### [Optional] Create the requirements file
 
First you need to build the docker image that contains all the dependencies for the application. These are currently stored in `requirements.lock`, so you don't need to recompute them, but in case you want to add new ones, these are the steps:

1. Modify `requirements.txt` to include everything the app needs.
2. Lock the versions of the dependencies using `uv`. It is recommended to do this in a virtual environment like this (this assumes you already havy python 3 installed locally):
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install uv
    uv pip compile requirements.txt -o requirements.lock
    ```

### Build and run a docker container

You can use the `docker compose` command which will automatically build an image for you if not already done locally.

We will first try to run the app in interactive mode.
```bash
docker compose --profile dev up -d app-shell
docker compose exec app-shell bash
```

Now, inside the container you can run the app using the command:
```bash
python src/interactive.py --source-language ENGLISH --target-language PORTUGUESE
```

This will prompt you to input a sentence in English and will provide the Portuguese translation on the following line:
```
Input a sentence to be translated or 'quit'/'exit' to stop the program.
(en)> I had a lot of fun doing this interview assignment this week.
(pt): Eu tive muita diversão fazendo esta entrevista tarefa esta semana.
```

> :information_source:
> You can also switch to using a different translator like Google Translator for example by passing `--translator-name=google` to the `src/interactive.py` script.

### Run translation in "production" mode

Another endpoint of this application is to perform translation based on input and output files. For this you have to run the `src/main.py` script. Let's try to do that using `docker compose`, but in the "normal application service" this time.

So, from outside the docker container:
```bash
docker compose --profile prod up app
docker compose run app python src/main.py \
  --source-language SPANISH \
  --target-language ENGLISH \
  --input-file data/news_article_es.txt \
  --output-file data/news_article_en.txt
```

You should now see a `data/news_article_en.txt` file with the content translated from Spanish. 
