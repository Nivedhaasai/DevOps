# DevOps

Each folder is a separate lab, from lab 2 onwards they all build on the same house price
model, so the whole repo ends up telling one story: linux basics first,
then version the data, then track experiments, then serve the model, then
automate the whole thing.

## Labs, in order

### 1. linux_lab
Basic linux commands lab. Directory and file handling, a small csv of
students and what they are learning, some grep and text processing on
that file, a shell script that prints system info, and an environment
variable holding the course name. No readme in this one, its small enough
that the files speak for themselves, just `students.txt`, `script.sh` and
`output.txt`.

### 2. [DVC-ML-Pipeline-Regression](DVC-ML-Pipeline-Regression)
First MLOps lab. A regression pipeline (diabetes dataset, random forest)
built with DVC, so the dataset and the pipeline stages are versioned
alongside git instead of just the code. Covers dvc init, tracking the
data, and wiring up a dvc.yaml pipeline that can be reproduced with one
command.

### 3. [MLflow-101-Regression](MLflow-101-Regression)
Second MLOps lab, this is where the california housing model that shows
up in the rest of the repo comes from. Trains three different regression
models, logs every run to mlflow with its parameters and metrics, and
registers the best one. Done twice, once with a local mlflow server and
once logging straight to dagshub.

### 4. [Model Deployment](Model%20Deployment)
Takes the model from the mlflow lab and puts it behind a fastapi
prediction api, then packs that into a docker image. Built, ran, and
tested the container for real, and the image is pushed to docker hub.

### 5. [Auto Deploy Model](Auto%20Deploy%20Model)
Final MLOps lab. Same model again, but now the whole thing (prepare
data, train, check the r2 score, deploy) runs by itself through github
actions every time i push a change to this folder. If the model is not
good enough it just does not deploy, so nothing bad ever goes out
automatically. The workflow file itself lives at the repo root
(`.github/workflows/huggingface.yml`) since that is where github actions
looks for it, but it is scoped to only run when this folder changes.



- Each lab folder has its own readme with the actual setup steps and results
