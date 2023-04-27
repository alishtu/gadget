from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *
from .utils import *
from django.contrib.auth import login

class ShowPost(DataMixin, DetailView):
    model = Shopee
    template_name = 'shopee/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))

class ShopeeMarket(DataMixin, ListView):
    model = Shopee
    template_name = 'shopee/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Shopee.objects.filter(is_published=True)

#def index(request):
#    posts = Shopee.objects.all()
#    context = {
#        'posts': posts,
#        'menu': menu,
#        'title': 'Главная страница'
#    }
#    return render(request, 'shopee/index.html', context = context)


def about(request):
    contact_list = Shopee.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'shopee/about.html', {'page_obj': page_obj, 'menu': menu, 'title': 'О сайте'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'shopee/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление смартфона")
        return dict(list(context.items()) + list(c_def.items()))

#def addpage(request):
#    if request.method == 'POST':
#        form = AddPostForm(request.POST, request.FILES)
#        if form.is_valid():
#                form.save()
#                return redirect('home')
#    else:
#        form = AddPostForm()
#    return render(request, 'shopee/addpage.html', {'menu': menu, 'title': 'Добавление смартфона', 'form': form})


#def contact(request):
 #   return HttpResponse("Обратная связь")
class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'shopee/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


#def show_post(request, post_slug):
#    post = (get_object_or_404(Shopee, slug=post_slug))
#    context = {
#       'post': post,
#       'menu': menu,
#        'title': post.title,
#   }
#return render(request, 'shopee/post.html', context=context)



class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'shopee/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
        form_class = LoginUserForm
        form_class = AuthenticationForm
        template_name = 'shopee/login.html'

        def get_success_url(self):
            return reverse_lazy('home')

        def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            c_def = self.get_user_context(title="Авторизация")
            return dict(list(context.items()) + list(c_def.items()))


def logout_user(request):
    logout(request)
    return redirect('login')

