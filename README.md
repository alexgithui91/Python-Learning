# Python Learning
Quick lesson references I use when teaching beginners coding.

- Start by creating a Virtual Environment. Makes it easy to keep track of Python package installs.

  - **python3 -m venv /path/to/folder/venv**

- Keeping Python code in PEP8 format is coding Pythonic Standard. I normally use autopep8. A nifty tool which automatically formats the code for you.

  - ```python
    pip install --upgrade autopep8
    autopep8 --in-place --aggressive --aggressive <filename>
    ```

- To keep passwords safe we can make use of python-dotenv. This allows you to store passwords in a .env file which should be added to the .gitignore file.

  - ```python
    pip install -U python-dotenv
    ```

  - ```python
    from dotenv import load_dotenv
    load_dotenv()
    ```

    