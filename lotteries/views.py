from django.shortcuts import render
from lotteries.forms.file_loader_form import FileLoaderForm
import pdb
from  lotteries.services.database_services import load_data_from_file

HTML_FILES = {
	'index': 'index.html',
	'loader': 'file_loader.html',
}

# Create your views here.
def index(request):
    return render(request, HTML_FILES['index'], {})

# View function used to load data into database.
def load_data(request):
    if request.method == 'POST':
        form = FileLoaderForm(request.POST, request.FILES)
        if form.is_valid():
            load_data_from_file(request.FILES['data_file'])
            return render(request, HTML_FILES['index'], {})
    else:
        form = FileLoaderForm()

    return render(request, HTML_FILES['loader'], { 'form': form})
