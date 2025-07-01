# document_export.py
from io import BytesIO
from fpdf import FPDF

class NotesPDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 14)
        self.cell(0, 10, "Study Notes", ln=True, align='C')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font("Arial", size=12)
        for line in body.split('\n'):
            self.multi_cell(0, 10, line)
            self.ln(0.5)

def save_notes_as_pdf(notes):
    pdf = NotesPDF()
    pdf.add_page()
    pdf.chapter_body(notes)
    
    # Convert to bytes and return
    pdf_bytes = pdf.output(dest='S').encode('latin1')  # Required for non-ASCII
    return BytesIO(pdf_bytes)
