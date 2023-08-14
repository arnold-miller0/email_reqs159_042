#Test plan
# Req_42: All email addresses identified as spam by the user shall be automatically sent to the spam folder

Feature: Req_42
Scenario Outline: In Bound Trigger Email failure

Given Trap Backend-Application Out-Bound-Mail-Server
Given Trap Sent Email-UI message
Given Open Personal-Database
# Given Personal-Database User-email <toEmail> remove <fromEmail> from Spam-list

  # Assumes <to-email> in Personal-Database User-mail list
  # Note: stub out code so Email-UI message and DB update expect "input"

When Send In-Bound-Trigger email from <fromEmail> to <toEmail> cc <ccList> subject <subj> body <body>
Then In-Bound-Trigger email response <result>
Then Send Email-UI message <result> folder <folder>
Then Personal-Database In-Bound-Trigger email <result> error <reason>

  # Note: Send In-Bound-Trigger email ... Step includes
  #     Select to-email via Personal-Database User-Address
  #     Create global from, to, cc unique lowercase list used in Then steps
  #		key-word from, to, cc, bcc key-word null for empty field 
  #     When not 'no' create global unique subject, body with date-time-stamp used in Then steps
  #     When 'no' create global subject or body as empty

 Examples: found Input failures
 | fromEmail       | toEmail       | ccList                       | subj | body | result  | folder | reason |
 | from21@list.com | to21@list.com |   ,                          | no   | yes  | failure | none   | Empty Subject |
 | FROM22@list.com | to22@list.com | cc22@list.com                | yes  | no   | failure | none   | Empty Body |
 |  ,              | to23@list.com | cc23@list.com, cc03@list.cc  | yes  | yes  | failure | none   | Empty From-Email |
 | From24@list.com | ,             | TO24@list.com                | yes  | yes  | failure | none   | Empty To-Email |
