from django.shortcuts import render,get_list_or_404, get_object_or_404
from Optracker import forms
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.core import mail
from Optracker.models import optrackertable
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import csv
from datetime import datetime
from Optracker import filters
from django.core.mail import EmailMultiAlternatives
from django.utils import timezone
# from Optracker import opform
# connection = mail.get_connection()
# connection.open()
# Create your views here.

def userform(request):
    form = forms.userForm()
    if request.method == "POST":
        form = forms.userForm(request.POST)
        if form.is_valid():
            # # send_mail("Opportunity Assigned",
            # # """Hi @%s,\n\nThank you very much, Your feedback is very valuable for the team.We will keep you posted about the status of your ideas soon. \n\nThank You!"""%(form.cleaned_data['submitted_by']),
            # #  'AdOps_AutoMailer@amazon.com', [form.cleaned_data['submitted_by']+'@amazon.com',form.cleaned_data['manager_Alias']+'@amazon.com'])
            # subject, from_email, to = "New Innovative Idea", 'AdOps_AutoMailer@amazon.com', 'to@example.com'
            # text_content = 'Hi @%s,\n\nThank you very much, Your feedback is very valuable for the team.We will keep you posted about the status of your ideas soon. \n\nThank You!'%(form.cleaned_data['submitted_by'])
            # html_content = '<p>Hi @%s,<br><br>Thank you very much, Your feedback is very valuable for the team.We will keep you posted about the status of your ideas soon. <br><br>Thank You!</p>'%(form.cleaned_data['submitted_by'])
            # msg = EmailMultiAlternatives(subject, text_content, from_email, [form.cleaned_data['submitted_by']+"@amazon.com"], cc=[form.cleaned_data["manager_Alias"]+"@amazon.com"])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            form.save(commit=True)
            print("SAVED")
            return HttpResponseRedirect(reverse("thankyou"))
        else:
            print("ERROR FORM INVALID")

    return render(request,"Optracker/userform.html",
        {
            'form'          :form,
            "exclude_list"  :["idea_Description","possible_solution"],
            "mail_field"    :["manager_Alias","submitted_by"],
        })




def update_the_form(request, id):
    instance = optrackertable.objects.get(id=id)
    form = forms.optracForm(request.POST or None, instance=instance)
    if form.is_valid():
          form.last_updated_at=str(datetime.now())
          form.save()
          return redirect('next_view')
    return direct_to_template(request, 'Optracker/update_optracker.html', {'form': form})

def dashboard(request):
    data = optrackertable.objects.all().order_by('-id')
    # print(data)
    # flag=0
    # if flag:
    #print(flag)
    #data_filter = filters.dashFilter(request.GET,queryset=data)
    #print(data_filter)
    #paginator = Paginator(data_filter.qs, 25) # Show 25 contacts per page
    # else:
    #     print(flags)
    paginator = Paginator(data, 25)
    #    flag=1
    page = request.GET.get('page',1)
    try:
        datas = paginator.page(page)
    except PageNotAnInteger:
        datas = paginator.page(1)
    except EmptyPage:
        datas = paginator.page(paginator.num_pages)
    return render(request,"Optracker/dashboard.html",{"dash":datas})

def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="optracker.csv"'

    writer = csv.writer(response)
    writer.writerow(["Problem Statement:","Description:",
    "Created Date:","Last Updated:","Status:","Status update:","Assign to:",
    "severity:","comment:",
    "Contributors:","Submitted by:"])

    optracker_values = optrackertable.objects.all().values_list("problem_statement",
    "description","created_at","last_updated_at","status","status_update","assign_to",
    "severity","comment",
    "contributors","submitted_by")

    for value in optracker_values:
        writer.writerow(value)
    return response



