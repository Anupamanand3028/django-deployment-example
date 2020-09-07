from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,args):
    ''' Removes all the value of args form string'''
    return replace(value,'')

register.filter('cut',cut)
