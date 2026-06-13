import os
import django
import urllib.parse

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ideaforge_project.settings')
django.setup()

from core.models import Project

def update_resources():
    projects = Project.objects.all()
    count = 0
    for project in projects:
        tech = project.technology
        domain = project.domain
        
        # URL encode for safe search links
        tech_query = urllib.parse.quote(tech)
        domain_query = urllib.parse.quote(domain)
        
        # Construct helpful learning links using HTML because Django templates |safe expects HTML
        resources = (
            f"<ul>"
            f"<li><strong>Official Documentation:</strong> <a href='https://www.google.com/search?q={tech_query}+official+documentation' target='_blank'>Learn more about {tech}</a> - The best place to start understanding the core concepts of the language.</li>"
            f"<li><strong>Domain Fundamentals:</strong> <a href='https://www.google.com/search?q={domain_query}+fundamentals+and+basics' target='_blank'>Introduction to {domain}</a> - Essential reading to grasp the domain requirements.</li>"
            f"<li><strong>Video Tutorials:</strong> <a href='https://www.youtube.com/results?search_query=how+to+build+{domain_query}+app+with+{tech_query}' target='_blank'>Build a {domain} project with {tech} on YouTube</a> - Step-by-step visual guides.</li>"
            f"<li><strong>Community & Troubleshooting:</strong> <a href='https://stackoverflow.com/questions/tagged/{tech_query.lower()}' target='_blank'>StackOverflow tag for {tech}</a> - Where to ask questions when you get stuck.</li>"
            f"</ul>"
        )
        
        project.learning_resources = resources
        project.save()
        count += 1
        
    print(f"Successfully updated learning resources with HTML links for {count} projects.")

if __name__ == '__main__':
    update_resources()
