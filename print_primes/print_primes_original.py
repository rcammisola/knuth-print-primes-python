
def print_values():
    M = 1000
    RR = 50
    CC = 4
    ORDMAX = 30
    P = [0] * (M + 1)
    PAGENUMBER = 0
    PAGEOFFSET = 0
    ROWOFFSET = 0
    JPRIME = False
    ORD = 0
    SQUARE = 0
    N = 0
    MULT = [0 for _ in range(ORDMAX)]

    J = 1
    K = 1
    P[1] = 2
    ORD = 2
    SQUARE = 9

    while K < M:
        while True:
            J += 2
            if J == SQUARE:
                ORD += 1
                SQUARE=P[ORD]*P[ORD]
                MULT[ORD-1] = J

            N=2
            JPRIME=True
            while (N < ORD and JPRIME):
                while (MULT[N] < J):
                    MULT[N] += P[N] + P[N]
                if (MULT[N] == J):
                    JPRIME=False
                N += 1

            if JPRIME:
                break
        K += 1
        P[K] = J

    PAGENUMBER = 1
    PAGEOFFSET = 1
    while PAGEOFFSET <= M:
        print("The First ", M, " Prime Numbers --- Page ", PAGENUMBER)
        for ROWOFFSET in range(PAGEOFFSET, PAGEOFFSET+RR-1):
          for C in range(CC+1):
            if (ROWOFFSET+C*RR <= M):
              print("%10s" % P[ROWOFFSET+C*RR], end="")
          print("")

        print("")
        PAGENUMBER += 1
        PAGEOFFSET += RR*CC


if __name__ == "__main__":
    print_values()
