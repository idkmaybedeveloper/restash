import base64
import struct
import zlib

props_dict = {
    "stash.LicenseTypeName": "COMMERCIAL",
    "stash.NumberOfUsers": "-1",
    "stash.active": "true",
    "stash.PurchaseDate": "2026-04-19",
    "stash.CreationDate": "2026-04-19",
    "stash.MaintenanceExpiryDate": "2099-01-01",
    "stash.LicenseExpiryDate": "2099-01-01",
    "LicenseTypeName": "COMMERCIAL",
    "Organisation": "cuddles.rs",
    "ContactName": "lain",
    "ContactEMail": "lain@wired",
    "ServerID": "",  # REPLACE WITH YOUR OWN
    "LicenseID": "asdasd-2026",
    "Description": "I_HATE_ATLASSIAN",
    "CreationDate": "2026-04-19",
    "LicenseExpiryDate": "2099-01-01",
    "MaintenanceExpiryDate": "2099-01-01",
    "NumberOfClusterNodes": "-1",
    "SEN": "13371337",
    "NumberOfBambooPlans": "-1",
    "NumberOfBambooRemoteAgents": "-1",
    "NumberOfBambooLocalAgents": "-1",
    "DataCenter": "meow",
    "Evaluation": "false",
}

props_str = "".join(f"{k}={v}\n" for k, v in props_dict.items())

prefix = bytes([13, 14, 12, 10, 15])
zipped_props = zlib.compress(props_str.encode("utf-8"))
license_text_bytes = prefix + zipped_props
dummy_hash = b"dummy-signature-padding-for-lain"
text_len = len(license_text_bytes)

payload = struct.pack(">I", text_len) + license_text_bytes + dummy_hash
encoded_payload = base64.b64encode(payload).decode("utf-8")


def to_base31(n):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTU"
    res = ""
    while n > 0:
        res = chars[n % 31] + res
        n //= 31
    return res or "0"


suffix = "X02" + to_base31(len(encoded_payload))
print(encoded_payload + suffix)
