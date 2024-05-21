from django.contrib.auth import get_user_model, login
from django.shortcuts import render, redirect

# Create your views here.
# recupérer le model utilisateur
User = get_user_model()


def signup(request):
    if request.method == 'POST':
        # traiter le formulaire
        username = request.POST.get("Username")
        password = request.POST.get("Password")
        lastname = request.POST.get("Lastname")
        firstname = request.POST.get("Firstname")
        email = request.POST.get("Email")

        # créer l'utilisateur
        user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)

        # connecter l'utilisateur
        login(request, user)
        return redirect('home')

    return render(request, 'accounts/signup.html')
