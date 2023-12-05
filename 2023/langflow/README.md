## Intro

This project creates a FastAPI app to make queries using the
[LangChain](https://langchain.com/) service to query and summarize the answers
to the client (user).

## [Pyenv](https://github.com/pyenv/pyenv)

You can you pyenv if you will, you can run `pyenv install`.
The Python version is under `.python-version` file.


## [PDM - Package and dependency manager](https://pdm.fming.dev/latest/)

### Install PDM 

`pip install --user pdm`

### Install dependencies

`pdm install`

Add an `.env` file with the content `OPENAI_API_KEY=your_open_api_key`
(see `.env-example`).

## Run project in dev mode

Run `pdm run-dev`

Or the full command:

`pdm run uvicorn app.main:app --reload`

## Run requests against the project up running

1. Check the file `tests/end2end_tests/_test_main.py` to modify them.
2. You can change `json={"query": "what happened to SVB? Make a big text"}`
   To have your *query* test.
3. You can also print/icecream (`from icecream import ic`) the `response`.
4. Run it by `pdm run test tests/end2end_tests/_test_main.py`

## Unit tests

The unit tests are under `tests/`. You can test it using `pdm run test`.

## Summarization methods

I have searched for Summarization Methods using LangChain and I have found that
there are three basic methods to do it:
* `map_reduce` after splitting the text, each text is summarized (map),
   and all summaries are summarized again at the end (reduce).
* `stuff` it seems this summarizes all the text instead of summarizing each separated text.
* `refine` each split text is summarized, but each previous
   text is used for the next text to be summarized. Something similar
   to a `fold` method from the functional programming paradigm.

I chose the `map_reduce` randomly this time, but we can experiment with other methods.

## Possible future improvements

* **SummaryService** can take too long to complete the `get_summary` call.
  We could do it async: e.g. returning a unique key to the client, and then
  the client could request using this key in the future.
* Add [Ruff](https://beta.ruff.rs/docs/) as a Python linter.
* Add [black](https://github.com/psf/black) as a Python formatter.

## Contact

allainclair@gmail.com
