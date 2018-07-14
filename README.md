# PyUmbral Docker

Interactive Docker shell to play around with pyUmbral implementation [https://github.com/nucypher/pyUmbral](https://github.com/nucypher/pyUmbral) due to dependency issues on mac and python installation.

# Install

Run the following command to build the docker container. It will per default download and install all the dependencies:

```
docker build -t py-umbral-docker .
```

# Start Container 

To run an interactive shell

```
docker run -v $(pwd)/contents:/contents -it py-umbral-docker /bin/bash -c "cd /pyUmbral; pipenv shell"
```

And work with your files (`/contents/test.py` in this example):

```
cd /contents && python test.py
```

The output for `/contents/test.py` is:

```
Generate Alice Keypair
/pyUmbral/umbral/config.py:19: RuntimeWarning: No default curve has been set.  Using SECP256K1.  A slight performance penalty has been incurred for only this call.  Set a default curve with umbral.config.set_default_curve().
  warn(cls.__WARNING_IF_NO_DEFAULT_SET, RuntimeWarning)
Alice Private Key: <umbral.keys.UmbralPrivateKey object at 0x7fc1827b3ef0>
Alice Public Key: <class 'umbral.keys.UmbralPublicKey'>:0388c807163c79d

Encrypt message ('Proxy Re-encryption is cool!') with Alice Public Key
Ciphertext: b'\xf3`>\xb6}g\xe0\xb4\x1bw\xbb\x1e\x02\x99oI\xbf\x7f\x8a\xec4\xdf\x9f\xbbG|8+\x0f\x17\xb9-eZ\x001\x1d\xdd\xbd\xef\xf9\x0e4\xa6\x8a\xc1\xb8f\xcd\x9c5\xa1\xfaj\ny'
Capsule: <umbral.pre.Capsule object at 0x7fc17ddb9978>

Generate Bob Keypair
Bob Private Key: <umbral.keys.UmbralPrivateKey object at 0x7fc17ddb9940>
Bob Public Key: <class 'umbral.keys.UmbralPublicKey'>:02935e56594eb13

Generate Split Rekey

Attach cfrags

Decrypt

Cleartext
b'Proxy Re-encryption is cool!'

Try decrypting as malicious actor
Traceback (most recent call last):
  File "test.py", line 63, in <module>
    cleartextMalicious = pre.decrypt(ciphertext, capsule, mali_private_key, alices_public_key)
  File "/pyUmbral/umbral/pre.py", line 509, in decrypt
    encapsulated_key = _open_capsule(capsule, decrypting_key, check_proof=check_proof)
  File "/pyUmbral/umbral/pre.py", line 492, in _open_capsule
    key = _decapsulate_reencrypted(receiving_privkey, capsule)
  File "/pyUmbral/umbral/pre.py", line 448, in _decapsulate_reencrypted
    raise GenericUmbralError()
umbral.pre.GenericUmbralError
```

You can now edit the files in `./contents` with your favourite editor and run them in the container.


# Whats PyUmbral?

PyUmbral is the Python Implementation of the Umbral Proxy Re-Encryption Scheme. The Umbral PRE Scheme was developed by David Núñez and enables splitting of re-encryption keys used for proxy re-encryption. See the whitepaper here: [https://github.com/nucypher/umbral-doc/blob/master/umbral-doc.pdf](https://github.com/nucypher/umbral-doc/blob/master/umbral-doc.pdf).
