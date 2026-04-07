# 📊 CSV to Excel Converter

A powerful and simple **Python CLI tool** to convert CSV files into Excel format (.xlsx) with built-in data cleaning and preprocessing.

---

## 🚀 Features

* 📂 Read CSV files efficiently
* 🧹 Handle missing values based on data types
* 📅 Automatic date parsing
* 🏷️ Column name normalization (clean & standardized)
* 💻 Command Line Interface (CLI) support
* 📝 Logging for tracking operations and errors
* ⚠️ Error handling for invalid or missing files

---

## 🛠️ Tech Stack

* Python
* pandas
* openpyxl
* argparse
* logging

---

## 📁 Project Structure

```
CSV-to-Excel-Converter/
│
├── converter.py       # Main script (CLI tool)
├── utils.py           # Data cleaning functions
├── sample.csv         # Sample input file
├── output.xlsx        # Generated output file
├── app.log            # Log file
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/CSV-to-Excel-Converter.git
cd CSV-to-Excel-Converter
```

2. Install dependencies:

```bash
pip install pandas openpyxl
```

---

## ▶️ Usage

Run the script using CLI:

```bash
python converter.py -i input.csv -o output.xlsx
```

### 🔹 Arguments

| Argument          | Description               |
| ----------------- | ------------------------- |
| `-i` / `--input`  | Path to input CSV file    |
| `-o` / `--output` | Path to output Excel file |

---

## 🧠 How It Works

1. Reads CSV file using pandas
2. Cleans data:

   * Missing values handled based on data type
   * Date columns parsed automatically
   * Column names standardized
3. Converts and exports data to Excel format using openpyxl
4. Logs all operations and errors

---

## 📌 Example

Input (`sample.csv`):

```
name, age, join date
Pratik, 20, 2023-01-10
Janhavi,, 2022-05-15
Sakshi, 22,
```

Output (`output.xlsx`):

* Missing values handled
* Dates formatted properly
* Clean column names

---

## ⚠️ Error Handling

* Handles missing file errors
* Logs unexpected issues in `app.log`
* Prevents crashes for invalid data formats

---

## 🔮 Future Enhancements

* Batch CSV to Excel conversion
* Custom column renaming via CLI
* GUI version using Tkinter
* Export to multiple formats (JSON, XLS, etc.)

---

## 👨‍💻 Author

**Pratik Chidrawar**
Python Developer | Data Enthusiast

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

