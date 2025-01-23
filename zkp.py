import random

class ZeroKnowledgeProof:
    def __init__(self, secret, prime):
        self.secret = secret
        self.prime = prime

    def commit(self):
        self.r = random.randint(1, self.prime - 1)
        self.C = pow(self.r, 2, self.prime)  # Commitment
        return self.C

    def challenge(self):
        return random.randint(0, 1)

    def respond(self, challenge):
        if challenge == 0:
            return self.r
        else:
            return (self.r * self.secret) % self.prime

    def verify(self, C, challenge, response):
        if challenge == 0:
            return pow(response, 2, self.prime) == C
        else:
            return pow(response, 2, self.prime) == (C * pow(self.secret, 2, self.prime)) % self.prime