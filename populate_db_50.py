import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ideaforge_project.settings')
django.setup()

from core.models import Project

domains = ['AI', 'Web', 'IoT', 'Mobile', 'Data Science', 'Cybersecurity', 'Game Dev']
technologies = ['Python', 'JavaScript', 'Java', 'C++', 'Go', 'Ruby', 'Swift', 'Kotlin', 'React', 'Node.js']
difficulties = ['Beginner', 'Intermediate', 'Advanced']

templates = [
    {
        'title': '{} based {} App',
        'desc': 'Build a comprehensive {} application focusing on {} techniques to solve real-world problems.',
        'roadmap': '### Phase 1: Planning\n- Define requirements\n- Wireframing\n\n### Phase 2: Development\n- Set up the {} environment\n- Implement core logic\n- Build UI/UX\n\n### Phase 3: Deployment\n- Testing and QA\n- Deploy to cloud (AWS/Heroku)',
        'resources': '- [freeCodeCamp {} Tutorial](https://www.freecodecamp.org/)\n- [Official {} Documentation](https://developer.mozilla.org/)\n- [YouTube Crash Course](https://www.youtube.com/)'
    },
    {
        'title': 'Intelligent {} System using {}',
        'desc': 'An automated system leveraging {} for {} capabilities. This project will challenge your {} skills.',
        'roadmap': '### Step 1: Setup\n- Install dependencies\n- Configure database\n\n### Step 2: Core Algorithm\n- Write the {} processing logic\n- Handle edge cases\n\n### Step 3: Finalization\n- Code review\n- Publish to GitHub',
        'resources': '- [{} Full Course](https://www.coursera.org/)\n- [Medium Article on {}](https://medium.com/)\n- [StackOverflow tag: {}](https://stackoverflow.com/)'
    }
]

def generate_projects():
    Project.objects.all().delete()
    projects_created = 0
    
    # Let's define some specific, high-quality projects first, then randomly generate the rest.
    high_quality = [
        {
            'title': 'AI-Powered Resume Screener',
            'description': 'A tool that parses resumes (PDF/DOCX) using NLP and ranks them against a job description using cosine similarity.',
            'domain': 'AI',
            'technology': 'Python',
            'difficulty': 'Intermediate',
            'estimated_time': '3 weeks',
            'learning_resources': '<ul><li><a href="https://www.nltk.org/" target="_blank">NLTK Documentation</a></li><li><a href="https://spacy.io/usage/spacy-101" target="_blank">spaCy 101 Tutorial</a></li><li><a href="https://towardsdatascience.com/resume-screening-with-python-1dea360be49b" target="_blank">Towards Data Science Guide</a></li></ul>',
            'roadmap': '<h5>Milestone 1: Text Extraction</h5><p>Extract text from PDFs using PyPDF2.</p><h5>Milestone 2: NLP Processing</h5><p>Tokenize and remove stop words using spaCy.</p><h5>Milestone 3: Matching Logic</h5><p>Implement TF-IDF and cosine similarity to compare resume text with job descriptions.</p>'
        },
        {
            'title': 'Real-time Collaborative Code Editor',
            'description': 'A web-based code editor where multiple users can type simultaneously. Features syntax highlighting and live cursors.',
            'domain': 'Web',
            'technology': 'JavaScript',
            'difficulty': 'Advanced',
            'estimated_time': '1 month',
            'learning_resources': '<ul><li><a href="https://socket.io/get-started/chat" target="_blank">Socket.io Basics</a></li><li><a href="https://codemirror.net/" target="_blank">CodeMirror Documentation</a></li><li><a href="https://www.freecodecamp.org/news/build-a-collaborative-text-editor-using-websockets/" target="_blank">freeCodeCamp WebSockets Guide</a></li></ul>',
            'roadmap': '<h5>Milestone 1: Frontend Setup</h5><p>Initialize React and CodeMirror.</p><h5>Milestone 2: WebSocket Server</h5><p>Setup Node.js with Socket.io.</p><h5>Milestone 3: Sync Logic</h5><p>Broadcast code changes and cursor positions to all connected clients.</p>'
        },
        {
            'title': 'Smart Agriculture IoT Monitor',
            'description': 'A dashboard that reads soil moisture, temperature, and humidity from sensors connected to a Raspberry Pi or Arduino.',
            'domain': 'IoT',
            'technology': 'Python',
            'difficulty': 'Intermediate',
            'estimated_time': '4 weeks',
            'learning_resources': '<ul><li><a href="https://projects.raspberrypi.org/en" target="_blank">Raspberry Pi Projects</a></li><li><a href="https://randomnerdtutorials.com/esp32-mqtt-publish-subscribe-arduino-ide/" target="_blank">MQTT with ESP32</a></li></ul>',
            'roadmap': '<h5>Milestone 1: Hardware Assembly</h5><p>Connect sensors to GPIO pins.</p><h5>Milestone 2: Data Collection</h5><p>Write Python scripts to read sensor data.</p><h5>Milestone 3: Dashboard</h5><p>Send data via MQTT to a local web dashboard.</p>'
        }
    ]
    
    for hq in high_quality:
        Project.objects.create(**hq)
        projects_created += 1

    # Generate the remaining to reach 55
    words = ['Manager', 'Analyzer', 'Tracker', 'Bot', 'Dashboard', 'Engine', 'Platform', 'Simulator']
    
    for i in range(52):
        domain = random.choice(domains)
        tech = random.choice(technologies)
        diff = random.choice(difficulties)
        word = random.choice(words)
        tmpl = random.choice(templates)
        
        title = f"{tech} {word} for {domain}" if random.random() > 0.5 else tmpl['title'].format(tech, domain)
        desc = tmpl['desc'].format(domain, tech, tech, domain, tech)
        
        roadmap_html = f"<h5>Phase 1: Setup</h5><p>Install {tech} tools and prepare environment.</p><h5>Phase 2: Build</h5><p>Develop the {domain} logic.</p><h5>Phase 3: Deploy</h5><p>Host on Vercel or AWS.</p>"
        
        resources_html = f"<ul><li><a href='https://www.youtube.com/results?search_query={tech}+tutorial' target='_blank'>YouTube: {tech} Full Tutorial</a></li><li><a href='https://www.google.com/search?q={domain}+best+practices' target='_blank'>Google: {domain} Best Practices</a></li><li><a href='https://freecodecamp.org' target='_blank'>freeCodeCamp Guide</a></li></ul>"
        
        Project.objects.create(
            title=title,
            description=desc,
            domain=domain,
            technology=tech,
            difficulty=diff,
            estimated_time=f"{random.randint(1, 8)} weeks",
            learning_resources=resources_html,
            roadmap=roadmap_html
        )
        projects_created += 1

    print(f"Database populated with {projects_created} projects.")

if __name__ == '__main__':
    generate_projects()
