from umbral import pre, keys, signing

from umbral import config
from umbral.curve import SECP256K1

# Generate umbral keys for Alice.
print("\nGenerate Alice Keypair")
alices_private_key = keys.UmbralPrivateKey.gen_key()
alices_public_key = alices_private_key.get_pubkey()
print("Alice Private Key: " + str(alices_private_key))
print("Alice Public Key: " + str(alices_public_key))

alices_signing_key = keys.UmbralPrivateKey.gen_key()
alices_verifying_key = alices_signing_key.get_pubkey()
alices_signer = signing.Signer(private_key=alices_signing_key)

# Encrypt data with Alice's public key.
plaintext = 'Proxy Re-encryption is cool!'
print("\nEncrypt message ('" + plaintext + "') with Alice Public Key")
ciphertext, capsule = pre.encrypt(alices_public_key, plaintext.encode())
print("Ciphertext: " + str(ciphertext))
print("Capsule: " + str(capsule))

# Decrypt data with Alice's private key.
cleartext = pre.decrypt(ciphertext, capsule, alices_private_key, alices_public_key)

# Generate umbral keys for Bob.
print("\nGenerate Bob Keypair")
bobs_private_key = keys.UmbralPrivateKey.gen_key()
bobs_public_key = bobs_private_key.get_pubkey()

print("Bob Private Key: " + str(bobs_private_key))
print("Bob Public Key: " + str(bobs_public_key))

# Alice generates split re-encryption keys for Bob with "M of N".
print("\nGenerate Split Rekey")
kfrags = pre.split_rekey(alices_private_key, alices_signer, bobs_public_key, 20, 20)

# set correctness keys for validation of capsule
capsule.set_correctness_keys(delegating=alices_public_key,
    receiving=bobs_public_key,
    verifying=alices_verifying_key)

# Ursula re-encrypts the capsule to obtain a cfrag.
# Bob attaches the cfrags to the capsule.
print("\nAttach cfrags")
for kfrag in kfrags:
    cfrag = pre.reencrypt(kfrag, capsule)
    capsule.attach_cfrag(cfrag)

# Bob activates and opens the capsule.
print("\nDecrypt")
cleartext = pre.decrypt(ciphertext, capsule, bobs_private_key, alices_public_key)

print('\nCleartext')
print(cleartext)

# generate some random keys for malicious actor
mali_private_key = keys.UmbralPrivateKey.gen_key()
mali_public_key = mali_private_key.get_pubkey()

print("\nTry decrypting as malicious actor")
cleartextMalicious = pre.decrypt(ciphertext, capsule, mali_private_key, alices_public_key)

print("\Cleartext")
print(cleartextMalicious)