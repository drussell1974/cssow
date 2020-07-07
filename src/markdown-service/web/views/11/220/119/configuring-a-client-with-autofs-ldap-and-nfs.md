Configure NFS Server
====================

See XXXXX for more details

Add the Automount to the LDAP Directory

Create the ldif file with the objects


> nano add_mounts.ldif


```
dn: ou=auto.master,dc=example,dc=net

ou: auto.master

objectClass: top

objectClass: automountMap



dn: cn=/home,ou=auto.master,dc=example,dc=net

cn: /home

objectClass: automount

automountInformation: ldap <LDAP_SERVER>:ou=auto.home,dc=example,dc=net 



dn: ou=auto.home,dc=example,dc=net

ou: auto.home

objectClass: top

objectClass: automountMap



dn: cn=/public,ou=auto.master,dc=example,dc=net

cn: /public

objectClass: automount

automountInformation: ldap <LDAP_SERVER>:ou=auto.misc,dc=example,dc=net 



dn: ou=auto.misc,dc=example,dc=net

ou: auto.misc

objectClass: top

objectClass: automountMap



## Add for each user

dn: uid=wolverine,ou=employees,dc=example,dc=net

objectClass: person

objectClass: organizationalPerson

objectClass: inetOrgPerson

objectClass: posixAccount

uid: wolverine

sn: Howlett

givenName: James

cn: wolverine

displayName: Wolverine

uidNumber: 1002

gidNumber: 5001

userPassword: password

loginShell: /bin/bash

homeDirectory: /home/wolverine



dn: cn=wolverine,ou=auto.home,dc=example,dc=net

cn: wolverine

objectClass: automount

automountInformation: -fstype=nfs,hard,intr,nodev,nosuid,uid=nslcd,gid=nslcd

<LDAP_SERVER>:/home/wolverine

... 

```

Add the mounts to the ldap directory



> ldapadd -w <PASSWORD> -D cn=admin,dc=example,dc=net -f add_mount.ldif



Create a group for members this group will have permission to create home folders,



> nano add_group_roamingusers.ldif



```

dn: cn=roamingusers,dc=example,dc=net

changetype: add

objectClass: posixGroup

cn: roamingusers

gidNumber: 5004

memberUid: wolverine

```



Add the group to the ldap directory



> ldapadd -w <PASSWORD> -D cn=admin,dc=example,dc=net -f add_mount.ldif



Allow client permissions of network directories



> nano /etc/exports  

```

/opt/nfs/public         192.168.1.0/24(rw,sync,no_subtree_check)

/home                   192.168.1.0/24(rw,sync,no_root_squash,no_subtree_check)

```

> exportfs -a



Install LDAP Tools on the Clients
Install the packages



> sudo apt-get libnss-ldapd libpam-ldapd ldap-utils nscd



Check the ldap configuration

> cat /etc/nslcd.conf

```

# /etc/nslcd.conf

# nslcd configuration file. See nslcd.conf(5)

# for details.



# The user and group nslcd should run as.

uid nslcd

gid nslcd



# The location at which the LDAP server(s) should be reachable.

uri ldap://<LDAP_SERVER>:389



# The search base that will be used for all queries.

base dc=<DOMAIN>,dc=<TLD>



# The LDAP protocol version to use.

#ldap_version 3



# The DN to bind with for normal lookups.

#binddn cn=<LDAP_ADMIN_USER>,dc=<DOMAIN>,dc=<TLD>

#bindpw <PASSWORD>



# The DN used for password modifications by root.

#rootpwmoddn cn=admin,dc=<DOMAIN>,dc=<TLD>



# SSL options

#ssl off

#tls_reqcert never

tls_cacertfile /etc/ssl/certs/ca-certificates.crt



# The search scope.

#scope sub

```

Verify the nsswitch.conf



> cat /etc/nsswitch.conf



```

# /etc/nsswitch.conf

#

# Example configuration of GNU Name Service Switch functionality.

# If you have the `glibc-doc-reference' and `info' packages installed, try:

# `info libc "Name Service Switch"' for information about this file.



passwd:         files ldap

group:          files ldap

shadow:         files ldap

gshadow:        files



hosts:          files mdns4_minimal [NOTFOUND=return] dns

networks:       files



protocols:      db files

services:       db files

ethers:         db files# /etc/nsswitch.conf

#

# Example configuration of GNU Name Service Switch functionality.

# If you have the `glibc-doc-reference' and `info' packages installed, try:

# `info libc "Name Service Switch"' for information about this file.



passwd:         files ldap

group:          files ldap

shadow:         files ldap

gshadow:        files



hosts:          files mdns4_minimal [NOTFOUND=return] dns

networks:       files



protocols:      db files

services:       db files

ethers:         db files

rpc:            db files



netgroup:       nis



rpc:            db files



netgroup:       nis

```



Restart LDAP client service



> /etc/init.d/nslcd restart



```

[ ok ] Restarting nslcd (via systemctl): nslcd.service.

```

Retrieve a list of LDAP users



> getent passwd



```

....

wolverine:x:1002:5001:wolverine:/home/wolverine:/bin/bash

....

```



Add Autofs automount to LDAP

See XXXX for detail on installing LDAP server. This assumes base dn of the LDAP Directory dc=example,dc=net



Install AutoFs



> apt-get install autofs autofs-ldap



Configure the client machine



> nano /etc/autofs.conf



```

master_map_name = ou=auto.master,dc=example,dc=net

logging = verbose

ldap_uri = "ldap://<ldap_server>:389

search_base = "dc=<domain>,dc=<tld>"

#

# Other common LDAP naming

#

map_object_class = automountMap

entry_object_class = automount

map_attribute = ou

entry_attribute = cn

value_attribute= automountInformation

```



> nano /etc/autofs_ldap_auth.conf



```

<autofs_ldap_sasl_conf

        usetls="no"

        tlsrequired="no"

        authrequired="no" />

```



> nano /etc/nsswitch.conf



```

automount: files ldap

```



Restart service



> /etc/init.d/autofs restart



```

 autofs.service - Automounts filesystems on demand

   Loaded: loaded (/lib/systemd/system/autofs.service; enabled; vendor preset: enabled)

   Active: active (running) since Thu 2020-06-25 05:37:44 BST; 5s ago



....



Jun 25 05:37:42 raspberrypi systemd[1]: Starting Automounts filesystems on demand...

Jun 25 05:37:42 raspberrypi automount[3203]: Starting automounter version 5.1.2, master map ou=…itute

Jun 25 05:37:42 raspberrypi automount[3203]: using kernel protocol version 5.03

Jun 25 05:37:43 raspberrypi automount[3203]: connected to uri ldap://<LDAP_SERVER>:389

Jun 25 05:37:43 raspberrypi automount[3203]: mounted indirect on /home with timeout 60, freq 15…conds

Jun 25 05:37:43 raspberrypi automount[3203]: ghosting enabled

Jun 25 05:37:43 raspberrypi automount[3203]: mounted indirect on /public with timeout 60, freq …conds

Jun 25 05:37:43 raspberrypi automount[3203]: ghosting enabled

```

Testing it out
> su - <ldap_user>



References and useful links

https://www.tecmint.com/configure-ldap-client-to-connect-external-authentication/



https://help.ubuntu.com/community/AutofsLDAP



https://www.openldap.org/faq/data/cache/599.html



https://computingforgeeks.com/how-to-configure-ubuntu-18-04-ubuntu-16-04-lts-as-ldap-client/