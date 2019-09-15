# dynamic53iptools
dynamic dns wanna-be for route 53

# purpose
Set of tools to mimic dynamic dns.
When I used to use dyndns this was fine, but now I run a few things in amazon and I don't want to grant full route53 control to a domain
so I allow the clients to push onto a queue and a more restricted control box can chaneg dns records for the domain.  This prevents 
having to give IAM access for the whole domain, instead the control box will only change single records it knows about.

# usage
From the client which has a changing IP
```
sqs_send_event.py queue_name.fifo booted
``` 

From the control box
```
sqs_fetch_event.py queue_name.fifo
```

# warnings
This was really saved for me and my son so I could remember how I did this ridiculous run around to not having to pay $1 a month for an elastic IP when
it is attached to a machine that is turned off.  This way we still get predictable DNS names for our minecraft server, but we don't have to attach
that "expensive" elastic ip. Besides, this is cooler.

You would actually have to change a few of the files to make this work for yourself. The SQS examples are solid but they call a shell script to make the route53 changes
becaue I'm lazy.

