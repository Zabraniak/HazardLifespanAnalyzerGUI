# Hazard and Lifespan Analyzer

![Python](https://img.shields.io/badge/python-v3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Info](#info)

## Description

The **Hazard and Lifespan Analyzer** is a Python application that performs life table analysis on survival data and presents the results using interactive graphical visualizations. It utilizes the `pandas` library for data manipulation, `matplotlib` for plotting, and `PyQt5` for creating the graphical user interface (GUI).

## Features

- Load survival data from Excel files.
- Conduct life table analysis to calculate survival probabilities and hazard functions.
- Display interactive plots of survival distribution and hazard function over time.
- User-friendly GUI for easy interaction and analysis.

## Prerequisites

Before running the application, you'll need to have the following installed:

- Python 3.x
- `pandas` library
- `matplotlib` library
- `PyQt5` library

You can install the required libraries using the following command:

```bash
pip install pandas matplotlib PyQt5
```

IMPORTANT: It's built to work on certain data structures - it isn't rocket science that will change the way we see the various industries. The test data is provided.

## Usage

1. Clone the repository:

   ```sh
   git clone https://github.com/Zabraniak/HazardLifespanAnalyzerGUI.git

2. Navigate to the repository folder.

3. Run the application:

   ```sh
   python filename.py

The GUI window will appear. Click the "Analyze the file" button to select an Excel file containing survival data for analysis.
The application will generate interactive plots showing the survival distribution and hazard function over time.

## Screenshots
![HazardLifespanAnalyzerMENU](https://i.imgur.com/HHhxecD.png)
![HazardLifespanAnalyzerOUTPUT](https://i.imgur.com/SkjUtw6.png)

## Contributing
Contributions are welcome! If you have any improvements or new features to add, feel free to fork this repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License.

## Info
This project was inspired by the need for an easy-to-use tool for life table analysis and visualization of survival data.
