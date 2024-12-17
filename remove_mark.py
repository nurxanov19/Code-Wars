def removes(s):
    return '' if not s else s[:-1] if s[-1] == '!' else s
print(removes("Hi!"))