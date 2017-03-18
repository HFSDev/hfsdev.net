from django.shortcuts import render

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
            loader = DatabaseLoader()
            loader.load_data(request.FILES['data_file'])
            return render(request, HTML_FILES['index'], {})
    else:
        form = FileLoaderForm()

    return render(request, 'file_loader.html', { 'form': form})
