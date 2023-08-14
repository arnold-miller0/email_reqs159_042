from pytest_bdd import scenarios, parsers, given, when, then

from .fakeDB_email_info import FakeEmailSpamDB

from .email_lists import EmailList

from . import conftest

scenarios('../features/test_Reqs_042_failure.feature',
          '../features/test_Reqs_042_spam.feature',
          '../features/test_Reqs_042_input.feature')

# Constants

@when(
    parsers.parse('Send In-Bound-Trigger email from {from_email} to {to_email} cc {cc_list} subject {subj} body {body}'),
    converters={"from_email":str, "to_email":str, "subj": str, "body": str})
def Send_In_Bound_Trigger_Email(from_email, to_email, cc_list, subj, body):
    
    EmailList.set_Email_lists_csv(EmailList, from_email, to_email, cc_list, "");
    from_lower = EmailList.get_from_list_index(EmailList, 0)
    to_lower = EmailList.get_to_list_index(EmailList, 0)
    base_output = "Send_In_Bound_Trigger_Email: from " + from_lower + " to " + to_lower + " "
    print(f'{base_output} subj {subj} body {body}')

    # TODO check email formats (from, to, cc-list)
    if not from_lower:
        FakeEmailSpamDB.set_folder_resp_reason(FakeEmailSpamDB, "none", "failure", "empty From-Email".lower())
        print(f'{base_output} {FakeEmailSpamDB.get_trigger_response(FakeEmailSpamDB)} reason {FakeEmailSpamDB.get_trigger_reason(FakeEmailSpamDB)}')
        return

    if not to_lower:
        FakeEmailSpamDB.set_folder_resp_reason(FakeEmailSpamDB, "none", "failure", "empty To-Email".lower())
        print(f'{base_output} {FakeEmailSpamDB.get_trigger_response(FakeEmailSpamDB)} reason {FakeEmailSpamDB.get_trigger_reason(FakeEmailSpamDB)}')
        return

    if subj.lower() == 'no': 
        FakeEmailSpamDB.set_folder_resp_reason(FakeEmailSpamDB, "none", "failure", "empty subject".lower())
        print(f'{base_output} {FakeEmailSpamDB.get_trigger_response(FakeEmailSpamDB)} reason {FakeEmailSpamDB.get_trigger_reason(FakeEmailSpamDB)}')
        return

    if body.lower() == 'no': 
        FakeEmailSpamDB.set_folder_resp_reason(FakeEmailSpamDB, "none", "failure", "empty body".lower())
        print(f'{base_output} {FakeEmailSpamDB.get_trigger_response(FakeEmailSpamDB)} reason {FakeEmailSpamDB.get_trigger_reason(FakeEmailSpamDB)}')
        return

    if FakeEmailSpamDB.find_user_email_with_spam_email(FakeEmailSpamDB, to_lower, from_lower):
         FakeEmailSpamDB.set_folder_resp_reason(FakeEmailSpamDB, "spam", "success", "")
    else:
        FakeEmailSpamDB.set_folder_resp_reason(FakeEmailSpamDB, "input", "success", "")
    print(f'{base_output} {FakeEmailSpamDB.get_trigger_response(FakeEmailSpamDB)} Folder {FakeEmailSpamDB.get_email_folder(FakeEmailSpamDB)}')


@then(
  parsers.parse('In-Bound-Trigger email response {result}'),
  converters={"result":str})
def Resp_In_Bound_Trigger_Email(result):
    conftest.check_FakeEmail_response("Resp Email-UI message", result)
 

@then(
  parsers.parse('Send Email-UI message {result} folder {folder}'),
  converters={"result":str, "folder":str})
def Resp_Email_UI_Send(result, folder):
    conftest.check_FakeEmail_response("Send Email-UI message", result)
    conftest.check_FakeEmail_folder("Send Email-UI message", folder)


@then(
  parsers.parse('Personal-Database In-Bound-Trigger email {result} folder {folder}'),
  converters={"result":str, "folder":str})
def Resp_Email_UI_Send(result, folder):
    conftest.check_FakeEmail_response("DB In-Bound-Trigger", result)
    conftest.check_FakeEmail_folder("Send Email-UI message", folder)


@then(
  parsers.parse('Personal-Database In-Bound-Trigger email {result} error {reason}'),
  converters={"result":str, "reason":str})
def Resp_Email_UI_Send(result, reason):
    conftest.check_FakeEmail_response("Resp Email-UI message", result)
    conftest.check_FakeEmail_reason("Resp Email-UI message", reason)



