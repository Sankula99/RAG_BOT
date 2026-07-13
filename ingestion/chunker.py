from ingestion.loader import load_pdf
from config.settings import CHUNK_OVERLAP, CHUNK_SIZE
# To split text from loader.py into smaller chunks for better processing by LLMs, we can create a chunking function. This function will take the extracted text and split it into manageable pieces based on a specified chunk size.
def chunk_text(text, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP):
    """Splits the input text into chunks of a specified size."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - chunk_overlap
    return chunks
