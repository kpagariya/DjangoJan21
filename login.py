def loginmenu(request):
    #return HttpResponse('<h1>Hello, I am learning Django!</h1>')
    # Steps
    # 1. Retrieve input entered by User by using request parameter
    # 2. Authenticate the User by passing username/password
    # 3. If success then return to Home page else show the error and ask for relogin
    if request.method == 'POST':
    	print("I am in POST request")
    	# Pass the field name to get the input value
    	unameEntered=request.POST['username']
    	passEntered=request.POST['password']
    	print("username :",unameEntered)
    	userObject = auth.authenticate(username=unameEntered, password=passEntered)

    	if userObject is not None:
    		# It create a session (Unique ID)
    		auth.login(request,userObject)
    		#messages.success(request, "You are now logged in")
    		print("User logged in")
    		return redirect('myhome')
    	else:
    		print("Username/password invalid")
    		return redirect("mylogin")
    else: 
    	return render(request,'menu/login.html')
