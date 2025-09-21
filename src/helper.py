from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List
from langchain.schema import Document

# Extract text from PDF files
def load_pdf_file(data):
    loader = DirectoryLoader(
        data,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )

    documents =loader.load()
    return documents


def filter_doc(doc: List[Document]) -> List[Document]:
    """
    Give a list of document objects, returna new list of document objects
    containign only 'source' in metadat and the original page_content.
    """
    minimal_docs: List[Document] = []
    for doc in doc:
        src = doc.metadata.get("source")
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={"source": src}
            )
        )
    return minimal_docs    