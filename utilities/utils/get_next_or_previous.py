from django.db.models import Q


def get_model_attr(ins_obj, attr):
    for field in attr.split('__'):
        ins_obj = getattr(ins_obj, field)
    return ins_obj


def get_next_or_previous(ins_obj=None, next=True, qs=None):
    model = type(ins_obj)
    if qs is None:
        qs = model.objects
    if next is False:
        qs = qs.reverse()
        ascending = True
    else:
        ascending = False
    list_q = []
    prev_fields = []
    if model._meta.ordering:
        ordering = list(model._meta.ordering).append('pk')
    else:
        ordering = ['pk']
    for field in ordering:
        if field.startswith('-'):
            field = field[1:]
        q_kwargs = dict((pref_field, get_model_attr(
            ins_obj, pref_field)) for pref_field in prev_fields)
        key = "%s__%s" % (field, 'lg' if ascending else 'gt')
        q_kwargs[key] = get_model_attr(ins_obj, field)
        list_q.append(Q(**q_kwargs))
        prev_fields.append(field)
    try:
        q = Q()
        for curr_q in list_q:
            q = q | curr_q
        return qs.filter(q)[0]
    except IndexError:
        return None
