from pytest_bdd import scenarios, parsers, given, when, then

from .fakeDB_email_info import FakeEmailSpamDB

from .email_lists import EmailList

from . import conftest

scenarios('../features/test_Reqs_159_success.feature',
          '../features/test_Reqs_159_failure.feature')

# Constants

@when(
    #              Send Email-UI with to <to-list> cc <cc-list> bcc <bcc-list> subject <subj> body <body>
    parsers.parse('Send Email-UI with to {to_list} cc {cc_list} bcc {bcc_list} subject {subj} body {body}'),
    converters={"to_list":str, "cc_list":str, "list":str, "subj": str, "body": str})
def Send_Email_UI_to_cc_bcc(to_list, cc_list, bcc_list, subj, body):
    
    EmailList.set_Email_lists_csv(EmailList, "", to_list, cc_list, bcc_list);
    to_list_lower = EmailList.get_to_list_all(EmailList)
    cc_list_lower = EmailList.get_cc_list_all(EmailList)
    bc_list_lower = EmailList.get_bcc_list_all(EmailList)
    base_output = "Send Email-UI: counts to " + str(len(to_list_lower)) + " cc " + str(len(cc_list_lower)) + " bc " + str(len(bc_list_lower)) + " "
    print(f'{base_output} subj {subj} body {body}')

    # TODO check email formats (from, to, cc-list)
    if len(to_list_lower) <= 0:
        FakeEmailSpamDB.set_folder_resp_reason(FakeEmailSpamDB, "none", "failure", "Empty To-List".lower())
        print(f'{base_output} {FakeEmailSpamDB.get_trigger_response(FakeEmailSpamDB)} reason: {FakeEmailSpamDB.get_trigger_reason(FakeEmailSpamDB)}')
        return

    if subj.lower() == 'no': 
        FakeEmailSpamDB.set_folder_resp_reason(FakeEmailSpamDB, "none", "failure", "empty subject".lower())
        print(f'{base_output} {FakeEmailSpamDB.get_trigger_response(FakeEmailSpamDB)} reason: {FakeEmailSpamDB.get_trigger_reason(FakeEmailSpamDB)}')
        return

    if body.lower() == 'no': 
        FakeEmailSpamDB.set_folder_resp_reason(FakeEmailSpamDB, "none", "failure", "empty body".lower())
        print(f'{base_output} {FakeEmailSpamDB.get_trigger_response(FakeEmailSpamDB)} reason: {FakeEmailSpamDB.get_trigger_reason(FakeEmailSpamDB)}')
        return

    FakeEmailSpamDB.set_folder_resp_reason(FakeEmailSpamDB, "output", "success", "")
    print(f'{base_output} {FakeEmailSpamDB.get_trigger_response(FakeEmailSpamDB)} Folder {FakeEmailSpamDB.get_email_folder(FakeEmailSpamDB)}')



@then(
  parsers.parse('Email-UI message response {result}'),
  converters={"result":str})
def Resp_In_Bound_Trigger_Email(result):
    conftest.check_FakeEmail_response("Email-UI message response", result)


@then(
  parsers.parse('Email-UI message response {result} error {reason}'),
  converters={"result":str, "reason":str})
def Resp_Email_UI_Send(result, reason):
    conftest.check_FakeEmail_response("Send Email-UI message", result)
    conftest.check_FakeEmail_reason("Send Email-UI message", reason)

@then(
  parsers.parse('Out-Bound-Mail-Server has sent-email {result}'),
  converters={"result":str})
def Resp_In_Bound_Trigger_Email(result):
     conftest.check_FakeEmail_response("Out-Bound-Mail-Server has sent-email", result)


@then(
  parsers.parse('Personal-Database sent-email {result}'),
  converters={"result":str})
def Resp_In_Bound_Trigger_Email(result):
    conftest.check_FakeEmail_response("Personal-Database sent-email", result)


