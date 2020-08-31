import sys
X,K,D = map(int, input().split())
if X < 0: X = abs(X) #Xがマイナスならプラスに変換しておく
 
if X // D > K:
    X = X - (K * D)
    print(X)
    sys.exit() #ここはOK
 
if (X // D) <= K:
    if X % D >= abs((X % D)-D):
        if (K - (X // D)) % 2 == 1:
            print(abs((X % D)-D))
            sys.exit()
        else:
            print(X % D)
            sys.exit()
    else:
        if (K - (X // D)) % 2 == 1:
            print(abs((X % D)-D))
            sys.exit()
        else:
            print(X % D)
            sys.exit()
