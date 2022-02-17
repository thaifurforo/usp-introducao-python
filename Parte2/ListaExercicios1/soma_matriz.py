def soma_matrizes(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        m3 = []
        m3_list = []
        for list in range(len(m1)):
            for item in range(len(m1[list])):
                n = m1[list][item] + m2[list][item]
                m3_list.append(n)
            m3.append(m3_list)
            m3_list = []
        return m3
    else:
        return False
