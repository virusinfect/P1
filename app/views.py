from django.shortcuts import render

def timeline(request):
    return render(request, 'timeline.html')
def test(request):
    return render(request, 'test.html')
def members(request):
    return render(request, 'members.html')
def founders(request):
    return render(request, 'founders.html')