from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_paginator_context(objects, request, n_pages=10):
    paginator = Paginator(objects, n_pages)
    page = request.GET.get('page')
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)
    return {
        'object_list': object_list,
        'is_paginated': paginator.num_pages > 1,
        'page_obj': object_list,
        'paginator': paginator
    }
