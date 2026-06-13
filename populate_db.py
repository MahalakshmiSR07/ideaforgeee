import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ideaforge_project.settings')
django.setup()

from core.models import Project

projects_data = [
    {
        'title': 'AI Chatbot for Customer Support',
        'description': 'Build an intelligent chatbot using natural language processing to handle customer queries automatically.',
        'domain': 'AI',
        'technology': 'Python',
        'difficulty': 'Intermediate',
        'estimated_time': '3 weeks',
        'learning_resources': '1. TensorFlow tutorials\n2. NLTK documentation\n3. Rasa framework guide',
        'roadmap': 'Step 1: Data collection\nStep 2: Model training\nStep 3: Integration with a web interface'
    },
    {
        'title': 'Smart Home Automation System',
        'description': 'Create a system to control home appliances using voice commands or a mobile app.',
        'domain': 'IoT',
        'technology': 'Python',
        'difficulty': 'Advanced',
        'estimated_time': '1 month',
        'learning_resources': '1. Raspberry Pi basics\n2. MQTT protocol guide\n3. Home Assistant docs',
        'roadmap': 'Step 1: Setup Raspberry Pi\nStep 2: Connect sensors\nStep 3: Build a dashboard'
    },
    {
        'title': 'Personal Portfolio Website',
        'description': 'Design and develop a personal portfolio website to showcase your projects and skills.',
        'domain': 'Web',
        'technology': 'JavaScript',
        'difficulty': 'Beginner',
        'estimated_time': '1 week',
        'learning_resources': '1. HTML/CSS basics\n2. React or Vue.js tutorials\n3. CSS animations guide',
        'roadmap': 'Step 1: Sketch design\nStep 2: Build HTML structure\nStep 3: Add CSS styling\nStep 4: Deploy on Vercel/GitHub Pages'
    },
    {
        'title': 'E-commerce Platform Backend',
        'description': 'Develop a robust backend for an e-commerce platform including user authentication, product catalog, and payment processing.',
        'domain': 'Web',
        'technology': 'Java',
        'difficulty': 'Advanced',
        'estimated_time': '2 months',
        'learning_resources': '1. Spring Boot documentation\n2. Stripe API guide\n3. PostgreSQL tutorials',
        'roadmap': 'Step 1: DB schema design\nStep 2: Setup Spring Boot\nStep 3: Implement Auth\nStep 4: Payment gateway integration'
    },
    {
        'title': 'Machine Learning Image Classifier',
        'description': 'Train a model to classify images into different categories (e.g., cats vs. dogs).',
        'domain': 'AI',
        'technology': 'Python',
        'difficulty': 'Beginner',
        'estimated_time': '2 weeks',
        'learning_resources': '1. PyTorch basics\n2. Fast.ai course\n3. Kaggle datasets',
        'roadmap': 'Step 1: Gather dataset\nStep 2: Preprocess images\nStep 3: Train CNN\nStep 4: Evaluate model'
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

def populate():
    Project.objects.all().delete()
    for data in projects_data:
        data['roadmap'] = generate_detailed_roadmap(
            data['title'], data['technology'], data['domain'], data['difficulty']
        )
        Project.objects.create(**data)
    print("Database populated with sample projects.")

if __name__ == '__main__':
    populate()
