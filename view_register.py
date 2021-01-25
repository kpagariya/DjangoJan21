def registermenu(request):
    #return HttpResponse('<h1>Hello, I am learning Django!</h1>')
    # Logic to register the User
    # if request is GET then display the registration form
    # else if its POST request then process the Form - validate the user info and perform the action
    if request.method == 'POST':
    	print("I am in POST request")
    	username=request.POST['username']
    	email=request.POST['email']
    	password1=request.POST['password1']
    	password2=request.POST['password2']
    	print("username :",username)
    	print("email :",email)
    	print("password1 :",password1)
    	print("password2 :",password2)

    	if(password1==password2):
    		if User.objects.filter(username=username).exists():
    			print('The username is not available/its already exists')
    			return redirect('register')
    		else:
    			user = User.objects.create_user(username=username,password=password1,email=email)
    			user.save()
    			print("You are now registered and can login")
    			return redirect('mylogin')
    	else:
    		print('Password do not match,please enter again')
    		return redirect("register")
    else:
    	print("I am in GET request")
    	return render(request,'menu/register.html')
