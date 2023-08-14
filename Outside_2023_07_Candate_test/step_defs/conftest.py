import pytest

from pytest_bdd import given, when, parsers

from .fakeDB_email_info import FakeEmailSpamDB


# Hooks

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')


# Fixtures

@pytest.fixture
# Shared Given Steps

@given(
    parsers.parse('Personal-Database User-email {user_email} add {spam_email} to Spam-list'),
        converters={"user_email": str, "spam_email": str})
def user_email_add_spam_list(user_email, spam_email):
    FakeEmailSpamDB.user_email_add_spam_list(FakeEmailSpamDB, user_email, spam_email)


@given(
     parsers.parse('Personal-Database User-email {user_email} remove {spam_email} from Spam-list'),
        converters={"user_email": str, "spam_email": str})
def user_email_remove_spam_list(user_email, spam_email):
    FakeEmailSpamDB.user_email_remove_spam_list(FakeEmailSpamDB, user_email, spam_email)
      

@given(
    parsers.parse('Trap Backend-Application Out-Bound-Mail-Server'))
def Trap_Out_Bound_Mail_Server():
    print(f'Stub: Backend-Application Out-Bound-Mail-Server')


@given(
    parsers.parse('Trap Email-UI message response'))
def Trap_Out_Bound_Mail_Server():
    print(f'Stub: Trap Email-UI message response')


@given(
    parsers.parse('Trap Sent Email-UI message'))
def Trap_Sent_Email_UTI_Msge():
    print(f'Stub: Sent Email-UI message')


@given(
    parsers.parse('Open Personal-Database'))
def Open_Personal_DB():
    print(f'Stub: Open Personal-Database')
    FakeEmailSpamDB


def check_FakeEmail_response(info, result):
    acc_resp = FakeEmailSpamDB.get_trigger_response(FakeEmailSpamDB)
    print(f'{info} {result} is {acc_resp}')
    assert result.lower() == acc_resp, info + " response: " + result


def check_FakeEmail_reason(info, reason):
    acc_reas = FakeEmailSpamDB.get_trigger_reason(FakeEmailSpamDB)
    print(f'{info} {reason} is {acc_reas}')
    assert reason.lower() == acc_reas, info + " reason: " + reason


def check_FakeEmail_folder(info, folder):
    acc_fold = FakeEmailSpamDB.get_email_folder(FakeEmailSpamDB)
    print(f'{info} {folder} is {acc_fold}')
    assert folder.lower() == acc_fold, info + " folder: " + folder
