from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
import sys
import os
from dotenv import load_dotenv
load_dotenv()


class PayPalClient:
    def __init__(self):
        self.client_id = str(os.environ.get('PAYPAL_CLIENT_ID'))
        self.client_secret = str(os.environ.get('PAYPAL_CLIENT_SECRET'))
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
