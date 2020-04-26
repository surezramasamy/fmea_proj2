from django import forms
from .models import Fmea_Record

class PostForm(forms.ModelForm):
    Recommended_Actions = forms.CharField(required=False,help_text="*Optional")
    Resp_Target_Date=forms.CharField(required=False,help_text="*Optional")
    Actions_Taken=forms.CharField(required=False,help_text="*Optional")
    Sev_Rev=forms.IntegerField(required=False,help_text="*Optional")
    Occ_Rev=forms.IntegerField(required=False,help_text="*Optional")
    Det_Rev=forms.IntegerField(required=False,help_text="*Optional")
    RPN_Rev=forms.IntegerField(required=False,help_text="*Optional")
    Rev_No=forms.IntegerField(required=False,help_text="*Optional")
    Rev_Date=forms.DateField(required=False,help_text="*Optional")
    Rev_History=forms.CharField(required=False,help_text="*Optional")

    class Meta:
        model = Fmea_Record
        fields = ['date','Part_Name','Process_OR_Function','Potential_Failure_Mode','Potential_Effects_of_Failure',
                  'Sev','Class','Potential_causes_or_Mechanisms_of_Failure','Occ','Current_Process_Control_Prevention',
                  'Current_Process_Control_Detection','Det','RPN','Recommended_Actions','Resp_Target_Date','Actions_Taken',
                  'Sev_Rev','Occ_Rev','Det_Rev','RPN_Rev','Rev_No','Rev_Date','Rev_History']
