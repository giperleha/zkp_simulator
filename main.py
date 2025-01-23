from zkp import ZeroKnowledgeProof

def main():
    print("Welcome to the Zero-Knowledge Proof Simulator!")
    secret = int(input("Enter your secret number: "))
    prime = int(input("Enter a prime number: "))

    zkp = ZeroKnowledgeProof(secret, prime)

    # Prover commits
    C = zkp.commit()
    print(f"\nCommitment (C): {C}")

    # Verifier sends challenge
    challenge = zkp.challenge()
    print(f"Challenge: {challenge}")

    # Prover responds
    response = zkp.respond(challenge)
    print(f"Response: {response}")

    # Verifier verifies
    if zkp.verify(C, challenge, response):
        print("\nVerification Successful! The prover knows the secret.")
    else:
        print("\nVerification Failed! The prover does not know the secret.")

if __name__ == "__main__":
    main()