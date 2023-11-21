import pdfkit

# Yol Tanımlama
path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

# Html Yolu Tanımlama
path_html_file = "index.html"

# Pdf kit konfigürasyonu
config = pdfkit.configuration(wkhtmltopdf = path_to_wkhtmltopdf)

# Html pdf e çevirme
pdfkit.from_file(path_html_file, output_path='output.pdf', configuration=config)
