#Test plan
# Req_42: All email addresses identified as spam by the user shall be automatically sent to the spam folder

Feature: Req_42

Scenario Outline: In Bound Trigger Email Spam
Given Trap Backend-Application Out-Bound-Mail-Server
Given Trap Sent Email-UI message
Given Open Personal-Database
Given Personal-Database User-email <toEmail> add <fromEmail> to Spam-list

  # Assumes toEmail in Personal-Database User-mail list
  # Note: stub out code so Email-UI message and DB update expect "spam"

 When Send In-Bound-Trigger email from <fromEmail> to <toEmail> cc <ccList> subject <subj> body <body>
 Then In-Bound-Trigger email response <result>
 Then Send Email-UI message <result> folder <folder>
 Then Personal-Database In-Bound-Trigger email <result> folder <folder>

  # Note: Send In-Bound-Trigger email ... Step includes
  #     Select to-email via Personal-Database User-Address
  #     Create global from, to, cc unique lowercase list used in Then steps
  #     Create global from, to, cc unique lowercase list used in Then steps
  #     When not 'no' create global unique subject, body with date-time-stamp used in Then steps
  #     When 'no' create global subject or body as empty

 Examples: found Spam email
 | fromEmail       | toEmail       | ccList                       | subj | body | result  | folder | notes |
 | from01@list.com | to01@list.com |  ,                           | yes  | yes  | success | spam   | only To |
 | FROM02@list.com | to02@list.com | cc02@list.com                | yes  | yes  | success | spam   | To, CC |
 | FROM03@list.com | to03@list.com | cc03@list.com, cc03@list.cc  | yes  | yes  | success | spam   | CC-list |
 | From04@list.com | to04@list.com | TO04@list.com                | yes  | yes  | success | spam   | To same CC |
 | From05@list.com | to05@list.com | CC05@list.com, TO05@list.com | yes  | yes  | success | spam   | To in CC-list |

