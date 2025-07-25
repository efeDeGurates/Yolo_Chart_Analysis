# YOLOv8 Candlestick Detector for Screen Images

This project captures your screen, processes the screenshot using a trained object detection model,
and identifies stock-related visual elements. It is built using Python and runs directly in the terminal.

## Features

- Automatically captures the screen at intervals
- Performs real-time object detection
- Trained on the **StockObjects** dataset from Roboflow

## Requirements

- Python 3.8 or higher must be installed
- Required packages:
  ```bash
  pip install -r requirements.txt
  ```

## How to Run

1. Open your terminal
2. Navigate to the project folder:
   ```bash
   cd path/to/project
   ```
3. Run the main file:
   ```bash
   python runner.py
   ```

## Dataset License

This project uses the [StockObjects dataset](https://universe.roboflow.com/stock-trends/stock-trends) provided by Bradley Blackwood via Roboflow.  
The dataset is licensed under the **CC BY 4.0** license.

> Attribution: Dataset by Bradley Blackwood via Roboflow (CC BY 4.0)

## Notes

- Since the script captures your screen, your antivirus (e.g., Windows Defender) may prompt for permission.
- Ensure you're not running screen-sensitive apps in the background for best performance.
