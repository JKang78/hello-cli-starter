# hello-cli-starter

A zero-setup Python CLI starter you can **push to GitHub** in minutes.

## What it does
- Provides a `hello` command that greets a name.
- Includes tests, linting, and type checks.
- Comes with GitHub Actions CI (runs on each push).
- Packaged with `pyproject.toml` (PEP 621).

## Quickstart

### 1) Open a terminal in this folder
If you downloaded a ZIP, unzip it and open a terminal **inside** `hello-cli-starter`.

### 2) Create & activate a virtual env (recommended)
```bash
python -m venv .venv
# On macOS/Linux:
source .venv/bin/activate
# On Windows (PowerShell):
.venv\Scripts\Activate.ps1
```

### 3) Install the package (editable) + dev tools
```bash
pip install -e ".[dev]"
```

### 4) Run the CLI
```bash
hello --name "Junha"
```

### 5) Run tests
```bash
pytest -q
```

### 6) Type-check and lint
```bash
mypy src
ruff check src tests
```

### 7) Initialize a local Git repo and make your first commit
```bash
git init
git add -A
git commit -m "Initial commit: hello-cli-starter"
```

### 8) Create a new GitHub repo and push
- Go to GitHub → New Repository → name it **hello-cli-starter** (or anything).
- Then run (replace `<YOUR_GITHUB_USERNAME>` and, if needed, repo name):

```bash
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/hello-cli-starter.git
git push -u origin main
```

> Tip: If you use SSH instead of HTTPS, use the `git@github.com:...` URL.

---

## Project layout

```
hello-cli-starter/
├─ src/
│  └─ hello_cli/
│     ├─ __init__.py
│     └─ main.py
├─ tests/
│  └─ test_main.py
├─ .github/
│  └─ workflows/
│     └─ ci.yml
├─ pyproject.toml
├─ .gitignore
└─ README.md
```

## Customize
- Edit `src/hello_cli/main.py` to add features.
- Change the CLI name by editing the `console_scripts` entry in `pyproject.toml`.
- Add dependencies under `[project.optional-dependencies]` or `[project.dependencies]`.

## FAQ

**I can't code—can I still use this?**  
Yes. You can run it as-is, and I can expand it for you. Tell me what you want the tool to do.

**Can this become a web app later?**  
Absolutely. We can add FastAPI/Flask and a simple frontend if you want.

---

Made for you ✨
