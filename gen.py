import io
import textwrap

from PyPDF2 import PdfFileWriter, PdfFileReader

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor

# Reads names from names.txt
def getNames():
  f = open("Input/names.txt")
  return f.read().split('\n')

# Reads msg from msg.txt
def getMsg():
  f = open("Input/msg.txt")
  return f.read()

# Registers the fonts to use later
def registerFont():
  pdfmetrics.registerFont(TTFont('DIN', 'Fonts/DINCondensed-Bold.ttf'))
  pdfmetrics.registerFont(TTFont('Roboto', 'Fonts/Roboto-Italic.ttf'))

names = getNames()
message = getMsg()

# Source for pdf writing code: Stack Overflow

registerFont()

for name in names:
  packet = io.BytesIO()
  can = canvas.Canvas(packet, pagesize=letter)
  
  # Write the name
  can.setFont("DIN", 48, leading = None)
  can.drawString(270, 260, name.upper())
  
  # Write the msg
  can.setFont("Roboto", 20, leading = None)
  can.setFillColor(HexColor('#1d1d1d'))
  for i in range(int(len(message) / 45) + 1):
    can.drawString(272, 209 - (22*i), textwrap.wrap(message, width=45)[i])
  can.save()

  # Move to the beginning of the StringIO buffer
  packet.seek(0)
  new_pdf = PdfFileReader(packet)

  # Read your existing PDF
  existing_pdf = PdfFileReader(open("Sample.pdf", "rb"))
  output = PdfFileWriter()

  # Add the "watermark" (which is the new pdf) on the existing page
  page = existing_pdf.getPage(0)
  page.mergePage(new_pdf.getPage(0))
  output.addPage(page)

  # Finally, write "output" to a real file
  outputStream = open("Generated/" + name + ".pdf", "wb")
  output.write(outputStream)
  outputStream.close()

