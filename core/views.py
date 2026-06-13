from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, ProjectForm
from .models import Project, SavedProject, UserProfile, PasswordResetOTP
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib import messages
import random

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form': form})

def landing(request):
    return render(request, 'core/landing.html')

def about(request):
    return render(request, 'core/about.html')


@login_required
def home(request):
    if request.user.is_staff:
        # Handle Project Addition directly from dashboard
        if request.method == 'POST' and 'add_project' in request.POST:
            form = ProjectForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = ProjectForm()

        # Admin Dashboard Logic
        user_count = User.objects.count()
        project_count = Project.objects.count()
        saved_count = SavedProject.objects.count()
        
        users = User.objects.all().order_by('-date_joined')
        projects = Project.objects.all().order_by('-id')
        bookmarks = SavedProject.objects.select_related('user', 'project').order_by('-saved_at')
        
        return render(request, 'core/admin_dashboard.html', {
            'user_count': user_count,
            'project_count': project_count,
            'saved_count': saved_count,
            'users': users,
            'projects': projects,
            'bookmarks': bookmarks,
            'form': form
        })
    else:
        # Redirect normal users to the new comprehensive dashboard
        return redirect('profile')

@user_passes_test(lambda u: u.is_staff)
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm()
    return render(request, 'core/add_project.html', {'form': form})

@login_required
def profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    saved_items = SavedProject.objects.filter(user=request.user).select_related('project')
    saved_projects = [item.project for item in saved_items]
    if request.method == 'POST':
        # Also handle new bio/links here if provided
        profile.preferred_domain = request.POST.get('domain', profile.preferred_domain)
        profile.preferred_technology = request.POST.get('technology', profile.preferred_technology)
        profile.preferred_difficulty = request.POST.get('difficulty', profile.preferred_difficulty)
        
        # New profile fields
        profile.bio = request.POST.get('bio', profile.bio)
        profile.usn = request.POST.get('usn', profile.usn)
        profile.college = request.POST.get('college', profile.college)
        profile.github_link = request.POST.get('github_link', profile.github_link)
        profile.linkedin_link = request.POST.get('linkedin_link', profile.linkedin_link)
        profile.save()
        
        return redirect('profile')
        
    explore_projects = Project.objects.order_by('?')[:10]
        
    return render(request, 'core/profile.html', {
        'profile': profile,
        'saved_projects': saved_projects,
        'explore_projects': explore_projects,
    })

import random

QUIZ_POOL = [
    {
        'text': 'What are you most passionate about creating?',
        'options': [
            {'val': 'Web_JavaScript_Beginner', 'label': 'Beautiful, colorful websites people can interact with easily.'},
            {'val': 'AI_Python_Beginner', 'label': 'Smart tools and bots that can think and analyze data.'},
            {'val': 'Game Dev_Mobile_Beginner', 'label': 'Fun, casual games or mobile apps to play on the go.'}
        ]
    },
    {
        'text': 'How much time can you realistically dedicate to learning and building this project?',
        'options': [
            {'val': 'Beginner_Web', 'label': 'Just a few hours on the weekend. I want quick and easy results.'},
            {'val': 'Intermediate_Python', 'label': 'A few weeks. I want to build something functional but manageable.'},
            {'val': 'Advanced_AI', 'label': 'Several months. I want to dive deep and build a true masterpiece.'}
        ]
    },
    {
        'text': 'Do you prefer working as part of a team or building something entirely on your own (solo)?',
        'options': [
            {'val': 'Python_Web_Beginner', 'label': 'Solo. I want to handle everything myself from start to finish.'},
            {'val': 'React_JavaScript_Beginner', 'label': 'Team. I prefer focusing purely on the visual/frontend side.'},
            {'val': 'Data Science_Java_Intermediate', 'label': 'Team. I prefer crunching data behind the scenes in the backend.'}
        ]
    },
    {
        'text': 'When you think of coding, what sounds the easiest and most fun to you right now?',
        'options': [
            {'val': 'Mobile_Beginner', 'label': 'Designing a simple mobile interface.'},
            {'val': 'Python_Beginner', 'label': 'Writing a short, fun script to automate a boring task.'},
            {'val': 'Web_Beginner', 'label': 'Putting together a basic webpage with pictures and text.'}
        ]
    },
    {
        'text': 'When you encounter an error or a bug, what is your first instinct?',
        'options': [
            {'val': 'Beginner_Web', 'label': 'Ask for help or search for the exact error online.'},
            {'val': 'Intermediate_Python', 'label': 'Try tweaking small parts of the code until it magically works.'},
            {'val': 'Advanced_Java', 'label': 'Read the error logs carefully and trace it back to the source.'}
        ]
    },
    {
        'text': 'When building an app, what do you care about the most?',
        'options': [
            {'val': 'Web_React_Beginner', 'label': 'How it looks. It has to be gorgeous and smooth.'},
            {'val': 'Data Science_Python_Intermediate', 'label': 'How it works. The logic and data must be flawless.'},
            {'val': 'Cybersecurity_Rust_Advanced', 'label': 'How secure it is. No one is hacking my application.'}
        ]
    },
    {
        'text': 'Which of these real-world apps would you love to build a clone of?',
        'options': [
            {'val': 'Mobile_Flutter_Intermediate', 'label': 'Instagram (Photos, scrolling, liking).'},
            {'val': 'Web_JavaScript_Intermediate', 'label': 'Spotify (Streaming audio, playlists).'},
            {'val': 'AI_Python_Advanced', 'label': 'ChatGPT (AI text generation and chatbots).'}
        ]
    },
    {
        'text': 'How do you prefer to learn new coding skills?',
        'options': [
            {'val': 'Beginner', 'label': 'Following a fun, step-by-step video tutorial.'},
            {'val': 'Intermediate', 'label': 'Reading through interactive documentation.'},
            {'val': 'Advanced', 'label': 'Jumping straight into the code and breaking things to see how they work.'}
        ]
    }
]

