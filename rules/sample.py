---
name: Sample
description: "Rule which sends an email when an email from jhilmiljain@gmail.com is received"
pack: email
enabled: false
trigger:
  type: email.imap.message
  parameters: {}
criteria:
  trigger.from:
    pattern: jhilmiljain@gmail.com
    type: contains
action:
  ref: core.sendmail
  parameters:
    body: 'We received an email'
    to: jhilmiljain@gmail.com
    from: stackstorm@yourcompanyname.com
    subject: 'Email Received'
