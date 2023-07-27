if __name__ == '__main__':
    biglist = []
    scorelist = []
    namelist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        biglist.append([score,name])
        scorelist.append(score)
       
    scorelist = list(set(scorelist))
    scorelist.sort()
    secondmin = scorelist[1]
    
    sollist = []
    for x in biglist:
        if secondmin == x[0]:
            sollist.append(x[1])
    sollist.sort()
    
    [print(u) for u in sollist]