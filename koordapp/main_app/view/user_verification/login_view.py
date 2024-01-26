from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render

from main_app.models import Personal

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":  
            form = LoginForm(data=request.POST)
            try:
                if form.is_valid():
                    cleandata=form.cleaned_data
                    #authenticate checks if credentials exists in db
                    user=authenticate(username=cleandata['username'],
                                    password=cleandata['password'])
                    if user is not None:
                        if user.is_active:
                            auth_login(request, user)
                            if(Personal.objects.filter(user=user).exists()):
                                personal = Personal.objects.get(user=user)
                                if(personal.is_password_otp == True):
                                    return redirect("set_new_pw")
                            return redirect("master_web")
                    else:
                        messages.error(request,"Benutzername oder Passwort Falsch")
                        return redirect("login")
                else:
                    messages.error(request,"Benutzername oder Passwort Falsch")
            except:
                messages.error(request,"Benutzername oder Passwort Falsch")
        else:
            form=LoginForm()
            
    else:
        return redirect("master_web")

    return render(request, "user_verification/user_login.html", {'form':form})


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Deaktiviere die Fehlermeldungen
        self.error_messages = {}
        self.fields['username'].label = "Benutzername"
        self.fields['password'].label = "Passwort"