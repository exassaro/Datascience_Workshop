from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout    
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.db.models import Q
from django.core.cache import cache  # Import cache
from django.utils.timezone import now

# Create your views here.

# Home Page View with no cache
@never_cache
@login_required(login_url='login')
def HomePage(request):
    if request.user.is_superuser:
        return redirect('admin')
    # user=request.user.username
    
    return render(request, 'home.html')
    # return render(request, 'home.html',{"username":user})

# Signup Page
@never_cache
def SignupPage(request):
    if request.user.is_authenticated:
        return redirect('home')  
    error = ''
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        # Check if passwords match
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return render(request, 'signup.html')
        
        # Check if username already exists
        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already exists")
            return render(request, 'signup.html')
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return render(request, 'signup.html')
        
        # Create user if validations pass
        my_user = User.objects.create_user(uname, email, pass1)
        my_user.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login')
    
    return render(request, 'signup.html')


# Login Page
def LoginPage(request):
    # If the user is already authenticated, redirect to home page
    if request.user.is_authenticated:
        return redirect('home')

    # Define the lockout period (e.g., 5 minutes)
    lockout_time = 300  # seconds (5 minutes)

    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')

        # Create a unique key for each user attempting login
        cache_key = f"failed_login_attempts_{username}"
        attempts = cache.get(cache_key, 0)

        # Check if user is locked out
        if attempts >= 3:
            messages.error(request, "Too many failed attempts. Try again later.")
            return render(request, 'login.html')

        # Authenticate user
        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            login(request, user)
            cache.delete(cache_key)  # Reset failed attempts on successful login
            return redirect('home')
        else:
            attempts += 1
            cache.set(cache_key, attempts, lockout_time)  # Store attempt count with expiry
            messages.error(request, f"Invalid credentials. Attempt {attempts}/3")

            # If reached the limit, show lockout message
            if attempts >= 3:
                messages.error(request, "Too many failed attempts. You are temporarily blocked.")
    
    return render(request, 'login.html')

# Admin panel view
@login_required(login_url='login')
@never_cache
def admin_panel(request):
    if request.user.is_authenticated and request.user.is_superuser:
        search_query = request.GET.get('search', '')
        if search_query:
            users = User.objects.filter(
                Q(username__icontains=search_query) | Q(email__icontains=search_query)
            )
        else:
            users = User.objects.all()
        return render(request, 'admin.html', {'det': users})
    else:
        messages.error(request, "You do not have permission to access this page.")
        return redirect('login')


# Add user view
@login_required
def add_user(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            if not username or not email or not password:
                messages.error(request, "All fields are required to add a user.")
                return redirect('admin')

            if User.objects.filter(username=username).exists():
                messages.warning(request, "A user with this username already exists.")
                return redirect('admin')

            if User.objects.filter(email=email).exists():
                messages.warning(request, "A user with this email already exists.")
                return redirect('admin')

            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, f"User '{username}' has been successfully added.")
            return redirect('admin')
    else:
        messages.error(request, "You do not have permission to perform this action.")
        return redirect('login')


# Update user view
@login_required
def update_user(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')

            if not username or not email:
                messages.error(request, "Both name and email are required to update a user.")
                return redirect('admin')

            User.objects.filter(id=id).update(username=username, email=email)
            messages.success(request, f"User '{username}' has been successfully updated.")
            return redirect('admin')
    else:
        messages.error(request, "You do not have permission to perform this action.")
        return redirect('login')


# Delete user view
@login_required
def delete_user(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            try:
                user = User.objects.get(id=id)
                user.delete()
                messages.success(request, f"User '{user.username}' has been successfully deleted.")
                return redirect('admin')
            except User.DoesNotExist:
                messages.error(request, "The user you are trying to delete does not exist.")
                return redirect('admin')
    else:
        messages.error(request, "You do not have permission to perform this action.")
        return redirect('login')


# Logout view
@login_required
@never_cache
def LogoutPage(request):
    logout(request)
    messages.info(request, "You have been successfully logged out.")
    return redirect('login')
