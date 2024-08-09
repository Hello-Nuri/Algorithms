def solution(ineq, eq, n, m):
    if ineq == "<" and eq == "=" :
        if n <= m :
            return 1
        else:
            return 0
    if ineq == ">" and eq == "=" :
        if n >= m:
            return 1
        else:
            return 0
    if ineq == "<" and eq == "!" :
        if n < m :
            return 1
        else:
            return 0
    if ineq == ">" and eq == "!" :
        if n > m:
            return 1
        else:
            return 0