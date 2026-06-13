import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ideaforge_project.settings')
django.setup()

from core.models import Project

domains = [
    'AI', 'Web', 'IoT', 'Mobile', 'Data Science', 'Cybersecurity', 'Game Dev',
    'DevOps', 'Blockchain', 'Cloud Computing', 'Embedded Systems', 'AR/VR'
]

technologies = [
    'Python', 'JavaScript', 'Java', 'C++', 'Go', 'Ruby', 'Swift', 'Kotlin', 'React', 'Node.js',
    'Rust', 'PHP', 'Angular', 'Vue.js', 'SQL', 'C#', 'Unity', 'React Native', 'Flutter',
    'Docker', 'Kubernetes', 'Solidity', 'TensorFlow', 'PyTorch', 'Unreal Engine', 'Arduino'
]

difficulties = ['Beginner', 'Intermediate', 'Advanced']

templates = [
    {
        'title': '{} based {} App',
        'desc': 'Build a comprehensive {} application focusing on {} techniques to solve real-world problems. Perfect for practicing your {} skills.',
        'roadmap': '### Phase 1: Planning\n- Define requirements\n- Wireframing\n\n### Phase 2: Development\n- Set up the {} environment\n- Implement core logic\n- Build UI/UX\n\n### Phase 3: Deployment\n- Testing and QA\n- Deploy to production',
        'resources': '<ul><li><a href="https://www.freecodecamp.org/" target="_blank">freeCodeCamp {} Tutorial</a></li><li><a href="https://developer.mozilla.org/" target="_blank">Official Documentation</a></li><li><a href="https://www.youtube.com/results?search_query={}+course" target="_blank">YouTube Crash Course</a></li></ul>'
    },
    {
        'title': 'Intelligent {} System using {}',
        'desc': 'An automated system leveraging {} for {} capabilities. This project will heavily challenge your {} skills and architecture design.',
        'roadmap': '### Step 1: Setup\n- Install dependencies\n- Configure database\n\n### Step 2: Core Algorithm\n- Write the {} processing logic\n- Handle edge cases\n\n### Step 3: Finalization\n- Code review\n- Publish to GitHub',
        'resources': '<ul><li><a href="https://www.coursera.org/" target="_blank">Coursera {} Full Course</a></li><li><a href="https://medium.com/search?q={}" target="_blank">Medium Articles</a></li><li><a href="https://stackoverflow.com/questions/tagged/{}" target="_blank">StackOverflow discussions</a></li></ul>'
    },
    {
        'title': '{} {} Automation Tool',
        'desc': 'A powerful script/tool built in {} to automate redundant {} workflows, dramatically improving productivity.',
        'roadmap': '### Milestone 1: CLI Interface\n- Build the command line interface.\n\n### Milestone 2: Automation Logic\n- Implement the core {} scripts.\n\n### Milestone 3: Distribution\n- Package the tool for others to install.',
        'resources': '<ul><li><a href="https://github.com/topics/{}" target="_blank">GitHub {} Projects</a></li><li><a href="https://www.youtube.com/" target="_blank">YouTube Guides</a></li></ul>'
    }
]

def generate_detailed_roadmap(title, tech, domain, difficulty):
    return (
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

def generate_projects():
    Project.objects.all().delete()
    projects_created = 0
    
    words = ['Manager', 'Analyzer', 'Tracker', 'Bot', 'Dashboard', 'Engine', 'Platform', 'Simulator', 'Hub', 'Network', 'API', 'Generator']
    
    # We want at least 150 projects
    for i in range(160):
        domain = random.choice(domains)
        tech = random.choice(technologies)
        diff = random.choice(difficulties)
        word = random.choice(words)
        tmpl = random.choice(templates)
        
        # Decide title randomly
        title_type = random.randint(1, 3)
        if title_type == 1:
            title = f"{tech} {word} for {domain}"
        elif title_type == 2:
            title = f"{domain} {word} built with {tech}"
        else:
            if '{}' in tmpl['title']:
                try:
                    title = tmpl['title'].format(tech, domain)
                except:
                    title = f"{tech} {word} for {domain}"
            else:
                title = f"{tech} {word} for {domain}"

        # Desc
        try:
            desc = tmpl['desc'].format(domain, tech, tech, domain, tech)
        except:
            desc = f"A {diff} level project focusing on {tech} and {domain}."
            
        # Roadmap
        roadmap = generate_detailed_roadmap(title, tech, domain, diff)
            
        # Resources
        try:
            resources = tmpl['resources'].format(tech, tech, tech)
        except:
            resources = f"<ul><li><a href='https://www.google.com/search?q={tech}+tutorial' target='_blank'>Search {tech} Tutorials</a></li></ul>"
        
        Project.objects.create(
            title=title,
            description=desc,
            domain=domain,
            technology=tech,
            difficulty=diff,
            estimated_time=f"{random.randint(1, 12)} weeks",
            learning_resources=resources,
            roadmap=roadmap
        )
        projects_created += 1

    print(f"Database populated with {projects_created} projects.")

if __name__ == '__main__':
    generate_projects()
