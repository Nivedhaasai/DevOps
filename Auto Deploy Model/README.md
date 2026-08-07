# Auto Deploy Model

Same house price model from
my mlflow and docker labs, but now it trains and deploys by itself using
github actions. Every time i push a change to this folder, it retrains the
model, checks if it is good enough, and if it is, sends it straight to my
hugging face account. No manual steps.

## How it works

```
i push code to github
        |
        v
   run tests (pytest)
        |
        v
   prepare data -> train model -> check r2 score
        |
        v
   if r2 is good enough and this was a push to main
        |
        v
   push model to hugging face
```

If the r2 score is too low, the pipeline just stops there. Nothing gets
pushed to hugging face. This is on purpose, so a bad model never goes live
by accident.

## What is in here

- `params.yaml` - all the settings, including the minimum r2 score allowed
- `src/prepare.py` - loads california housing data, splits into train and test
- `src/train.py` - trains an xgboost regressor, same settings as my mlflow lab
- `src/evaluate.py` - checks r2 score, this is the quality gate
- `src/register.py` - uploads the model to hugging face
- `tests/test_pipeline.py` - basic sanity tests
- `.github/workflows/huggingface.yml` - the actual github actions workflow (this file lives at the repo root since that is where github actions needs it, but it only runs when something in this folder changes)

## Setup i did

### 1. made a hugging face account and a token
Went to huggingface.co/settings/tokens and made a token with write access.

### 2. added the token as a github secret
In the DevOps repo settings, Secrets and variables, Actions, New repository secret.
- Name: `HF_TOKEN`
- Value: the token from step 1

### 3. added the target repo name as a github variable
Same page, Variables tab, New repository variable.
- Name: `HF_REPO_ID`
- Value: `<my-hf-username>/house-price-regression`

### 4. pushed to main
That is it, the workflow runs by itself now. I can check the Actions tab
on github to see it running, and once it finishes the model shows up at
`https://huggingface.co/<my-hf-username>/house-price-regression`

## Changing the quality gate

The `evaluate.min_r2` value in `params.yaml` decides how good the model
needs to be before it gets deployed. Right now it is set comfortably below
what the model actually scores (around 0.84), so there is room before it
would ever fail.

## Running it on my own computer first

```bash
pip install -r requirements.txt
python src/prepare.py
python src/train.py
python src/evaluate.py
cat metrics.json
```