def opform(request):
    form = forms.mainForm()
    if request.method == "POST":
        form = forms.mainForm(request.POST)
        # form.cleaned_data['status_update'] = None
        # form.cleaned_data['last_updated_at'] = None
        if form.is_valid():
            # subject, from_email, to = "New Innovative Idea", 'AdOps_AutoMailer@amazon.com', 'to@example.com'
            # text_content = 'Hi @%s,\n\nThank you very much, Your feedback is very valuable for the team.We will keep you posted about the status of your ideas soon. \n\nThank You!'%(form.cleaned_data['submitted_by'])
            # html_content = '<p>Hi @%s,<br><br>Thank you very much, Your feedback is very valuable for the team.We will keep you posted about the status of your ideas soon. <br><br>Thank You!</p>'%(form.cleaned_data['submitted_by'])
            # msg = EmailMultiAlternatives(subject, text_content, from_email, [form.cleaned_data['submitted_by']+"@amazon.com"], cc=[form.cleaned_data["manager_Alias"]+"@amazon.com"])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()


            form.save(commit=True)
            print("SAVED")
            return HttpResponseRedirect(reverse("thankyou"))
        else:
            print("ERROR FORM INVALID")

    return render(request,"Optracker/mainform.html",
        {
            'form'          :form,
            "exclude_list"  :["idea_Description","possible_solution","impact_summary","assign_to"],
            "mail_field"    :["manager_Alias","assign_to","submitted_by"],
            "update_col"    :['last_updated_at','status_update']
        })
from django.utils import timezone
def thankyou(request):
    return render(request,"Optracker/thankyou.html",{})

def edit_post(request,id):
    post = get_object_or_404(optrackertable,id=id)
    if request.method == "POST":
        form =forms.editForm(request.POST,request.FILES, instance=post)

        if form.is_valid():
            # subject, from_email, to = "New Innovative Idea", 'AdOps_AutoMailer@amazon.com', 'to@example.com'
            # text_content = 'Hi @%s,\n\nThank you for submitting the idea and your idea is (%s).  \n\nThank You!'%(form.cleaned_data['submitted_by'],form.cleaned_data['status'])
            # html_content = '<p>Hi @%s,<br><br>Thank you for submitting the idea and your idea is (%s). <br><br>Thank You!</p>'%(form.cleaned_data['submitted_by'],form.cleaned_data['status'])
            # msg = EmailMultiAlternatives(subject, text_content, from_email, [form.cleaned_data['submitted_by']+"@amazon.com"], cc=[form.cleaned_data["manager_Alias"]+"@amazon.com"],bcc=[form.cleaned_data['status']])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            # send_mail("Status Update", """Hi @%s,\n\nThis opportunity has been updated.Please take the necessary actions.\n\nOpportunity Number: %s\nType of opportunity: %s\n Opportunity name: %s\nTeam name: %s\nStatus: %s\nImpact estimate: %s\nImpact summary: %s\nProblem solution: %s\nStatus update: %s\nCreated date: %s\nLast Updated:%s\n\nThank You!
            # """%(form.cleaned_data['assign_to'],optrackertable.objects.all().count()+1,
            # form.cleaned_data['type_of_opportunity'],
            # form.cleaned_data['opportunity_name'],
            # form.cleaned_data['team_name'],
            # form.cleaned_data['status'],
            # form.cleaned_data['impact_estimate'],
            # form.cleaned_data['impact_summary'],
            # form.cleaned_data['problem_solution'],
            # form.cleaned_data['status_update'],
            # post.created_at,
            # str(datetime.now())
            # ), 'AdOps_AutoMailer@amazon.com', [form.cleaned_data['assign_to']+'@amazon.com','kendavar@amazon.com'])
            post.last_updated_at=datetime.now(tz=timezone.utc)
            post = form.save(commit=True)
            post.save()
            return HttpResponseRedirect(reverse("dashboard"))
    else:
        form = forms.editForm(instance=post)

    return render(request,"Optracker/mainform.html",
            {
                'form'          :form,
                "exclude_list"  :["idea_Description","impact_summary","possible_solution","assign_to"],
                "mail_field"    :["manager_Alias","assign_to","submitted_by"],
                "update_col"    :['last_updated_at'],
                "cancel_page"   :[]
            })
