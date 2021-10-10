from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail
from django.forms.models import model_to_dict
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from currency import model_choices as mch
from currency.forms import RateForm, SourceForm
from currency.models import ContactUs, Rate, Source
from currency.services import get_latest_rates
from currency.tasks import contact_us


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


def get_contact_us(request):
    contacts = ContactUs.objects.all()

    context = {
        "contact_list": contacts
    }

    return render(request, "contact.html", context=context)


class RateListView(ListView):
    queryset = Rate.objects.all().defer('created').select_related('source').order_by('-created')
    template_name = 'rate_list.html'


class CreateRateViev(CreateView):
    queryset = Rate.objects.all()
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'create_rate.html'


class DeleteRateView(DeleteView):
    queryset = Rate.objects.all()
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'delete_rate.html'


class UpdateRateView(UpdateView):
    queryset = Rate.objects.all()
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'update_rate.html'


class DetailRateView(DetailView):
    queryset = Rate.objects.all()
    template_name = 'rate_details.html'


class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'


class CreateSourceViev(CreateView):
    queryset = Source.objects.all()
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')
    template_name = 'create_source.html'


class DeleteSorceView(DeleteView):
    queryset = Source.objects.all()
    success_url = reverse_lazy('currency:source-list')
    template_name = 'delete_source.html'


class UpdateSourceView(UpdateView):
    queryset = Source.objects.all()
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')
    template_name = 'update_source.html'


class DetailSourceView(DetailView):
    queryset = Source.objects.all()
    template_name = 'sourсe_details.html'


class ContactUsCreateViev(CreateView):
    model = ContactUs
    success_url = reverse_lazy('index')
    template_name = 'create_contactus.html'
    fields = ('email_to', 'subject', 'body')

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        body = form.cleaned_data['body']
        email_to = form.cleaned_data['email_to']

        full_email_body = f'''
        Email To: {email_to}
        Body: {body}
        '''

        contact_us.apply_async(args=(subject,), kwargs={'body': full_email_body})
        return super().form_valid(form)


class LatestRatesView(TemplateView):
    template_name = 'latest_rates_list.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['rate_list'] = get_latest_rates()
        return context
