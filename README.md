# stock-price-prediction

## For env setup

Install uv (macos and linux)
`curl -LsSf https://astral.sh/uv/install.sh | sh`

To sync your python env
`uv sync`

To add dependencies
`uv add [blah]`

Please test with /notebooks/test_your_env.ipynb

---

## For commits

Clean up notebooks before committing
`jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace notebooks/*.ipynb`

`nbdev_clean`

### How to open a PR

1. Create new branch
`git checkout -b feature/model-training`

2. Make changes and commit
`git add my_script.py`
`git commit -m "Added model training script"`

3. Push to github
`git push origin feature/model-training`

4. Open a PR

- Go to the GitHub repository.
- Click "Compare & pull request" next to the branch you pushed.
- Add a title and description.
- Click "Create pull request".
