# TACR_2022_Neurosky

The Neurosky recording tool.

# Structure

* src - Python source codes of the main project
* data_output - default directory for saving/loading Neurosky recordings
* requirements.txt - define Python dependencies of the project
* profile.yaml - configuration file
* run_neurosky_tool.bat - script for executing the application

# Running the tool
Requires Python 3.7.
Works with NeuroSky Mindwave Mobile 2.

To execute:
1. Directly run *run_neurosky_tool.bat* to install all dependencies and run the main application.
2. If all dependencies including this project are installed, go to *./src* and execute *python app.py*.

# Quick start
1. ThinkGear connector, Bluetooth module and pairing with the NeuroSky headset are prerequisities before running the app.
2. After clicking on the Start button, the connection is established and its status is shown in the status bar.
3. Once the status is 'connected', the data are stored into memory and shown in the GUI.
4. The variables shown can be changed by clicking on the variable checkboxes.
5. The data can be save using the Save button, or by stopping the recording if Autosave is enabled.

# Configuration file profile.yaml
* collected_metrics - Metrics that are stored into JSON file (could be all metrics), should correspond to GUI checkboxes.
* metrics_to_display - Metrics that will be shown in the plot
* samples_to_plot - Samples to be shown in the plot at once if 'Zobrazit cely signal' is unchecked
* output_dir - Directory to save output files
* subject_name, condition - Identification of recording (part of the output filename)

# Outputs
* stored in the output_dir (/data_output/ by default)
* in JSON and XLSX format
* reading of JSON in Python to Python dict
```python
import json

        with open(filename) as f:
            all_data = json.load(f)
```
