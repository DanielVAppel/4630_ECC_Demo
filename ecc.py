import os
from ecdsa import SigningKey, NIST256p, VerifyingKey
from ecdsa.util import randrange_from_seed__trytryagain

def generate_keys():
    """
    Generates a public-private key pair using ECC with a secure random seed.
    Utilizes NIST P-256 curve (also known as secp256r1).
    """
    # Generate a secure random seed
    seed = os.urandom(NIST256p.baselen)
    # Generate private key using the random seed
    secexp = randrange_from_seed__trytryagain(seed, NIST256p.order) #acts as the private key
    private_key = SigningKey.from_secret_exponent(secexp, curve=NIST256p)
    public_key = private_key.get_verifying_key()
    return private_key, public_key

def sign_message(private_key, message):
    """
    Signs a message using the provided private key.
    """
    # Ensure message is bytes, not str
    message = message.encode('utf-8') if isinstance(message, str) else message
    signature = private_key.sign(message)
    return signature

def verify_signature(public_key, message, signature):
    """
    Verifies a signature using the public key.
    """
    # Ensure message is bytes, not str
    message = message.encode('utf-8') if isinstance(message, str) else message
    return public_key.verify(signature, message)

def main():
    """
    Main function to demonstrate signing and verification.
    """
    # Simulating a message from a mobile device
    message = "This is a secure message from the mobile device."
    print("Original Message:", message)

    # Generate ECC keys
    private_key, public_key = generate_keys()
    
    # Sign the message
    signature = sign_message(private_key, message)
    print("Signature:", signature.hex())

    # Verify the signature
    verification = verify_signature(public_key, message, signature)
    print("Verification result:", "Success" if verification else "Failure")

if __name__ == "__main__":
    main()
