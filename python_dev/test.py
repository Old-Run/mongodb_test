

def sol(m, n, head):
    ans = [[-1]*n for _ in range(m)]
    vector = "right"
    m_idx, n_idx = 0, 0
    m_o, n_o = 0, 0
    for num in head:
        ans[m_idx][n_idx] = num
        print(m_idx, n_idx, num, vector)
        if vector == "right":
            n_idx += 1
            if n_idx >= n or ans[m_idx][n_idx] != -1:
                vector = "down"
                n_idx -= 1
        if vector == "down":
            m_idx += 1
            if m_idx >= m or ans[m_idx][n_idx] != -1:
                vector = "left"
                m_idx -= 1
        if vector == "left":
            n_idx -= 1
            if n_idx < n_o or ans[m_idx][n_idx] != -1:
                vector = "up"
                n_idx += 1
        if vector == "up": 
            m_idx -= 1
            if m_idx < m_o  or ans[m_idx][n_idx] != -1:
                vector = "right"
                m_idx += 1
                n_idx += 1
        

    print(ans)

    return ans


if __name__ == "__main__":
    # Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
    m, n, head = 3, 5, [3,0,2,6,8,1,7,9,4,2,5,5]
    sol(m, n, head)
