#Test plan
# Req_159: Email shall be sent to any valid email address from To, Cc, and/or Bcc address lines

Scenario Outline: Email-UI message Failure

Given Trap Backend-Application Out-Bound-Mail-Server
Given Trap Email-UI message response
Given Open Personal-Database

 When Send Email-UI with to <to-list> cc <cc-list> bcc <bcc-list> subject <subj> body <body>
 Then Email-UI message response <result> error <reason>
 Then Out-Bound-Mail-Server has sent-email <result>
 Then Personal-Database sent-email <result>

  # Note: Send mail-ui ... Step includes
  #    Select from-email via Personal-Database User-Address
  #    Create global from, to, cc, bcc unique lowercase list used in Then steps
  #    When not 'no' create global unique subject, body with date-time-stamp used in Then steps
  #    When 'no' create global subject or body as empty

  # TODO check for TO, CC, BCC email pattern

 Examples:
  | to-list                     | cc-list                     | bcc-list                       | subj  | body | result  | reason        |
  | to30@list.com               | TO30@list.com               | bcc30@list.com                 | no    | yes  | failure | Empty Subject |
  | to31@list.com               | cc31@list.com               | bcc31@list.com                 | yes   | no   | failure | Empty Body    |
  |     ,                       | cc32@list.com               | bcc32@list.com                 | yes   | no   | failure | Empty To-List |
# TODO | to3-@list.com               | cc33@list.com               |     ,                          | yes   | yes  | failure | Bad To-Email  |
# TODO | to35@list.com               | cc35@list.com               | BCC35-list.com                 | yes   | yes  | failure | Bad BCC-Email |
# TODO | TO36@list.com, to36@list    | cc36@list.com, cc37list.cc  | Bcc36@list.com, bcc36@lisb.bcc | yes   | yes  | failure | Bad To-Email  |
# TODO | TO37@list.to, to37@list.com | cc37@list.com, cc37@list,cc | Bcc37@list.com, bcc37@list.bcc | yes   | yes  | failure | Bad CC-Email  |
# TODO | TO38@list.to, to38@list.com | cc38@list.com, cc38@list.cc | Bcc33@list.com, bcc38@list!bcc | yes   | yes  | failure | Bad BCC-Email |

