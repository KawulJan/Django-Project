
from django.views.generic import TemplateView


# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "Gulnur"
        return ctxt

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self):
       ctxt = super().get_context_data()
       ctxt["num_services"] = 67565441
       ctxt["skills"] =[
        "Python",
        "HTML",
        "JavaScript",
        "Java",
        "CSS",

       ]
       return ctxt



class ContectView(TemplateView):
    template_name = "contect.html"