@login_required
def quiz(request):
    if request.method == 'POST':
        domain_scores = {'AI': 0, 'Web': 0, 'IoT': 0, 'Mobile': 0, 'Game Dev': 0, 'Data Science': 0}
        tech_scores = {'Python': 0, 'JavaScript': 0, 'Java': 0, 'C++': 0, 'React': 0, 'Rust': 0, 'Docker': 0, 'TensorFlow': 0, 'Unity': 0, 'PHP': 0}
        diff_scores = {'Beginner': 0, 'Intermediate': 0, 'Advanced': 0}
        
        answered_count = 0
        for key, val in request.POST.items():
            if key.startswith('q'):
                answered_count += 1
                parts = val.split('_')
                for part in parts:
                    if part in domain_scores: domain_scores[part] += 1
                    if part in tech_scores: tech_scores[part] += 1
                    if part in diff_scores: diff_scores[part] += 1
                    
        best_domain = max(domain_scores, key=domain_scores.get) if any(domain_scores.values()) else 'Web'
        best_tech = max(tech_scores, key=tech_scores.get) if any(tech_scores.values()) else 'JavaScript'
        best_diff = max(diff_scores, key=diff_scores.get) if any(diff_scores.values()) else 'Beginner'
        
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        profile.preferred_domain = best_domain
        profile.preferred_technology = best_tech
        profile.preferred_difficulty = best_diff
        
        # Update metrics (Max 10 questions)
        profile.total_quizzes += 1
        # Give a fun randomized score based on answers, between 7 and 10 since there's no "wrong" answer
        profile.quiz_score = random.randint(7, 10)
        profile.save()
        
        return redirect('recommendations')
        
    else:
        import copy
        # Use all available questions (up to 10 max)
        num_questions = min(len(QUIZ_POOL), 10)
        questions = copy.deepcopy(random.sample(QUIZ_POOL, num_questions))
        for idx, q in enumerate(questions):
            q['id'] = f'q{idx+1}'
        return render(request, 'core/quiz.html', {'questions': questions})

from django.db.models import Case, When, IntegerField, Value

