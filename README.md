# Contributing to WhereCanWeGo

## Getting Started
1. Fork and clone:
```sh
git clone https://github.com/444B/wherecanwego.git
cd wherecanwego
```
2. Create branch:
```sh
git checkout -b your-feature-name
```

## Development Environment Setup
1. Install Python 3.10.x
2. Install and setup uv:
```sh
pip install uv
uv venv .venv --python 3.10
source .venv/bin/activate
```
3. Install dependencies:
```sh
uv pip install -e ".[dev]"
uv sync
```
4. Run the app:
```sh
streamlit run main.py
```
5. If you need to add a package:
```sh
uv add <package-name>
```

## Pull Request Process

1. Push changes:
```sh
git add .
git commit -m "Your commit message"
git push origin your-feature-name
```
2. Open PR on GitHub

For issues: [GitHub issue tracker](https://github.com/444B/wherecanwego/issues/new/choose)
