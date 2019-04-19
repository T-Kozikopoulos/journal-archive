from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView
from archive.forms import PostForm
from archive.models import Post


@login_required
def index(request):
    posts = Post.objects.filter(author=request.user).order_by('-date_created')
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.instance.author = request.user
        saved = form.save(commit=False)
        saved.save()
        return redirect('index')

    context = {
        'posts': posts,
        'form': form
    }
    return render(request, 'index.html', context)


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('index')
    template_name = 'delete_post.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
