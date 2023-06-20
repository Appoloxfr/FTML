# FTML project
    This is the FTML project of:
        - Nicolas Fidel
        - Timothée Strouk
        - Gabriel Huet De Froberville
        - Raphaël Mourot-Pelade
# Report
    The report source code is available in the report folder.
    You can find the report compiled in the `main-PDF` artifact of the last Action run. (Actions > Last worflow run > main-PDF)

# Workflow

    Please run pre-commit before pushing your code.

    Pre-commit will automaticly remove output cells when you commit your notebook in another branch than `main`.
    This will avoid conflic and keep the repository clean.

    To install pre-commit, run:
    `pip install pre-commit`

    Then, run:
    `pre-commit install`

    You can generate the output cells by running the script `generate_output_cells.py` in the `scripts` folder.