from django.shortcuts import render

from .models import Notes

from django.http import Http404

# Create your views here.

def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})

def details(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist!!")
    return render(request, 'notes/notes_detail.html', {'note': note})
