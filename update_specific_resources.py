import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ideaforge_project.settings')
django.setup()

from core.models import Project

# High-quality, free, specific learning resources for technologies
TECH_RESOURCES = {
    'Python': 'https://www.freecodecamp.org/learn/scientific-computing-with-python/',
    'JavaScript': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide',
    'Java': 'https://java-programming.mooc.fi/',
    'Kotlin': 'https://developer.android.com/courses/android-basics-kotlin/course',
    'Rust': 'https://doc.rust-lang.org/book/',
    'React Native': 'https://reactnative.dev/docs/getting-started',
    'Kubernetes': 'https://kubernetes.io/docs/tutorials/',
    'Solidity': 'https://cryptozombies.io/',
    'Swift': 'https://developer.apple.com/tutorials/swiftui',
    'Go': 'https://go.dev/tour/welcome/1',
    'TensorFlow': 'https://www.tensorflow.org/tutorials',
    'C++': 'https://www.learncpp.com/',
    'PHP': 'https://phptherightway.com/',
    'Docker': 'https://docs.docker.com/get-started/',
    'Unity': 'https://learn.unity.com/'
}

# High-quality, free, specific learning resources for domains
DOMAIN_RESOURCES = {
    'Web': 'https://roadmap.sh/frontend',
    'AI': 'https://course.fast.ai/',
    'IoT': 'https://docs.arduino.cc/learn/',
    'Cybersecurity': 'https://tryhackme.com/',
    'Mobile': 'https://roadmap.sh/android',
    'Data Science': 'https://www.kaggle.com/learn',
    'Game Dev': 'https://learn.unity.com/pathway/junior-programmer',
    'Cloud Computing': 'https://aws.amazon.com/training/digital/',
    'AR/VR': 'https://learn.unity.com/course/create-with-vr',
    'Embedded Systems': 'https://www.coursera.org/learn/iot',
    'Blockchain': 'https://ethereum.org/en/developers/docs/',
    'DevOps': 'https://roadmap.sh/devops'
}

def update_specific_resources():
    projects = Project.objects.all()
    count = 0
    for project in projects:
        tech = project.technology
        domain = project.domain
        
        tech_link = TECH_RESOURCES.get(tech, f'https://www.google.com/search?q={tech}+free+course')
        domain_link = DOMAIN_RESOURCES.get(domain, f'https://www.google.com/search?q={domain}+free+roadmap')
        
        resources = (
            f"<ul style='list-style-type: none; padding-left: 0;'>"
            f"<li style='margin-bottom: 12px;'><i class='fas fa-code text-primary me-2'></i><strong>Free {tech} Course:</strong> <br> <a href='{tech_link}' target='_blank' rel='noopener noreferrer' class='ms-4 text-decoration-none'>Interactive Guide / Official Tutorial for {tech}</a></li>"
            f"<li style='margin-bottom: 12px;'><i class='fas fa-layer-group text-success me-2'></i><strong>{domain} Learning Path:</strong> <br> <a href='{domain_link}' target='_blank' rel='noopener noreferrer' class='ms-4 text-decoration-none'>Industry Standard Roadmap for {domain}</a></li>"
            f"<li style='margin-bottom: 12px;'><i class='fab fa-youtube text-danger me-2'></i><strong>Project Walkthroughs:</strong> <br> <a href='https://www.youtube.com/results?search_query={domain}+project+with+{tech}+full+course' target='_blank' rel='noopener noreferrer' class='ms-4 text-decoration-none'>Free YouTube Tutorials for {tech} & {domain}</a></li>"
            f"</ul>"
        )
        
        project.learning_resources = resources
        project.save()
        count += 1
        
    print(f"Successfully updated learning resources with SPECIFIC FREE LINKS for {count} projects.")

if __name__ == '__main__':
    update_specific_resources()
