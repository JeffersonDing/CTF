# Weird File

So this is something to do with MSWord macros
Heres the macros in the file

```vbscript=
Sub AutoOpen()
    MsgBox "Macros can run any program", 0, "Title"
    Signature

End Sub

 Sub Signature()
    Selection.TypeText Text:="some text"
    Selection.TypeParagraph

 End Sub

 Sub runpython()

Dim Ret_Val
Args = """" '"""
Ret_Val = Shell("python -c 'print(\"cGljb0NURnttNGNyMHNfcl9kNG5nM3IwdXN9\")'" & " " & Args, vbNormalFocus)
If Ret_Val = 0 Then
   MsgBox "Couldn't run python script!", vbOKOnly
End If
End Sub
```

The `runpython()` is sus

# Flag

Yup the print in the python script is just base64 encoded.

```
picoCTF{m4cr0s_r_d4ng3r0us}
```
