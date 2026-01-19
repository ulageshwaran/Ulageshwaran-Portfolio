from django.core.management.base import BaseCommand
from portfolio.models import Project, Skill, Experience, Tag, Education, Certification, Achievement
from datetime import date

class Command(BaseCommand):
    help = 'Populates the database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Cleaning old data...')
        Project.objects.all().delete()
        Skill.objects.all().delete()
        Experience.objects.all().delete()
        Tag.objects.all().delete()
        Education.objects.all().delete()
        Certification.objects.all().delete()
        Achievement.objects.all().delete()

        self.stdout.write('Seeding data...')

        # Skills
        skills_data = {
            'FRONTEND': ['HTML5', 'CSS3', 'JavaScript', 'Bootstrap', 'Responsive Design'],
            'BACKEND': ['Python', 'Django', 'REST API', 'MySQL', 'SQLite'],
            'TOOLS': ['Git & GitHub', 'VS Code', 'AWS', 'Version Control']
        }

        for category, names in skills_data.items():
            for name in names:
                Skill.objects.create(name=name, category=category, proficiency=80) # Default proficiency

        # Tags
        tag_django = Tag.objects.create(name='Django')
        tag_python = Tag.objects.create(name='Python')
        tag_js = Tag.objects.create(name='JavaScript')
        tag_css = Tag.objects.create(name='CSS3')
        tag_html = Tag.objects.create(name='HTML5')
        tag_bootstrap = Tag.objects.create(name='Bootstrap')
        tag_aws = Tag.objects.create(name='AWS')
        tag_mysql = Tag.objects.create(name='MySQL')
        tag_ajax = Tag.objects.create(name='AJAX')

        # Projects
        p1 = Project.objects.create(
            title='WABI Clothing - E-Commerce Platform',
            description='A professional, responsive, and fully operational online clothing store. Features include fully functional shopping cart, secure user authentication, complete checkout process, and dynamic product listing.',
            link='https://wabiclothing.com',
            github_link='',
            image='projects/wabi_clothing.png'
        )
        p1.tags.add(tag_django, tag_python, tag_js, tag_bootstrap, tag_aws, tag_mysql, tag_ajax)

        p2 = Project.objects.create(
            title='Developer Portfolio Website',
            description='A modern, interactive portfolio website featuring a space-themed design with animated constellation effects. Built to showcase projects, skills, and professional journey.',
            link='', # Self link?
            github_link='',
            image='projects/portfolio.png'
        )
        p2.tags.add(tag_django, tag_html, tag_css, tag_js)

        # Experience (None provided in "Experience" section specifically other than projects, but "What I Do" implies freelancer/student work. 
        # The user listed projects as experiences. I will treat the E-commerce project as an "Experience" if meaningful, but since they have a "Projects" section,
        # I will leave Experience empty or put a placeholder if they have actual job experience. 
        # Looking at "Experience" section in prompt: user listed "Resume/Experience" section content as "Projects".
        # Actually, under "Projects Section" they are listed.
        # Background story says "Currently pursuing Master's". 
        # I'll add "Full-Stack Web Developer" as a role description based on "What I Do" or maybe leave it empty if no formal employment.
        # User title: "Aspiring Software Development Engineer".
        # Let's add the Internships/Freelance if implied, but for now I will add their Education as the main timeline items if Experience is empty, OR just leave Experience section for actual jobs.
        # Wait, the prompt has a "Experience" section in the requested fields, but the user provided "Projects".
        # "Experience" model might be better suited for the "Availability" section: "Open to internships..."
        # Actually, let's use the layout: Projects in Projects section. Experience section can be "Education" + "Work".
        # I'll stick to the model. I won't create fake experience.
        
        # Education
        Education.objects.create(
            institution='SRM IST FSH - Kattankulathur',
            degree='M.Sc in Information Technology',
            duration='2024 - 2026',
            score='CGPA: 7.45/10',
            status='Currently Pursuing'
        )
        Education.objects.create(
            institution='SRM Institute of Science and Technology, Chennai',
            degree='B.Sc in Computer Science',
            duration='2024', # Year of completion
            score='Percentage: 81.3%',
            status='Completed'
        )

        # Certifications
        Certification.objects.create(
            title='Python Full Stack Development',
            issuer='TAAS Academy',
            status='Completed',
            skills='Full-stack development, Python, Django, Frontend technologies'
        )
        Certification.objects.create(
            title='Django Application Development with SQL and Database',
            issuer='IBM',
            certificate_id='ULC463BBU72O',
            date=date(2025, 9, 1), # Future date in prompt? "September 2025". Okay.
            skills='Django framework, SQL, Database management'
        )

        # Achievements
        Achievement.objects.create(
            event='Club Inferno',
            position='3rd Place',
            date=date(2024, 9, 1),
            description='Successfully competed against multiple college teams, demonstrating problem-solving and development skills under time constraints'
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))
