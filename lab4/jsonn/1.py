import json 

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------ """)
print(data['imdata'][0]["l1PhysIf"]["attributes"]["dn"], end='                               ')
print(data['imdata'][0]["l1PhysIf"]["attributes"]["speed"], end='  ')
print(data['imdata'][0]["l1PhysIf"]["attributes"]["mtu"])

print(data['imdata'][1]["l1PhysIf"]["attributes"]["dn"], end='                               ')
print(data['imdata'][1]["l1PhysIf"]["attributes"]["speed"], end='  ')
print(data['imdata'][1]["l1PhysIf"]["attributes"]["mtu"])

print(data['imdata'][2]["l1PhysIf"]["attributes"]["dn"], end='                               ')
print(data['imdata'][2]["l1PhysIf"]["attributes"]["speed"], end='  ')
print(data['imdata'][2]["l1PhysIf"]["attributes"]["mtu"])
print("\n")