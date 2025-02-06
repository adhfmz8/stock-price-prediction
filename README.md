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
