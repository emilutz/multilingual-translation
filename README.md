# multilingual-translation
A multilingual translation application using LLM

## Building the image

Creating the requirements file using `uv`:
```bash
python3 -m venv .venv
source venv/bin/activate
pip install uv
uv pip compile requirements.txt -o requirements.lock
```

Running a docker container:
```bash
docker compose --profile dev up -d app-shell
docker compose exec app-shell bash
```