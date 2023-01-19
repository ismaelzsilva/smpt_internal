from django.shortcuts import render
from django.views.generic import FormView, ListView, DetailView, CreateView, DeleteView
from django.http import FileResponse
from .models import FabricationOrders
from .forms import CreateLabelsForm

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm
from reportlab.lib.pagesizes import letter
import io

# Create your views here.

class HomeView(ListView):
    model = FabricationOrders
    template_name = "home/home.html"
    context_object_name = 'fabrication_orders'


class OF(DetailView):
    model = FabricationOrders
    template_name = 'home/of.html'

class CreateOF(CreateView):
    model = FabricationOrders
    template_name = 'home/create_of.html'
    fields = ('__all__')
    success_url = '/'

class DeleteOF(DeleteView):
    model = FabricationOrders
    template_name = "home/delete_of.html"
    success_url = '/'

class CreateLabels(FormView):
    template_name = 'home/create_labels.html'
    form_class = CreateLabelsForm
    success_url ='/'

    def form_valid(self, form):

        order_fabrication = str(form.cleaned_data['fabrication_order'])
        reference = str(form.cleaned_data['reference'])
        article = str(form.cleaned_data['article'])
        designation = str(form.cleaned_data['designation'])

        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize = (90*mm,30*mm), bottomup = 0)

        for n in range(1, form.cleaned_data['quantity'] + 1):

            textob = c.beginText()
            textob.setTextOrigin(10, 15)
            textob.setFont('Helvetica', 11)
            
            lines = [
                'OF:                ' + order_fabrication,
                'Reference:    ' + reference,
                'Article:           ' + article,
                'Designation:  ' + designation,
                'Number:        ' + str(n),
            ]

            for line in lines:
                textob.textLine(line)
            c.drawText(textob)
            c.showPage()
        
        c.save()
        buf.seek(0)
        
        return FileResponse(buf, as_attachment=False, filename='labels.pdf')
