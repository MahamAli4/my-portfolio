import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from portfolio.models import Skill, Education, Experience
from projects.models import Project

def populate_data():
    print("Clearing existing data...")
    Skill.objects.all().delete()
    Education.objects.all().delete()
    Experience.objects.all().delete()
    
    print("Populating Skills...")
    skills_data = [
        # Graphic Design Tools
        {'name': 'Adobe Photoshop', 'category': 'tools', 'proficiency': 90, 'icon': 'fa-solid fa-paintbrush', 'description': 'Photo editing and manipulation'},
        {'name': 'Adobe Illustrator', 'category': 'tools', 'proficiency': 85, 'icon': 'fa-solid fa-pen-nib', 'description': 'Vector graphics and illustration'},
        {'name': 'Canva', 'category': 'tools', 'proficiency': 95, 'icon': 'fa-solid fa-palette', 'description': 'Quick design and layout'},
        {'name': 'AI Tools & Websites', 'category': 'tools', 'proficiency': 80, 'icon': 'fa-solid fa-robot', 'description': 'AI-assisted design'},
        
        # Graphic Design Types
        {'name': 'Product Design', 'category': 'frontend', 'proficiency': 80, 'icon': 'fa-solid fa-box-open', 'description': ''},
        {'name': 'Product Packaging', 'category': 'frontend', 'proficiency': 75, 'icon': 'fa-solid fa-box', 'description': ''},
        {'name': 'Web Page Design', 'category': 'frontend', 'proficiency': 85, 'icon': 'fa-solid fa-laptop-code', 'description': 'UI Design'},
        {'name': 'Banner Design', 'category': 'frontend', 'proficiency': 90, 'icon': 'fa-solid fa-image', 'description': ''},
        {'name': 'Flyers', 'category': 'frontend', 'proficiency': 90, 'icon': 'fa-solid fa-file-image', 'description': ''},
        {'name': 'Brochure', 'category': 'frontend', 'proficiency': 90, 'icon': 'fa-solid fa-book-open', 'description': ''},
        {'name': 'Social Media Post Design', 'category': 'frontend', 'proficiency': 95, 'icon': 'fa-solid fa-hashtag', 'description': ''},
        {'name': 'Resume', 'category': 'frontend', 'proficiency': 85, 'icon': 'fa-solid fa-file-alt', 'description': ''},
        {'name': 'eBook Cover', 'category': 'frontend', 'proficiency': 80, 'icon': 'fa-solid fa-book', 'description': ''},
        {'name': 'KDP Book Designing', 'category': 'frontend', 'proficiency': 75, 'icon': 'fa-solid fa-swatchbook', 'description': ''},
        {'name': 'Picture Editing', 'category': 'frontend', 'proficiency': 90, 'icon': 'fa-solid fa-camera', 'description': ''},
        {'name': 'Mockup Designs', 'category': 'frontend', 'proficiency': 85, 'icon': 'fa-solid fa-mobile-alt', 'description': ''},
        {'name': '3D Logo & Vector Design', 'category': 'frontend', 'proficiency': 80, 'icon': 'fa-solid fa-cube', 'description': ''},

        # Microsoft Office
        {'name': 'MS Word', 'category': 'tools', 'proficiency': 95, 'icon': 'fa-solid fa-file-word', 'description': ''},
        {'name': 'MS Excel', 'category': 'tools', 'proficiency': 90, 'icon': 'fa-solid fa-file-excel', 'description': ''},
        {'name': 'MS Publisher', 'category': 'tools', 'proficiency': 85, 'icon': 'fa-solid fa-newspaper', 'description': ''},

        # Web Development
        {'name': 'HTML', 'category': 'frontend', 'proficiency': 95, 'icon': 'fa-brands fa-html5', 'description': 'Semantic markup'},
        {'name': 'CSS 3', 'category': 'frontend', 'proficiency': 90, 'icon': 'fa-brands fa-css3-alt', 'description': 'Responsive styling'},
        {'name': 'JavaScript & ES6', 'category': 'frontend', 'proficiency': 85, 'icon': 'fa-brands fa-js', 'description': 'Interactive logic'},
        {'name': 'Tailwind CSS', 'category': 'frontend', 'proficiency': 80, 'icon': 'fa-solid fa-wind', 'description': 'Utility-first CSS'},
        {'name': 'Bootstrap', 'category': 'frontend', 'proficiency': 85, 'icon': 'fa-brands fa-bootstrap', 'description': 'Responsive framework'},
        {'name': 'Typescript', 'category': 'frontend', 'proficiency': 75, 'icon': 'fa-brands fa-js', 'description': 'Type-safe JavaScript'},
        {'name': 'React.js', 'category': 'frontend', 'proficiency': 80, 'icon': 'fa-brands fa-react', 'description': 'Component-based UI'},
        {'name': 'Next.js', 'category': 'frontend', 'proficiency': 75, 'icon': 'fa-solid fa-n', 'description': 'React Framework'},
        {'name': 'Supabase', 'category': 'backend', 'proficiency': 70, 'icon': 'fa-solid fa-database', 'description': 'Backend as a Service'},
        {'name': 'Node.js', 'category': 'backend', 'proficiency': 75, 'icon': 'fa-brands fa-node', 'description': 'Server-side JavaScript'},
        {'name': 'Express.js', 'category': 'backend', 'proficiency': 75, 'icon': 'fa-brands fa-node-js', 'description': 'Web framework'},
        {'name': 'MongoDB', 'category': 'database', 'proficiency': 75, 'icon': 'fa-brands fa-envira', 'description': 'NoSQL Database'},
        {'name': 'GraphQL', 'category': 'backend', 'proficiency': 65, 'icon': 'fa-solid fa-project-diagram', 'description': 'API Query Language'},
        {'name': 'Websocket / socket.ai', 'category': 'backend', 'proficiency': 60, 'icon': 'fa-solid fa-plug', 'description': 'Real-time communication'},
        {'name': 'Git/Github', 'category': 'tools', 'proficiency': 85, 'icon': 'fa-brands fa-git-alt', 'description': 'Version Control'},
        {'name': 'Python', 'category': 'backend', 'proficiency': 70, 'icon': 'fa-brands fa-python', 'description': 'General purpose programming'},
    ]
    
    for skill in skills_data:
        Skill.objects.create(**skill)
        
    print("Populating Experience...")
    experiences = [
        {
            'position': 'Internal Internship',
            'company': 'AIT',
            'duration': 'Recent',
            'description': 'Gaining practical industry experience and applying skills in real-world projects.',
            'order': 1
        },
        {
            'position': 'Arabic Grammar Teacher',
            'company': 'Self-Employed / Institute',
            'duration': '3 Years',
            'description': 'Taught Arabic grammar, mentoring students and strengthening communication skills.',
            'order': 2
        },
        {
            'position': 'Microsoft Office Specialist',
            'company': 'Various',
            'duration': '2 Years',
            'description': 'Extensive experience with MS Word, MS Excel, and MS Publisher.',
            'order': 3
        },
        {
            'position': 'Graphic Designer',
            'company': 'Freelance / Various',
            'duration': '2 Years',
            'description': 'Experience in Logo Design, Vector Design, Mockup Designs, Picture Editing, Book Designing (KDP), Brochures, Flyers, etc.',
            'order': 4
        },
        {
            'position': 'Jewelry Making',
            'company': 'Self-Employed',
            'duration': '1 Year',
            'description': 'Creative jewelry design and creation.',
            'order': 5
        }
    ]
    
    for exp in experiences:
        Experience.objects.create(**exp)

    print("Populating Education...")
    education = [
        {
            'degree': 'Full Stack Web Development',
            'institution': 'SMIT (Saylani Mass IT Training)',
            'year': 'Completed',
            'description': 'Comprehensive training in MERN Stack and web technologies.',
            'order': 1
        },
        {
            'degree': 'Frontend Web Development',
            'institution': 'Desk Skill',
            'year': 'Completed',
            'description': 'Focus on HTML, CSS, JavaScript and responsive design.',
            'order': 2
        },
        {
            'degree': 'Master of Arabic Language',
            'institution': 'Karachi University',
            'year': 'Completed',
            'description': 'Advanced studies in Arabic language and literature.',
            'order': 3
        },
        {
            'degree': 'Shahadat ul ailmia',
            'institution': 'Tanzim ul Madaris',
            'year': 'Completed',
            'description': 'Advanced Islamic studies.',
            'order': 4
        }
    ]
    
    for edu in education:
        Education.objects.create(**edu)
        
    print("Data population complete!")

if __name__ == '__main__':
    populate_data()
