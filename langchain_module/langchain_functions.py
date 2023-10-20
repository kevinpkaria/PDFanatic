# langchain_module/langchain_functions.py

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain import PromptTemplate, LLMChain
from langchain.callbacks import get_openai_callback
import pickle
from PyPDF2 import PdfReader
import os

os.environ["OPENAI_API_KEY"] = "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"

def process_pdf_and_get_answer(pdf_file_path, question):
    pdf_reader = PdfReader(pdf_file_path)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text=text)

    store_name = pdf_file_path[:-4]  # Assuming pdf_file_path contains the name
    if os.path.exists(f"{store_name}.pkl"):
        with open(f"{store_name}.pkl", "rb") as f:
            VectorStore = pickle.load(f)
    else:
        embeddings = OpenAIEmbeddings()
        VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
        with open(f"{store_name}.pkl", "wb") as f:
            pickle.dump(VectorStore, f)

    docs = VectorStore.similarity_search(query=question, k=3)

    llm = OpenAI()
    template = """Question: {que}
                Answer: Read and understand {src} and give an answer to it."""
    prompt = PromptTemplate(input_variables=["que", "src"], template=template)
    chain = LLMChain(llm=llm, prompt=prompt, verbose=True)

    with get_openai_callback() as cb:
        response = chain.run({'que': question, 'src': docs})

    return response
