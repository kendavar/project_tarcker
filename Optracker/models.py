from django.db import models

# Initailse the choices field
TYPES_OF_OPPORTUNITYS =(
  ("PROCESS","Process"),
  ("TOOL","Tool"),
)

STATUS = (
   ("OPEN","Open"),
   ("UNDER REVIEW","Under Review"),
   ("ACCEPTED","Accepted"),
   ("CLOSED/REJECTED","Closed/Rejected")
)

SEVERITY = (
    ("HIGH","HIGH"),
    ("MEDIUM","MEDIUM"),
    ("LOW","LOW")
)

PROCESS_IMPACT = (
   ("BOOKING","Booking"),
   ("TRAFFICKING","Trafficking"),
   ("REPORTING","Reporting"),
   ("EXPANSION SERVICES","Expansion Services")

)
class optrackertable(models.Model):
    type_of_idea = models.CharField(max_length=10,default=None, choices=TYPES_OF_OPPORTUNITYS,null=True)
    problem_statement = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now_add=False,default=None,null=True)
    description = models.TextField(max_length=10000)
    assign_to = models.CharField(max_length=100,default=None,null=True)
    severity = models.CharField(max_length=100,default=None, choices=SEVERITY)
    Other_tool = models.CharField(max_length=100,default=None,blank=True,null=True)
    process_Impact = models.CharField(max_length=100,default=None,choices=PROCESS_IMPACT,null=True)
    comment =models.TextField(max_length=10000,default=None,null=True)
    possible_solution = models.TextField(max_length=10000)
    file_upload = models.FileField(upload_to='files_uploaded')
    contributors = models.CharField(max_length=100,default=None)
    submitted_by = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    status = models.CharField(max_length=30,default=STATUS[0][0], choices=STATUS,null=True)
    status_update = models.CharField(max_length=100,default=None,null=True)

    def __str__(self):
        return self.opportunity_name
