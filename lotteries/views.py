from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import permission_required
from lotteries.forms.file_loader_form import FileLoaderForm
from django.http import HttpResponseForbidden
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
@permission_required('lotteries.can_add', raise_exception=True)
def load_data(request):
    if request.method == 'POST':
        form = FileLoaderForm(request.POST, request.FILES)
        if form.is_valid():
            load_data_from_file(request.FILES['data_file'])
            return redirect('lotteries-views-index')
    else:
        form = FileLoaderForm()

    return render(request, HTML_FILES['loader'], { 'form': form})
