from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PDFFile, ChatHistory
from langchain_module.langchain_functions import process_pdf_and_get_answer


def chat(request, pdf_id):
    # Get the PDF object and chat history
    pdf_obj = PDFFile.objects.get(id=pdf_id)
    chat_history = ChatHistory.objects.filter(pdf_file=pdf_obj)

    response = ""  # Initialize the response variable

    if request.method == 'POST':
        question = request.POST['question']

        # Replace this with your actual code to interact with your LLM model
        response = your_model_function(pdf_obj.file.path, question, your_llm_model)

        # Save the question and answer to chat history
        chat_history.create(question=question, answer=response, pdf_file=pdf_obj)

    return render(request, 'chat.html', {'pdf_obj': pdf_obj, 'chat_history': chat_history, 'response': response})

def upload_pdf(request):
    if request.method == 'POST':
        pdf_file = request.FILES.get('pdf_file')
        if pdf_file:
            pdf_obj = PDFFile(file=pdf_file)
            pdf_obj.save()
            return redirect('chat', pdf_id=pdf_obj.id)
    return render(request, 'upload_pdf.html')

def chat(request, pdf_id):
    pdf_obj = PDFFile.objects.get(id=pdf_id)
    chat_history = ChatHistory.objects.filter(pdf_file=pdf_obj)

    response = ""  # Initialize the response variable

    if request.method == 'POST':
        question = request.POST['question']
        response = process_pdf_and_get_answer(pdf_obj.file.path, question)  # Use the imported function

        chat_history.create(question=question, answer=response, pdf_file=pdf_obj)

    return render(request, 'chat.html', {'pdf_obj': pdf_obj, 'chat_history': chat_history, 'response': response})
    