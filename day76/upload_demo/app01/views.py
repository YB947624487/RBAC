from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def qigeming(request):
    if request.method == "POST":
        file_obj = request.FILES.get("kouge")
        with open(file_obj.name, "wb") as f:
            for line in file_obj.chunks():
                f.write(line)
    return render(request, "qigeming.html")