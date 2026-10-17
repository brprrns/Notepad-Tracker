import subprocess
from pathlib import Path


def run_git_command(command, working_directory):
    result = subprocess.run(
        command,
        cwd=working_directory,
        capture_output=True,
        text=True,
        check=False,
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())

    return result.stdout.strip()


def initialize_git(directory):
    directory = Path(directory)

    git_directory = directory / ".git"

    if not git_directory.exists():
        run_git_command(
            ["git", "init"],
            directory,
        )


def commit_file(file_path):
    file_path = Path(file_path)
    directory = file_path.parent

    initialize_git(directory)

    run_git_command(
        ["git", "add", file_path.name],
        directory,
    )

    run_git_command(
        [
            "git",
            "commit",
            "-m",
            f"Update {file_path.name}",
        ],
        directory,
    )