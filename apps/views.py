from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.http import Http404

from .models import App, Comment
from .forms import PostCommentForm

class AppsView(ListView):
    template_name = "apps/index.html"
    context_object_name = "latest_apps"

    def get_queryset(self):
        return App.objects.order_by('release_date')[:20]
    
def app_view(request, pk):
    comment_form = PostCommentForm()
    app = get_object_or_404(App, pk=pk, active=True)
    is_authenticated = request.user.is_authenticated
    comments = Comment.objects.filter(app=app)

    return render(request, 'apps/app.html', {'app': app, 'comments': comments, 'is_authenticated': is_authenticated, 'comment_form': comment_form})

def post_comment(request):
    if request.method == 'POST':
        app = get_object_or_404(App, pk=int(request.POST.get('app_pk')))
        form = PostCommentForm(request.POST)
        
        if form.is_valid():
            print('Form is valid!')
            comment = Comment.objects.create(user=request.user, app=app, text=form.cleaned_data['text'])
            comment.save()
        else:
            print(form.errors)
        return redirect('apps:app', pk=app.pk)
    
    return Http404