# xorAndb64

## example

js

```
var en =  XorAndB64.encode("!@#$%^&*())<>,.?/:;KKEWO32823@#*@*#*&&#@(*(#&&^$#", "abcabcabcabaaabc");
console.log(en);
var de = XorAndB64.decode(en, "abcabcabcabaaabc");
console.log(de);
```

py

```
en = xorAndb64('!@#$%^&*())<>,.?/:;KKEWO32823@#*@*#*&&#@(*(#&&^$#', 'abcabcabcabaaa', True)
print(en)
print(xorAndb64(en, 'abcabcabcabaaa', False))
```