# Bulk Certificate Generator

A Python script that generates personalized PDF certificates in bulk from a template, using a list of names from a CSV file.

## Features

- Generates individual PDF certificates from a template
- Supports custom fonts (includes Dancing Script font)
- Centers text automatically on the certificate
- Processes multiple names from a CSV file
- Maintains original certificate template quality
- Outputs named PDFs in a dedicated folder

## Prerequisites

- Python 3.x
- Required Python packages (install using requirements.txt)

## Installation

1. Clone this repository or download the files
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Project Structure

```
bulk-certificate-generator/
├── certificate.pdf       # Your certificate template
├── main.py              # Main script
├── requirements.txt     # Python dependencies
├── students.csv         # List of names
├── fonts/              # Custom fonts directory
│   └── DancingScript-Bold.ttf
└── output/             # Generated certificates
```

## Usage

1. Prepare your files:

   - Place your certificate template PDF as `certificate.pdf` in the root directory
   - Create a CSV file named `students.csv` with a column named "name" containing the list of names
   - Ensure the fonts are in the `fonts/` directory

2. Format your CSV file:

   ```csv
   name
   John Doe
   Jane Smith
   ```

3. Run the script:

   ```bash
   python main.py
   ```

4. Find the generated certificates in the `output/` directory, named as `FIRSTNAME_LASTNAME.pdf`

## Customization

You can modify the following in `main.py`:

- Font size (default: 46)
- Text position (default y-coordinate: 300)
- Text color (default: black)
- Font style (default: DancingScript-Bold)

To help with positioning, uncomment the `draw_grid()` function call to show coordinate grid lines on the certificate.

## Dependencies

- pandas: Data handling and CSV reading
- reportlab: PDF generation and text manipulation
- PyPDF2: PDF merging and template handling
- Python standard libraries

## Notes

- The script automatically centers text horizontally on the certificate
- Names are automatically converted to title case
