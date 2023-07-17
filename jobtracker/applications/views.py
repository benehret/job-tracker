from django.shortcuts import render, redirect, get_object_or_404
from .models import Application
from .forms import ApplicationForm

from django.shortcuts import render, redirect
from .models import Company, Application

def application_create(request):
    if request.method == 'POST':
        company_name = request.POST.get('company')
        position = request.POST.get('position')
        status = request.POST.get('status')
        interview_date = request.POST.get('interview_date')

        # Check if the company already exists in the database
        try:
            company = Company.objects.get(name=company_name)
        except Company.DoesNotExist:
            # If the company doesn't exist, create a new one
            company = Company(name=company_name)
            company.save()

        application = Application(company=company, position=position, status=status, interview_date=interview_date)
        application.save()
        return redirect('application_list')

    return render(request, 'applications/application_create.html')

def application_list(request):
    if request.method == 'POST':
        application_id = request.POST.get('application_id')
        if application_id:
            application = get_object_or_404(Application, id=application_id)
            form = ApplicationForm(request.POST, instance=application)
        else:
            form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('application_list')
    else:
        form = ApplicationForm()

    applications = Application.objects.all()
    return render(request, 'applications/application_list.html', {'applications': applications, 'form': form})

def application_detail(request, pk):
    application = Application.objects.get(pk=pk)
    return render(request, 'applications/application_detail.html', {'application': application})

