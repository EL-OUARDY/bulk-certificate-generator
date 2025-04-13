import pandas as pd
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.colors import Color

from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

csv_file = "./students.csv"
certificate_template = "./certificate.pdf"
output_dir = "./output"


def draw_grid(packet, page_width, page_height):
    """
    Draw a grid on the canvas to help with positioning.
    """
    packet.setFont("Helvetica", 8)
    packet.setStrokeColor("#cccccc")

    # Horizontal lines
    for y in range(0, int(page_height), 50):
        packet.line(0, y, page_width, y)
        packet.drawString(5, y + 2, str(y))  # Label the y-coordinates

    # Vertical lines
    for x in range(0, int(page_width), 50):
        packet.line(x, 0, x, page_height)
        packet.drawString(x + 2, 5, str(x))  # Label the x-coordinates


def hex_to_color(hex_color):
    """
    Convert a hex color string (e.g., '#FF5733') to a Color object.
    """
    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i : i + 2], 16) / 255.0 for i in (0, 2, 4))
    return Color(r, g, b)


def create_certificate(name: str):
    output_file = f"{output_dir}/{name.replace(' ', '_').upper()}.pdf"

    # Load the PDF template
    template = PdfReader(certificate_template)
    template_page = template.pages[0]
    page_width, page_height = (
        float(template_page.mediabox.width),
        float(template_page.mediabox.height),
    )

    # Create a new PDF canvas
    packet = canvas.Canvas(output_file, pagesize=(page_width, page_height))

    # Draw the grid to visualize coordinates
    # draw_grid(packet, page_width, page_height)

    # Register a custom font
    pdfmetrics.registerFont(
        TTFont("DancingScript-Bold", "./fonts/DancingScript-Bold.ttf")
    )

    font_name = "DancingScript-Bold"
    font_size = 46
    packet.setFont("DancingScript-Bold", font_size)

    # Calculate the x-coordinate for centering
    text_width = packet.stringWidth(name, font_name, font_size)
    x = (page_width - text_width) / 2  # Center horizontally

    # Specify the y-coordinate (adjust as needed for your template)
    y = 300

    # Set text color
    packet.setFillColor(hex_to_color("#000000"))

    # Write the name on the certificate
    packet.drawString(x, y, name.title())

    # Save the canvas
    packet.save()

    # Merge with the template
    output = PdfWriter()
    new_pdf = PdfReader(output_file)

    new_page = template_page
    new_page.merge_page(new_pdf.pages[0])
    output.add_page(new_page)

    # Save the final certificate
    with open(output_file, "wb") as final_certificate:
        output.write(final_certificate)


data = pd.read_csv(csv_file)
names = data["name"].tolist()

for name in names:
    create_certificate(name)
    print(f"Certificate created for {name}")
