from django.contrib import admin
from fmea_app.models import Fmea_Record,Part_name,Process_or_Function
from import_export import fields,resources
from import_export.fields import Field
from import_export.widgets import ManyToManyWidget
from import_export.admin import ImportExportModelAdmin

class BookResource(resources.ModelResource):
    Part_Name = fields.Field(attribute ='Part_Name',widget=ManyToManyWidget('Part_Name'))
    Process_OR_Function = fields.Field(attribute = 'Process_OR_Function')

    class Meta:
        model = Fmea_Record
        fields = ('date','Part_Name','Process_OR_Function','Potential_Failure_Mode','Potential_Effects_of_Failure',
                  'Sev','Class','Potential_causes_or_Mechanisms_of_Failure','Occ','Current_Process_Control_Prevention',
                  'Current_Process_Control_Detection','Det','RPN','Recommended_Actions','Resp_Target_Date','Actions_Taken',
                  'Sev_Rev','Occ_Rev','Det_Rev','RPN_Rev','Rev_No','Rev_Date','Rev_History')

        export_order = ('Part_Name','date','Process_OR_Function','Potential_Failure_Mode','Potential_Effects_of_Failure',
                  'Sev','Class','Potential_causes_or_Mechanisms_of_Failure','Occ','Current_Process_Control_Prevention',
                  'Current_Process_Control_Detection','Det','RPN','Recommended_Actions','Resp_Target_Date','Actions_Taken',
                  'Sev_Rev','Occ_Rev','Det_Rev','RPN_Rev','Rev_No','Rev_Date','Rev_History')





class BookAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = BookResource
    list_display = ['date','All_parts','Process_OR_Function','Potential_Failure_Mode','Potential_Effects_of_Failure',
              'Sev','Class','Potential_causes_or_Mechanisms_of_Failure','Occ','Current_Process_Control_Prevention',
              'Current_Process_Control_Detection','Det','RPN','Recommended_Actions','Resp_Target_Date','Actions_Taken',
              'Sev_Rev','Occ_Rev','Det_Rev','RPN_Rev','Rev_No','Rev_Date','Rev_History']




    #search_fields = ['part_name','defect_catagory','contractor']
    #list_filter = ['part_name','defect_catagory','contractor']

admin.site.register(Fmea_Record,BookAdmin)
admin.site.register(Part_name)
admin.site.register(Process_or_Function)

# Register your models here.
