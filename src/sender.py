import urllib2
import urllib

import json

class Sender(object):
    PUB_URL = "http://%s/publish/%s/%s/0/%s/0/%s"
    SUB_URL = "http://%s/subscribe/%s/%s/0/%s"

    last_tt = 0

    def send(self,url):
        print "URL: %s" % (url,)
        return urllib2.urlopen( url ).read()

    def publish(self,channel,payload):
        return json.loads(self.send(self.PUB_URL % ( "pubsub.pubnub.com","demo","demo",channel,urllib.quote(json.dumps(payload)) )));

    def subscribe(self,channel):
        response = json.loads(self.send(self.SUB_URL % ( "pubsub.pubnub.com", "demo", channel, self.last_tt)));
        self.last_tt = response[1];
        return response[0]
