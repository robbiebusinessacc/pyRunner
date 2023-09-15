# pyRunner - MacOS Menu Bar Python File Runner

Execute Python files directly from the macOS menu bar with ease.

## Features:
- Integrate seamlessly with macOS menu bar.
- Dynamic listing of Python files in a specified directory.
- One-click file execution.
- Built using the AppKit library.

## Prerequisites:

Make sure to install the `PyObjC` package to access the AppKit framework. You can install it using pip:

```bash
pip install pyobjc
```

## Usage:

1. Place your Python files in the `./new` directory.
2. Run the `pyRunner` script.
3. A menu bar item labeled "File Runner" will appear.
4. Click on the menu bar item to see a list of Python files.
5. Select a file from the dropdown to execute it.

## Included Example:

In the `./new` directory, you will find an example named "slowType". This is a Python implementation that simulates human-like typing. For more details and source code, visit the [GitHub repository](https://github.com/robbiebusinessacc/slowPaste).

## Origin:

The `pyRunner` is an evolution of the original [fileLinker project](https://github.com/robbiebusinessacc/fileLinker) which is also developed by the same author (robbiebusinessacc).

## Script Breakdown:

- `MacOSMenuBar`: Main class handling the macOS menu bar interaction.
  - `__init__`: Initializes the menu bar item and its dropdown.
  - `fileLinker`: Adds Python files from the `./new` directory to the dropdown.
  - `runPythonFile_`: Handles the file execution.

## Contributing:

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Safety:

Always ensure that the Python files in the `./new` directory are safe to run, as they will be executed as-is.

## License:

[MIT](https://choosealicense.com/licenses/mit/)

