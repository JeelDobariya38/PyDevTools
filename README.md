[![RunPytest](https://github.com/JeelDobariya38/PyDevTools/actions/workflows/%20test-code.yml/badge.svg)](https://github.com/JeelDobariya38/PyDevTools/actions/workflows/%20test-code.yml) [![Code Quality Check](https://github.com/JeelDobariya38/PyDevTools/actions/workflows/code-quality-check.yml/badge.svg)](https://github.com/JeelDobariya38/PyDevTools/actions/workflows/code-quality-check.yml)

# PyDevTools - Simplifying Python Development

"PyDevTools" is a versatile utility package designed to streamline various aspects of Python development. Whether you're working on mathematical computations, managing input/output, handling files, or organizing data collections, "PyDevTools" has you covered.

## Features

- **Math:** Mathematical operations made easy with a range of functions and utilities.
- **Input:** Simplify user input handling and validation.
- **Output:** Format and display output effectively for improved readability.
- **FileManager:** Efficiently manage files and directories with convenience.
- **Collection:** Tools to work with data collections and structures.
- **Database:** Interact with databases seamlessly.

## Installation

### Installing a Latest Code

1. To use "PyDevTools" in your project, you can install it via pip:

   ```bash
   pip install git+https://github.com/JeelDobariya38/PyDevTools.git
   ```

### Installing a Specific Release

If you want to install a specific release of PyDevTools, you can follow these steps:

1. Visit the [Releases](https://github.com/JeelDobariya38/PyDevTools/releases) page on GitHub.

2. Browse through the list of releases to find the version you want to install.

3. Once you've identified the desired release, look for the tag associated with it (e.g., `v1.0.0`).

4. Use the following command to install the specific release using pip:

   ```bash
   pip install git+https://github.com/JeelDobariya38/PyDevTools.git@<tag>
   ```
   **Note**: don't forget to replace the `<tag>` with actual tag

## Updating

To update "PyDevTools" to the latest version, run:

```bash
pip install --upgrade git+https://github.com/JeelDobariya38/PyDevTools.git
```

## Uninstalling

To uninstall "PyDevTools," use the following command:

```bash
pip uninstall pydevtools
```

## Usage

Here's a quick example of how to use the "PyDevTools" package:

```python
# Import the math module from PyDevTools
from pydevtools.math import math

# Use a function from the math module
result = math.add(5, 3)
print(result)  # Output: 8
```

For detailed information on each module and its functions, please refer to the [documentation](https://jeeldobariya38.github.io/PyDevTools/).

## Contributing

Contributions to "PyDevTools" are welcome! If you have ideas for improvements, bug fixes, or new features, please feel free to submit a [pull request](https://github.com/JeelDobariya38/PyDevTools/pulls) or open a new [issue](https://github.com/JeelDobariya38/PyDevTools/issues) in the repository.

## Code of Conduct

Please review our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing to the project.

## License

This project is licensed under the [MIT License](LICENSE.txt).
