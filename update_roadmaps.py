import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ideaforge_project.settings')
django.setup()

from core.models import Project

def update_roadmaps():
    projects = Project.objects.all()
    count = 0
    for project in projects:
        title = project.title
        tech = project.technology
        domain = project.domain
        difficulty = project.difficulty
        
        roadmap = (
            f"### Phase 1: Research, Design, and Environment Setup\n"
            f"- **Understand the Concepts:** Review key architecture patterns for building a {domain} application using {tech}.\n"
            f"- **System Requirements:** Create a list of essential features and outline the user flows / API endpoints.\n"
            f"- **Tech Stack Installation:** Initialize a local project repository. Install {tech} runtime and define necessary configuration files.\n"
            f"- **Database Design:** Map out the database schema (tables, models, attributes) appropriate for a {difficulty}-level project.\n\n"
            
            f"### Phase 2: Core Feature Implementation\n"
            f"- **Database Models & Migrations:** Write the {tech} models, define relationships, and run initial database migrations.\n"
            f"- **Logic & Services Layer:** Implement the main algorithms and business logic supporting the {title} features.\n"
            f"- **Server-Side API/Routing:** Build clean, well-tested routes and endpoints to query, create, update, and delete data.\n"
            f"- **Frontend Skeleton:** Set up the basic structural pages/views, keeping in mind responsive layout principles.\n\n"
            
            f"### Phase 3: UI Enhancement and System Integration\n"
            f"- **Styling & Responsive Design:** Apply cohesive, modern styling. Ensure a premium look on mobile and desktop.\n"
            f"- **Form Validations:** Implement client-side and server-side forms validation to prevent bugs or empty requests.\n"
            f"- **Interactive Elements:** Integrate user feedback cues like loading spinners, transition micro-animations, and confirmation modal alerts.\n"
            f"- **Auth & Security:** Add secure login/registration guards to sensitive routes if required for a {difficulty} level.\n\n"
            
            f"### Phase 4: Testing, Optimization, and Deployment\n"
            f"- **Troubleshooting & QA:** Perform comprehensive end-to-end user-testing. Debug console errors, broken links, or edge-case input crashes.\n"
            f"- **Performance Tuning:** Optimize database queries, minify assets, and remove redundant log statements.\n"
            f"- **Live Deployment:** Deploy the finalized {tech} app to a modern hosting service (e.g., Vercel, Render, GitHub Pages, or Heroku).\n"
            f"- **GitHub Documentation:** Write a highly descriptive README.md file highlighting setup guides, tech stack badges, and usage screenshots."
        )
        
        project.roadmap = roadmap
        project.save()
        count += 1
        
    print(f"Successfully updated roadmaps for {count} projects in the database!")

if __name__ == '__main__':
    update_roadmaps()
