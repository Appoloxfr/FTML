# FTML project
    This is the FTML project of:
        - Nicolas Fidel
        - Timothée Strouk
        - Gabriel Huet De Froberville
        - Raphaël Mourot-Pelade
# Report
    The report source code is available in the report folder.
    You can find the report compiled in the `main-PDF` artifact of the last Action run. (Actions > Last worflow run > main-PDF)


# Project FTML

This project utilizes Poetry to manage dependencies. Poetry is a
dependency management and packaging tool for Python that helps ensure
consistent and reproducible environments.

To ensure that everything works correctly, it is recommended to use
Poetry. Follow the steps below to set up the project:

## Prerequisites
- Python 3.10 or higher
- Poetry installed (Installation instructions can be found at https://python-poetry.org/docs/#installation)

## Setup
1. Clone the project repository.
2. Navigate to the project directory.
3. Run the following command to install the project dependencies:
   ```
   poetry install
   ```

## Running the Project
To run the project, you can activate Poetry's virtual environment
using the `poetry shell` command. Run the following command: 
```
poetry shell
```

This will activate the project's virtual environment, allowing
you to directly run commands without the need to prefix them with
`poetry run`.

Alternatively, you can still use the `poetry run` command to run
specific Python scripts within the virtual environment:

```
poetry run python main.py
```

Using Poetry ensures that the project's dependencies are properly
managed and that the correct versions are installed. It creates a
separate virtual environment specifically for this project, isolating
it from other Python installations on your system.

By following these steps and utilizing Poetry, you can ensure a smooth
and consistent development experience for this project.

## Workflow

    Please run pre-commit before pushing your code.

    Pre-commit will automaticly remove output cells when you commit
    your notebook in another branch than `main`.  This will avoid
    conflic and keep the repository clean.

    To install pre-commit, run:
    `pip install pre-commit`

    Then, run:
    `pre-commit install`

    You can generate the output cells by running the script
    `generate_output_cells.py` in the `scripts` folder.
