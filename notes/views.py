from django.shortcuts import render

from .models import Notes

from django.http import Http404
from django.views.generic import ListView,DetailView

# Create your views here.
class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"



def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})

def details(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist!!")
    return render(request, 'notes/notes_detail.html', {'note': note})
