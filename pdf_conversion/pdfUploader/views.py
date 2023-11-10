# pdfuploader/views.py
from django.shortcuts import render, redirect
from .models import PDFFile
from .forms import PDFFileForm
import fitz
import subprocess
from django.http import HttpResponse
from PIL import Image
import pytesseract

def convert_pdf_to_text(pdf_path, request):
    try:
        # Replace 'your_command_here' with the actual terminal command you want to run
        command = f'nougat --markdown pdf {pdf_path} --out "physics"'

        # Run the command and capture the output
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Display the output in the template
        return {'result': result.stdout, 'error': result.stderr}

    except subprocess.CalledProcessError as e:
        # Handle errors if the command fails
        return HttpResponse(f"Error: {e}", status=500)

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_pdf = form.save()
            print(uploaded_pdf.file.path)
            pdf_path = uploaded_pdf.file.path
            result = convert_pdf_to_text(pdf_path, request)
            print(result)
            return redirect('pdf_list')
    else:
        form = PDFFileForm()
    return render(request, 'pdfuploader/upload_pdf.html', {'form': form})


def pdf_list(request):
    pdf_files = PDFFile.objects.all()
    return render(request, 'pdfuploader/pdf_list.html', {'pdf_files': pdf_files})