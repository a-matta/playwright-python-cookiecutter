# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

---

*Documentation**: [https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug}}](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug}})

**Source Code**: [https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})

---

## Development

* Requirements:
  * [Poetry](https://python-poetry.org/)
  * Python 3.12+
* Clone this repository
* Create a virtual environment and activate it
  ```sh
  poetry shell
  ```
* Install the dependencies
  ```sh
  poetry install
  ```

## Running the Tests

```sh
# Uses PyInvoke
inv tests
```

---

This project was generated using the [playwright-python-cookiecutter](https://github.com/a-matta/playwright-python-cookiecutter) template.
