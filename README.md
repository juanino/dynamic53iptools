# dynamic53iptools
dynamic dns wanna-be for route 53

# purpose
Set of tools to mimic dynamic dns.
When I used to use dyndns this was fine, but now I run a few things in amazon and I don't want to grant full route53 control to a domain
so I allow the clients to push onto a queue and a more restricted control box can chaneg dns records for the domain.  This prevents 
having to give IAM access for the whole domain, instead the control box will only change single records it knows about.
