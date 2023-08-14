"""
This module contains FakeDB User-Emails with Spam-List
"""

class FakeEmailSpamDB:

    _DB_USER_EMAIL_SPAM_LIST = {}

    _Send_EMAIL_folder = ""
    _Trigger_response = ""
    _Trigger_reason = ""

    def __init__(self):
         self._DB_USER_EMAIL_SPAM_LIST = {
             "to01@list.com": ["from01@list.com"],
             "to02@list.com": ["from02@list.com"],
             "to03@list.com": ["from03@list.com"],
             "to04@list.com": ["from04@list.com"],
             "to05@list.com": ["from05@list.com"]
        }
     


    def set_folder_resp_reason(self, folder, resp, reason):
        self._Send_EMAIL_folder = folder
        self._Trigger_response = resp
        self._Trigger_reason = reason


    def get_email_folder(self):
            return self._Send_EMAIL_folder


    def get_trigger_response(self):
        return self._Trigger_response


    def get_trigger_reason(self):
        return self._Trigger_reason



    def user_email_add_spam_list(self, user_email, spam_email):
        print(f'fakeBD add user-email {user_email} spam_email {spam_email}')
        user_lower = user_email.lower()
        spam_lower = spam_email.lower()
        spam_list = self._DB_USER_EMAIL_SPAM_LIST.get(user_lower)
        if spam_list:
            if spam_lower not in spam_list:
                spam_list.append(spam_lower)
                print(f'user-email {user_lower} added {spam_lower} to Spam-List')
                self._DB_USER_EMAIL_SPAM_LIST[user_lower] = spam_list
            else:
                 print(f'user-email {user_lower} has {spam_lower} in Spam-List')
        else:
            spam_list = {spam_lower}
            self._DB_USER_EMAIL_SPAM_LIST[user_lower] = spam_list
            print(f'user-email {user_lower} added to DB User-email with {spam_lower} in Spam-List')


    def user_email_remove_spam_list(self, user_email, spam_email):
        print(f'fakeBD remove user-email {user_email} spam_email {spam_email}')
        user_lower = user_email.lower()
        spam_lower = spam_email.lower()
        spam_list = self._DB_USER_EMAIL_SPAM_LIST.get(user_lower)
        if spam_list:
            if spam_lower in spam_list:
                spam_list.remove(spam_lower)
                print(f'user-email {user_lower} removed {spam_lower} from Spam-List')
                self._DB_USER_EMAIL_SPAM_LIST.update(spam_list)
            else:
                  print(f'user-email {user_lower} missing {spam_lower} from Spam-List')
        else:
            self._DB_USER_EMAIL_SPAM_LIST[user_lower] = {}
            print(f'user-email {user_lower} added to DB User-email with empty Spam-List')


    def find_user_email_with_spam_email(self, user_email, spam_email):
        print(f'fakeBD find user-email {user_email} spam_email {spam_email}')
        user_lower = user_email.lower()
        spam_lower = spam_email.lower()
        spam_list = self._DB_USER_EMAIL_SPAM_LIST.get(user_lower)
        if spam_list:
            print(f'user-email {user_lower} is in DB User-email list')
            return spam_lower in spam_list
        else:
            print(f'user-email {user_lower} not in DB User-email list')
            return False

