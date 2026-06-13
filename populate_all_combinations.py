import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ideaforge_project.settings')
django.setup()

from core.models import Project

def populate_all():
    domains = list(Project.objects.values_list('domain', flat=True).distinct())
    techs = list(Project.objects.values_list('technology', flat=True).distinct())
    diffs = list(Project.objects.values_list('difficulty', flat=True).distinct())

    if not domains:
        domains = ['Web', 'AI', 'IoT', 'Cybersecurity', 'Mobile']
    if not techs:
        techs = ['Python', 'JavaScript', 'Java', 'Kotlin', 'Rust']
    if not diffs:
        diffs = ['Beginner', 'Intermediate', 'Advanced']

    # We want to make sure EVERY combination exists.
    # To avoid creating too many duplicate projects if they already exist, we use get_or_create.
    
    count = 0
    for d in domains:
        for t in techs:
            for diff in diffs:
                # Check if it exists
                if not Project.objects.filter(domain=d, technology=t, difficulty=diff).exists():
                    title = f"{t} Project for {d} ({diff})"
                    description = f"An automated project idea for {d} using {t}. This project is tailored for {diff} level."
                    
                    Project.objects.create(
                        title=title,
                        description=description,
                        domain=d,
                        technology=t,
                        difficulty=diff,
                        estimated_time='2-4 weeks',
                        learning_resources=f'{t} documentation, {d} basics',
                        roadmap='Step 1: Setup\nStep 2: Build\nStep 3: Deploy'
                    )
                    count += 1
                    
    print(f"Successfully added {count} missing combinations to the database!")

if __name__ == '__main__':
    populate_all()
