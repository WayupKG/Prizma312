from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView


class RegisterView(TemplateView):
    template_name = 'registration/register.html'

    def post(self, request, *args, **kwargs):
        context = {}
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        user = User.objects.filter(username=username)
        user_email = User.objects.filter(email=email)

        if user:
            context['username_error'] = 'Пользователь с таким логином уже существует'

        elif user_email:
            context['email_error'] = 'Пользователь с таким Email уже существует'

        elif password != password2:
            context['password2_error'] = 'Пароль не совпадает'

        else:
            new_user = User.objects.create_user(username=username, email=email, password=password)
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.save()
            return redirect('/accounts/login/')
        return render(request, self.template_name, context)
