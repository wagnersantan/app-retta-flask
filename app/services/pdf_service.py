from reportlab.pdfgen import canvas
import uuid

def gerar_pdf(nome, produto):

    arquivo = f"pdfs/{uuid.uuid4()}.pdf"

    c = canvas.Canvas(arquivo)

    c.drawString(100, 750, "Solicitação de Produto")
    c.drawString(100, 720, f"Cliente: {nome}")
    c.drawString(100, 700, f"Produto: {produto}")

    c.save()

    return arquivo