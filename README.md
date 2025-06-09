# 📈 Stock Portfolio Tracker (CLI Edition)

This is a command-line based **Stock Portfolio Tracker** written in Python. It allows users to enter stock symbols and quantities, calculates total investment, and provides the option to save the summary as a `.csv` and as an image.

---

## 🚀 Features

- 🧠 Simple CLI interface for entering stocks
- 🧮 Auto-calculates total investment value
- 🖼️ Generates a **summary table image** using `matplotlib`
- 💾 Option to save results as `.csv` and `.png` in the same folder
- ❓ Asks user before saving or showing anything

---

## 🛠️ Technologies Used

- Python 3
- `pandas` for table handling
- `matplotlib` for image generation

---

## 📦 Installation

```bash
pip install pandas matplotlib
```

## How to Use
- Run the script:
```bash
python main.py
```
- Follow the prompts:
Enter stock symbols like AAPL, GOOGL, etc.
Type done to finish input
View the summary in the terminal
Choose to view/save the portfolio image and CSV

## 📁 Output Files
If you choose to save the data, the following files will be created in the same folder:
```
portfolio_summary_YYYY-MM-DD_HH-MM-SS.csv
portfolio_summary_YYYY-MM-DD_HH-MM-SS.png
```
