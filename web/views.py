from django.shortcuts import render, get_object_or_404
from media.models import Article
from orgstructure.models import Organization


def index(request):
    approved_articles = Article.objects.filter(status="APPROVED").select_related('author', 'author__organization')
    important_articles = approved_articles.filter(is_important=True)
    articles = approved_articles.filter(is_important=False)
    organizations = Organization.objects.all()

    data = {
        'important_articles': important_articles,
        'articles': articles,
        'organizations': organizations,
    }

    return render(request, 'index.html', data)


def article_list(request, section_id):
    articles = Article.objects.filter(status="APPROVED", sections__id=section_id).select_related('author', 'author__organization')
    data = {
        'articles': articles,
    }
    return render(request, 'article_list.html', data)


def article_search(request):
    query = request.GET.get('query', '')
    data = {
        'query': query,
    }
    return render(request, 'article_search.html', data)


def article_item(request, article_id):
    article = get_object_or_404(Article, id=article_id, status="APPROVED").select_related('author', 'author__organization')
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
    data = {
        'organization': organization
    }
    return render(request, 'organization_item.html', data)