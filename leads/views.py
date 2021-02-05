from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm


class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class LandingTemplateView(TemplateView):
    # TODO render the home page
    template_name = "landing.html"


def landing(request):
    return render(request, "landing.html")


class LeadListView(LoginRequiredMixin, ListView):
    template_nanme = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"



def home(request):
    leads = Lead.objects.all()

    context = {"leads":leads}
    return render(request, "leads/lead_list.html", context)


class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)

    context = {'lead':lead}
    return render(request, "leads/lead_detail.html", context)


class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse("leads:lead_list")

    def  form_valid(self, form):
        # TODO send email
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see the new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )
        return super(LeadCreateView, self).form_valid(form)



def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        print("Recieving a post request")
        form = LeadModelForm(request.POST)
        if form.is_valid():
            print("This form is valid")
            form.save()
            return redirect('/leads')

    context = {
        "form":form
        }

    return render(request, "leads/lead_create.html", context)


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm
    queryset = Lead.objects.all()
    context_object_name = "lead"

    def get_success_url(self):
        return reverse("leads:lead_list")


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        print("Recieving a posr request")
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            print("This form is valid")
            form.save()
            return redirect('/leads')

    context = {
        "form":form,
        "lead":lead,
        }

    return render(request, "leads/lead_update.html", context)


class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

    def get_success_url(self):
        return reverse("leads:lead_list")


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    if request.method == "POST":
        lead.delete()
        return redirect('/leads')
    context = {
        "lead":lead
    }
    return render(request, "leads/lead_delete.html", context)

"""def lead_create(request):
    form = LeadForm()
    if request.method == "POST":
        print("Recieving a posr request")
        form = LeadForm(request.POST)
        if form.is_valid():
            print("This form is valid")
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age = age,
                email = email,
                agent = agent
            )
            return redirect('/leads')

    context = {
        "form":form
        }

    return render(request, "leads/lead_create.html", context)"""



