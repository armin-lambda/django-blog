from django.shortcuts import render, get_object_or_404
from django.views import View
from django.db.models import Q

from .models import Post


class PostListView(View):
    template_name = 'blog/post_list.html'

    def get(self, request):
        post_list = Post.objects.filter(is_published=True)

        if request.GET.get('search'):
            search = request.GET['search']
            post_list = post_list.filter(
                Q(title__icontains=search) |
                Q(body__icontains=search) |
                Q(created_at__icontains=search)
            )

        return render(request, self.template_name, {'post_list': post_list})


class PostDetailView(View):
    template_name = 'blog/post_detail.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name, {
            'post': get_object_or_404(Post, slug=kwargs['slug']),
        })
