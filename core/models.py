from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    preferred_domain = models.CharField(max_length=100, blank=True, null=True)
    preferred_technology = models.CharField(max_length=100, blank=True, null=True)
    preferred_difficulty = models.CharField(max_length=50, blank=True, null=True)
    
    # New Fields for Dashboard
    bio = models.TextField(blank=True, null=True, help_text="Short professional bio")
    usn = models.CharField(max_length=50, blank=True, null=True, verbose_name="USN/Roll Number")
    college = models.CharField(max_length=200, blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    
    # Quiz Metrics
    quiz_score = models.IntegerField(default=0)
    total_quizzes = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    domain = models.CharField(max_length=100)  # e.g., AI, Web, IoT
    technology = models.CharField(max_length=100) # e.g., Python, Java
    difficulty = models.CharField(max_length=50) # e.g., Beginner, Intermediate, Advanced
    estimated_time = models.CharField(max_length=100) # e.g., "2 weeks"
    learning_resources = models.TextField() # e.g., links or text
    roadmap = models.TextField() # e.g., step by step guide
    
    def __str__(self):
        return self.title

class SavedProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'project')
        
    def __str__(self):
        return f"{self.user.username} saved {self.project.title}"

class PasswordResetOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"OTP for {self.user.email}"
