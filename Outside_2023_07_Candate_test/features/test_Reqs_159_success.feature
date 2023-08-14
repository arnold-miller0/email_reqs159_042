#Test plan
# Req_159: Email shall be sent to any valid email address from To, Cc, and/or Bcc address lines

Scenario Outline: Email-UI message Success

Given Trap Backend-Application Out-Bound-Mail-Server
Given Trap Email-UI message response
Given Open Personal-Database

 When Send Email-UI with to <toList> cc <ccList> bcc <bccList> subject <subj> body <body>
 Then Email-UI message response <result>
 Then Out-Bound-Mail-Server has sent-email <result>
 Then Personal-Database sent-email <result>

  # Note: Send mail-ui ... Step includes
  #    Select from-email via Personal-Database User-Address
  #    Create global from, to, cc, bcc unique lowercase list used in Then steps
  #    When not 'no' create global unique subject, body with date-time-stamp used in Then steps
  #    When 'no' create global subject or body as empty

  # TODO unqiue emails over TO, CC and BCC list

 Examples:
  | toList        | ccList        | bccList        | subj | body | result  | notes |
  | to01@list.com |  ,            |       ,        | yes  | yes  | success | only TO |
  | to02@list.com | cc02@list.com |       ,        | yes  | yes  | success | TO, CC |
  | to03@list.com |  ,            | BCC03@list.com | yes  | yes  | success | TO, BCC |
  | to04@list.com | CC04@list.com | BCC04@list.com | yes  | yes  | success | TO, CC, BCC |
  | TO05@list.com | to05@list.com |   ,            | yes  | yes  | success | TO same CC |
  | to06@list.com |   ,           | TO06@list.com  | yes  | yes  | success | TO same BCC |
  | to07@list.com | cc07@list.com | Cc07@list.com  | yes  | yes  | success | CC same BCC |

  | to11@list.com, to11@lisB.to  |        ,                     |      ,                        | yes  | yes  | success | TO-list |
  | to12@list.com                | cc12@list.com, cc12@list.cc  |        ,                      | yes  | yes  | success | CC-list |
  | to13@list.com                |             ,                | bc13@list.com, bc13@list.bcc  | yes  | yes  | success | BCC-list |
  | to14@list.com, to14@list.to  | cc14@list.com, cc14@list.cc  | bc14@list.com, bc14@list.bcc  | yes  | yes  | success | TO, CC BCC-list |
  | to16@list.com, to16@list.to  | cc16@list.com, TO15@list.com | bc16@list.com, bc16@list.bcc  | yes  | yes  | success | TO in CC-list |
  | to17@list.com, to17@list.to  | cc17@list.com, cc17@list.com | To175@list.com, bc17@list.bcc | yes  | yes  | success | TO in BCC-list |
  | to18@list.com, to18@list.to  | cc18@list.com, cc18@list.cc  | cC18@list.com, bc18@list.bcc  | yes  | yes  | success | CC in BCC-list |
  | to19@list.com, to19@list.com | cc19@list.com, cc19@list.cc  | bc19@list.com, bc19@list.bcc  | yes  | yes  | success | TO duplicate |
  | to20@list.com, to20@list.to  | cc20@list.com, cc20@list.com | bc20@list.com, bc20@list.bcc  | yes  | yes  | success | CC duplicate |
  | to21@list.com, to21@list.to  | cc21@list.com, cc21@list.cc  | bc21@list.bcc, bc21@list.bcc  | yes  | yes  | success | BCC duplicate |

