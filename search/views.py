from django.conf import settings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from wagtail.contrib.search_promotions.models import Query
from wagtail.models import Page

from bakerydemo.blog.models import BlogPage
from bakerydemo.breads.models import ImplantPage  # Updated import
from bakerydemo.locations.models import LocationPage


def search(request):
    # Search
    search_query = request.GET.get("q", None)
    if search_query:
        if "elasticsearch" in settings.WAGTAILSEARCH_BACKENDS["default"]["BACKEND"]:
            # In production, use ElasticSearch and a simplified search query
            search_results = Page.objects.live().search(search_query)
        else:
            # If we aren't using ElasticSearch, fall back to native DB search.
            # Hard-code in the model names we want to search.
            blog_results = BlogPage.objects.live().search(search_query)
            blog_page_ids = [p.page_ptr.id for p in blog_results]

            implant_results = ImplantPage.objects.live().search(search_query)  # Updated reference
            implant_page_ids = [p.page_ptr.id for p in implant_results]

            location_results = LocationPage.objects.live().search(search_query)
            location_result_ids = [p.page_ptr.id for p in location_results]

            page_ids = blog_page_ids + implant_page_ids + location_result_ids
            search_results = Page.objects.live().filter(id__in=page_ids)

        query = Query.get(search_query)

        # Record hit
        query.add_hit()

    else:
        search_results = Page.objects.none()

    # Pagination
    page = request.GET.get("page", 1)
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return render(
        request,
        "search/search_results.html",
        {
            "search_query": search_query,
            "search_results": search_results,
        },
    )
