Towel Data Visualizer

<img width="502" alt="Screen Shot 2024-10-08 at 12 05 00 AM" src="https://github.com/user-attachments/assets/ee70144e-e021-481e-9886-a846d6a4c6a2">

The dataset I used as an example in these pictures is from this kaggle dataset:
https://www.kaggle.com/datasets/lainguyn123/student-performance-factors?resource=download

<img width="648" alt="Screen Shot 2024-10-08 at 12 04 36 AM" src="https://github.com/user-attachments/assets/fc17dd64-ee9d-49f2-8c6b-f9309382f3bd">

This tool is designed to provide a user-friendly interface for visualizing data from CSV files through various types of plots, such as histograms, scatter plots, box plots, and correlation heatmaps.

📈 Features

Browse and Load: Easily load your CSV files using a file dialog.
Visualization Options: Select from a range of plot types to visualize your data effectively.
Interactive GUI: Simple and interactive graphical user interface built with Tkinter.


📦 Dependencies

This project uses several Python libraries to handle data manipulation and visualization:

matplotlib: For creating static, interactive, and animated visualizations in Python.
pandas: Provides high-performance, easy-to-use data structures and data analysis tools.
seaborn: A Python visualization library based on matplotlib, providing a high-level interface for drawing attractive statistical graphics.
tkinter: Standard GUI toolkit in Python, used for building the application interface.
six: Provides utility functions for smoothing over differences between Python 2 and Python 3. Used indirectly through other dependencies.


🖥️ Running the Application

To run Towel Data Visualizer on your machine, follow these steps:

Ensure you have Python installed. This application requires Python 3.6 or higher.

Clone the repository or download the source code:
git clone https://github.com/towelWet/Towel-Data-Visualizer.git

cd Towel-Data-Visualizer

Install the required Python libraries:
pip install -r requirements.txt

Run the application:
python app.py


🔨 Compiling the Application

Windows

To compile the application into a standalone executable on Windows:

Install PyInstaller:
pip install pyinstaller
Navigate to the application directory and run PyInstaller:
pyinstaller --onefile --windowed --icon=icon.ico app.py
The executable will be located in the dist directory.

macOS

To compile the application into a .app on macOS:

Install PyInstaller:
pip install pyinstaller
Run PyInstaller with the following command:
pyinstaller --onefile --windowed --icon=icon.icns app.py
The application bundle will be in the dist directory.

📂 Releases

You can find the latest precompiled binaries for Windows (.exe) and macOS (.app) in the Releases section of this repository.