@login_required
def recommendations(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if profile.preferred_domain or profile.preferred_technology or profile.preferred_difficulty:
        # Score projects based on how many preferences they match
        score = (
            Case(When(domain__icontains=profile.preferred_domain, then=1), default=0, output_field=IntegerField()) +
            Case(When(technology__icontains=profile.preferred_technology, then=1), default=0, output_field=IntegerField()) +
            Case(When(difficulty__icontains=profile.preferred_difficulty, then=1), default=0, output_field=IntegerField())
        )
        # Get projects that match at least one preference, sorted by best match
        projects = Project.objects.annotate(match_score=score).filter(match_score__gt=0).order_by('-match_score')[:20]
    else:
        # Fallback if no profile is set
        projects = Project.objects.all().order_by('?')[:20]
        
    return render(request, 'core/recommendations.html', {'projects': projects})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    saved = SavedProject.objects.filter(user=request.user, project=project).exists()
    return render(request, 'core/project_detail.html', {'project': project, 'saved': saved})

@login_required
def save_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    SavedProject.objects.get_or_create(user=request.user, project=project)
    return redirect('saved_projects')

@login_required
def remove_saved_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    SavedProject.objects.filter(user=request.user, project=project).delete()
    return redirect('saved_projects')

@login_required
def saved_projects(request):
    saved_items = SavedProject.objects.filter(user=request.user)
    projects = [item.project for item in saved_items]
    return render(request, 'core/saved_projects.html', {'projects': projects})

@login_required
def search(request):
    domain_filter = request.GET.get('domain', '')
    difficulty_filter = request.GET.get('difficulty', '')
    tech_filter = request.GET.get('technology', '')
    
    projects = Project.objects.all()
    
    # Apply strict AND filters from dropdowns
    if domain_filter:
        projects = projects.filter(domain__iexact=domain_filter)
    if tech_filter:
        projects = projects.filter(technology__iexact=tech_filter)
    if difficulty_filter:
        projects = projects.filter(difficulty__iexact=difficulty_filter)

            
    # 2. If NO filters were provided, just return a random sample
    if not (domain_filter or difficulty_filter or tech_filter):
        projects = projects.order_by('?')[:50]
        
    domains = Project.objects.values_list('domain', flat=True).distinct()
    techs = Project.objects.values_list('technology', flat=True).distinct()
    diffs = Project.objects.values_list('difficulty', flat=True).distinct()
        
    return render(request, 'core/search.html', {
        'projects': projects, 
        'domains': domains,
        'techs': techs,
        'diffs': diffs
    })

def password_reset_request(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        users = User.objects.filter(email=email)
        if users.exists():
            user = users.first()
            
            # Generate 6-digit OTP
            otp_code = f"{random.randint(100000, 999999)}"
            
            # Delete old OTPs for this user
            PasswordResetOTP.objects.filter(user=user).delete()
            
            # Save new OTP
            PasswordResetOTP.objects.create(user=user, otp=otp_code)
            
            # Send Email
            subject = "IdeaForge Password Reset - Your Verification Code"
            message = f"Hello {user.username},\n\nYour 6-digit verification code to reset your password is: {otp_code}\n\nThis code will expire in 15 minutes.\n\nIf you did not request this, please ignore this email."
            try:
                send_mail(
                    subject,
                    message,
                    'no-reply@ideaforge.com',
                    [email],
                    fail_silently=False,
                )
            except Exception as e:
                # Log email failure and show OTP in demo mode to prevent server timeout/502 Bad Gateway
                print(f"Error sending password reset email: {e}")
                messages.warning(
                    request,
                    f"Unable to send verification email due to SMTP connection issues. "
                    f"[Demo Mode] Your 6-digit OTP code is: {otp_code}"
                )
            
            request.session['reset_email'] = email
            return redirect('password_reset_verify')
        else:
            messages.error(request, "If that email is registered, an OTP has been sent.")
            
    return render(request, 'core/password_reset_form.html')

def password_reset_verify(request):
    email = request.session.get('reset_email')
    if not email:
        return redirect('password_reset')
        
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        users = User.objects.filter(email=email)
        if users.exists():
            user = users.first()
            otp_record = PasswordResetOTP.objects.filter(user=user).last()
            
            if otp_record:
                # Check expiration (15 minutes)
                time_diff = timezone.now() - otp_record.created_at
                if time_diff.total_seconds() > 900:
                    messages.error(request, "This OTP has expired. Please request a new one.")
                    return redirect('password_reset')
                    
                if otp_record.otp == entered_otp:
                    request.session['reset_user_id'] = user.id
                    return redirect('password_reset_confirm_custom')
                else:
                    messages.error(request, "Invalid OTP code. Please try again.")
            else:
                messages.error(request, "No OTP request found.")
                return redirect('password_reset')
                
    return render(request, 'core/password_reset_otp.html', {'email': email})

def password_reset_confirm_custom(request):
    user_id = request.session.get('reset_user_id')
    if not user_id:
        return redirect('password_reset')
        
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        if new_password and new_password == confirm_password:
            user = User.objects.get(id=user_id)
            user.set_password(new_password)
            user.save()
            
            # Clean up session and OTP
            PasswordResetOTP.objects.filter(user=user).delete()
            del request.session['reset_user_id']
            if 'reset_email' in request.session:
                del request.session['reset_email']
                
            messages.success(request, "Your password has been successfully reset! You can now log in.")
            return redirect('login')
        else:
            messages.error(request, "Passwords do not match. Please try again.")
            
    return render(request, 'core/password_reset_confirm.html')
