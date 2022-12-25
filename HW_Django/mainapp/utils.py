from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import QuerySet


def paginate(
        obj: QuerySet,
        size: int,
        request: WSGIRequest,
        context: dict,
        var_name: str = 'object_list',
) -> dict:

    paginator = Paginator(obj, size)
    page_num = request.GET.get('page', '1')

    try:
        page = paginator.page(page_num)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    context[var_name] = page
    context['is_paginated'] = page.has_other_pages()
    context['page_obj'] = page
    context['paginator'] = paginator
    context['pages'] = range(1, context['page_obj'].paginator.num_pages + 1)

    return context



