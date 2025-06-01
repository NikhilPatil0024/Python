# Match Case Statements.

x = int(input("Enter the x: "))
match x:
    case 10:
        print("hi")
    case 20:
        print("Hey")
    case _ if x==80: # to use "if" with case - use the default case. and then start the "if" statement. case _ if() ✅.
        print("Hellow")
    case _: # this is default case denoted with "_" underscore - default can only be used as last case.
        print('shhhh!')
