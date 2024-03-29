---
name: Sample
description: "Rule which sends an email when an email from jhilmiljain@gmail.com is received"
pack: trial123
enabled: false
criteria:
  trigger.from:
    pattern: jhilmil123jain@gmail.com
    type: contains
action:
  ref: core.sendmail
  parameters:
    body: 'We received an email'
    to: jhilmiljain821@gmail.com
    from: jhilmil123jain@gmail.com
    subject: 'Email Received'
