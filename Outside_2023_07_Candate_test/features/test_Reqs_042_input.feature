#Test plan
# Req_42: All email addresses identified as spam by the user shall be automatically sent to the spam folder

Feature: Req_42
Scenario Outline: In Bound Trigger Email Input

Given Trap Backend-Application Out-Bound-Mail-Server
Given Trap Sent Email-UI message
Given Open Personal-Database
Given Personal-Database User-email <toEmail> remove <fromEmail> from Spam-list

  # Assumes <to-email> in Personal-Database User-mail list
  # Note: stub out code so Email-UI message and DB update expect "input"

When Send In-Bound-Trigger email from <fromEmail> to <toEmail> cc <ccList> subject <subj> body <body>
Then In-Bound-Trigger email response <result>
Then Send Email-UI message <result> folder <folder>
Then Personal-Database In-Bound-Trigger email <result> folder <folder>

  # Note: Send In-Bound-Trigger email ... Step includes
  #     Select to-email via Personal-Database User-Address
  #     Create global from, to, cc unique lowercase list used in Then steps
  #		key-word from, to, cc, bcc key-word null for empty field 
  #     When not 'no' create global unique subject, body with date-time-stamp used in Then steps
  #     When 'no' create global subject or body as empty

 Examples: found Input email
 | fromEmail       | toEmail       | ccList                       | subj | body | result  | folder | notes |
 | from11@list.com | to01@list.com |   ,                          | yes  | yes  | success | input  | only To |
 | FROM12@list.com | to02@list.com | cc02@list.com                | yes  | yes  | success | input  | To, CC |
 | FROM13@list.com | to03@list.com | cc03@list.com, cc03@list.cc  | yes  | yes  | success | input  | CC-list |
 | From14@list.com | to04@list.com | TO04@list.com                | yes  | yes  | success | input  | To same CC |
 | From15@list.com | to05@list.com | CC05@list.com, TO05@list.com | yes  | yes  | success | input  | To in CC-list |

