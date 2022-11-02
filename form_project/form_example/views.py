from django.shortcuts import render
from .forms import ExampleForm


def form_example(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
    else:
        form = ExampleForm()

    if request.method == "POST":
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print("{}: {}".format(name, value))
    return render(request, "form-example.html", {"method": request.method, "form": form})
