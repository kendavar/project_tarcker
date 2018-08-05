from django import forms
from Optracker.models import optrackertable

#Main form page to create new entries
class mainForm(forms.ModelForm):

    class Meta:
        model= optrackertable
        exclude = exclude = ("possible_solution","Other_tool","process_Impact","type_of_idea","last_updated_at","status_update",
        "assign_to","status","comment")
                                                     # This two fields are
                                                     #filled after the new
                                                     #form is created. So they
                                                     #are exculded.

#edit form page having all the fields
class editForm(forms.ModelForm):

    class Meta:
        model= optrackertable
        #fields = "__all__"
        exclude = ("last_updated_at","status_update","possible_solution","Other_tool","process_Impact","type_of_idea","status",)

class userForm(forms.ModelForm):

    class Meta:
        model = optrackertable
        exclude = ("possible_solution","Other_tool","process_Impact","impact_summary",
        "type_of_idea","last_updated_at","status_update","assign_to","impact_summary","status")
