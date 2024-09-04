from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306212695',
        'name': 'Alfian Bassam Firjatullah',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
