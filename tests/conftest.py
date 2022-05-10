import pytest
from posts.models import Resume, Rating, Poll, PollFile
from django.contrib.auth.models import User
from direct_message.models import Message
from django.utils import timezone


CREATION_DATE = timezone.now()


USERNAME = "testuser"
FIRSTNAME = "Test"
LASTNAME = "User"
PASSWORD = "testpass"
EMAIL = "testuser@gmail.com"
DESCRIPTION = "this is a test post"
FILE1 = "Alon_Shakaroffs_resume.pdf"
LONG_PROFESSION = " test test test test test test test test test test test test test test test test" \
                 " test test test test test test test test test" \
                 " test test test test test test test test test" \
                 " test test test test "
VALID_COMMENT = "test"
EMPTY_COMMENT = ""
LONG_COMMENT = "test test test test test test test test test test test test test test test test test" \
    " test test test test test test test test test test test test test test test test test test test" \
    " test test test test test test test test test test test test test test test test test test test" \
    " test test test test test test test test test test test test test test test test test test test" \
    " test test test test test test test test test test test test test test test test test test test" \
    " test test test test test test test test test test test test test test test test test test test" \
    " test test test test test test test test test test test test test test test test test test test"


@pytest.fixture
def new_user():
    user = User(username=USERNAME, first_name=FIRSTNAME, last_name=LASTNAME, email=EMAIL)
    user.set_password(PASSWORD)
    return user


@pytest.fixture
def persist_user(new_user):
    new_user.save()
    return new_user


@pytest.fixture
def new_resume(new_user):
    return Resume(author=new_user, description=DESCRIPTION, resume_file=FILE1)


@pytest.fixture
def persist_resume(new_resume):
    new_resume.author.save()
    new_resume.save()
    return new_resume


@pytest.fixture
def new_rating(new_resume, new_user):
    return Rating(
        author=new_user,
        resume=new_resume,
        design_rating=5,
        skill_relevance_rating=5,
        grammar_rating=5,
        conciseness_rating=5
    )


@pytest.fixture
def persist_rating(new_rating):
    new_rating.author.save()
    new_rating.resume.save()
    new_rating.save()
    return new_rating


@pytest.fixture
def new_poll(new_user):
    return Poll(author=new_user, description=DESCRIPTION)


@pytest.fixture
def persist_poll(new_poll):
    new_poll.author.save()
    new_poll.save()
    return new_poll


@pytest.fixture
def new_poll_file(new_poll):
    return PollFile(poll=new_poll, file=FILE1)


@pytest.fixture
def persist_poll_file(new_poll_file):
    new_poll_file.poll.author.save()
    new_poll_file.poll.save()
    new_poll_file.save()
    return new_poll_file


@pytest.fixture
def new_user_sender():
    return User(username='TestSender', first_name='Nick',
                last_name='Birch', password='1234', email='Nick@email.com')


@pytest.fixture
def new_user_receiver():
    return User(username='TestReceiver', first_name='Andrew',
                last_name='Glouberman', password='abcd', email='Andrew@email.com')


@pytest.fixture
def new_message(new_user_sender, new_user_receiver):
    return Message(sender=new_user_sender,
                   receiver=new_user_receiver,
                   creation_date=CREATION_DATE,
                   message_text='test')
