from django import template
register = template.Library()

@register.simple_tag
def is_state_selected(selected_state, id):
    if selected_state == str(id):
        return "selected"
    else:
        return ""
    
@register.simple_tag
def is_city_selected(selected_city, id):
    if selected_city == str(id):
        return "selected"
    else:
        return ""