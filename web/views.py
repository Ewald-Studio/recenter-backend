from __future__ import annotations
from django.views.decorators.cache import cache_page
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from media.models import Article, Section
from orgstructure.models import Organization


# @cache_page(60*10)
def index(request):
    approved_articles = Article.objects.filter(status="APPROVED").select_related('author', 'author__organization')
    important_articles = approved_articles.filter(is_important=True)
    articles = approved_articles.filter(is_important=False).order_by('?')[:3]
    sections = Section.objects.all().annotate(articles_count=Count('articles', filter=Q(articles__status="APPROVED")))
    organizations = Organization.objects.all()

    data = {
        'important_articles': important_articles,
        'articles': articles,
        'sections': sections,
        'organizations': organizations,
    }

    return render(request, 'index.html', data)


def article_list(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    articles = Article.objects.filter(status="APPROVED", sections__id=section_id).select_related('author', 'author__organization')
    data = {
        'section': section,
        'articles': articles,
    }
    return render(request, 'article_list.html', data)


def article_search(request):
    query = request.GET.get('query', '').strip()
    if len(query) < 3:
        data = {
            'query': query,
            'articles': [],
            'error': "Запрос должен содержать не менее 3-х символов"
        }
    else:
        articles = Article.objects.filter(
            Q(title__icontains=query) | 
            Q(annotation__icontains=query) |
            Q(text__icontains=query) |
            Q(questions__icontains=query)
        )
        data = {
            'query': query,
            'articles': articles,       
        }
    return render(request, 'article_search.html', data)


def article_item(request, article_id):
    article = get_object_or_404(Article, id=article_id, status="APPROVED")
    data = {
        'article': article
    }
    return render(request, 'article_item.html', data)


def organization_list(request):
    organizations = Organization.objects.all()
    data = {
        'organizations': organizations,
    }
    return render(request, 'organization_list.html', data)


def organization_item(request, organization_id):
    organization = get_object_or_404(Organization, id=organization_id)
    articles = Article.objects.filter(status="APPROVED", author__organization=organization).order_by('-creation_date')[:3]
    data = {
        'organization': organization,
        'articles': articles,
    }
    return render(request, 'organization_item.html', data)