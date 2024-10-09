from models import db, Book, Section, User, Role
from werkzeug.security import generate_password_hash
from datastorefile import datastore
from datetime import datetime

def initialize_sample_data():
    from main import app
    with app.app_context():
        db.create_all()
        
        datastore.find_or_create_role(name='user', description='This is the user role')
        datastore.find_or_create_role(name='librarian', description='This is the librarian role')
        db.session.commit()

        # Create librarian user if not exists
        if not datastore.find_user(email='librarian@email.com'):
            datastore.create_user(
            email='librarian@email.com',
            username='librarian',
            password=generate_password_hash('librarian'),
            roles=['librarian']
            )
        db.session.commit()


        # Sample sections
        sections = [
            Section(section_name="Fiction", description="Fictional works including novels, short stories, etc."),
            Section(section_name="Science", description="Books related to science and technology."),
            Section(section_name="History", description="Books on historical events and figures."),
            Section(section_name="Biography", description="Biographies and autobiographies of famous personalities."),
            Section(section_name="Philosophy", description="Books on philosophical thoughts and theories."),
        ]

        # Adding sections if they don't already exist
        for section in sections:
            existing_section = Section.query.filter_by(section_name=section.section_name).first()
            if not existing_section:
                db.session.add(section)

        # Sample books
        books = [
    Book(book_name="To Kill a Mockingbird", author="Harper Lee", description="A novel addressing themes of racial injustice and moral growth in the 1930s American South.", content="Set in the fictional town of Maycomb, Alabama, the novel follows Scout Finch, a young girl who witnesses her father, lawyer Atticus Finch, defend a black man falsely accused of raping a white woman. Through Scout's innocent perspective, the novel explores deep-seated prejudices and the complexities of human nature.", section_id=1, likes=12, dislikes=3),
    
    Book(book_name="A Brief History of Time", author="Stephen Hawking", description="A best-selling popular science book on cosmology and the universe's origins.", content="In 'A Brief History of Time', Stephen Hawking explains complex theories of space and time, black holes, and the Big Bang in a comprehensible manner. He discusses the nature of the universe, from its birth to its eventual fate, captivating readers with his insights into the mysteries of the cosmos.", section_id=2, likes=15, dislikes=2),
    
    Book(book_name="The Diary of a Young Girl", author="Anne Frank", description="The diary of Anne Frank, a Jewish teenager who hid from the Nazis in Amsterdam during World War II.", content="Anne Frank's diary provides an intimate account of her life in hiding, offering poignant reflections on adolescence, love, and hope amidst the horrors of war. Her diary has become a symbol of resilience and courage, reminding readers of the human spirit's ability to endure in the face of adversity.", section_id=3, likes=25, dislikes=1),
    
    Book(book_name="Steve Jobs", author="Walter Isaacson", description="A biography detailing the life, career, and legacy of Apple co-founder Steve Jobs.", content="Walter Isaacson's biography of Steve Jobs chronicles his visionary leadership at Apple, his innovative spirit in technology, and his tumultuous personal life. From the creation of iconic products like the iPhone to his challenging relationships, the biography delves deep into the complexities of one of Silicon Valley's most influential figures.", section_id=4, likes=10, dislikes=0),
    
    Book(book_name="Meditations", author="Marcus Aurelius", description="A collection of personal writings by Roman Emperor Marcus Aurelius, offering philosophical reflections on life and leadership.", content="Marcus Aurelius' 'Meditations' presents philosophical reflections on Stoicism, exploring themes of virtue, resilience, and acceptance of fate. Written as a series of notes to himself, the writings provide timeless wisdom and practical advice on navigating life's challenges with integrity and inner peace.", section_id=5, likes=20, dislikes=4)
]


        # Adding books if they don't already exist
        for book in books:
            existing_book = Book.query.filter_by(book_name=book.book_name).first()
            if not existing_book:
                db.session.add(book)

        db.session.commit()
        print("Sample data initialized successfully.")
