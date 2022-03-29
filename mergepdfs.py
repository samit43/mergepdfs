from PyPDF2 import PdfFileReader, PdfFileWriter
import click

@click.command()
@click.option("-o", "--output", type=click.File("wb"), required=True, nargs=1)
@click.argument("inputs", type=click.File("rb"), nargs=-1)
def cli(inputs, output):
    """Merge PDFs."""
    # thnx https://realpython.com/pdf-python/#how-to-merge-pdfs
    pdf_writer = PdfFileWriter()

    for f in inputs:
        pdf_reader = PdfFileReader(f)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    pdf_writer.write(output)
