import sender
# init sender obj
s = sender.Sender();

# subscribe to get Timetoken
s.subscribe("some-ch")

# publish a msg and subscribe to get it
print s.publish("some-ch","foo-bar")
print s.subscribe("some-ch")
