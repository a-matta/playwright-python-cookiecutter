# Playwright Python Cookiecutter

A [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/README.html) (project template) for playwright testing project.

## Usage

Make sure you have [`cruft`](https://github.com/cruft/cruft#installation) installed.

> Alternatively, you can use [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/installation.html) if you are not interested in getting updates to the project "boilerplate" in the future.

Create a new project:

```sh
cruft create https://github.com/a-matta/playwright-python-cookiecutter
```

The CLI interface will ask some basic questions, such the name of the project, and then generate the project automatically.

After that you can make it a proper git repo:

```sh
cd <your-project-slug>
git init
git add .
git commit -m "Initial project structure from Wolt Python Package cookiecutter"
```

If the project template is updated, you can get the updates into your project with:

```sh
cruft update
```