import pathlib
import subprocess
from importlib.metadata import version

from invoke import task

ROOT = pathlib.Path(__file__).parent.resolve().as_posix()
VERSION = version("{{cookiecutter.project_slug}}")


@task
def clean(context):
    cmd = [
        "rm",
        "-rf",
        f"{ROOT}/.pytest_cache",
        f"{ROOT}/pytest.log",
        f"{ROOT}/report",
        f"{ROOT}/test-results",
    ]
    subprocess.run(" ".join(cmd), shell=True, check=False)


@task(pre=[clean])
def tests(context, headed=False, browser="chromium", video=False):
    cmd = [
        "pytest",
        "--headed" if headed else "",
        f"--browser {browser}",
        "--video=retain-on-failure" if video else "",
        f"{ROOT}/tests",
    ]
    subprocess.run(" ".join(cmd), shell=True, check=True)
