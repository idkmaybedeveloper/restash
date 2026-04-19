# restash

cracking the fucking stash v3

all the logic is in atlassian-extras-decoder-v2-3.2.jar, validation happens in
Version2LicenseDecoder class

# how to??

copy atlassian-extras-decoder-v2-3.2.jar to the machine, patch it in Recafe:

```
L:
    line 185
    pop // spit it out
    goto N ; go to N
```

## license

jst run meow.py (replace with own server id)

## p.s.

```
failed to lookup license type <null>
```
