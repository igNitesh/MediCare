from atexit import register
from http.client import OK
from django import template
register =template.Library()

@register.simple_tag
def get_table_class(value):
    # if value:
    #     return "bg-success"
    # return "bg-danger"
    if value == 0:
        return "bg-danger"

    elif value>0 and value <10:
        return "bg-warning"

    else:
        return "bg-success"




@register.simple_tag
def is_city_selected(selected_city_id,pk):
    if selected_city_id == str(pk):
        return 'selected'
    return ''