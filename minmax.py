MAX=1000
MIN=-1000
def minmax(depth,nodeindex,mp,values,alpha,beta):
    if depth==3:
        return values[nodeindex]
    if mp:
        best=MIN
        for i in range(0,2):
            val=minmax(depth+1,nodeindex*2+i,False,values,alpha,beta)
            best=max(best,val)
            alpha=max(alpha,best)
            if beta<=alpha:
                break
        return best
    else:
        best=MAX
        for i in range(0,2):
            val=minmax(depth+1,nodeindex*2+i,True,values,alpha,beta)
            best=min(best,val)
            beta=min(beta,best)
            if beta<=alpha:
                break
        return best
values=[3,5,6,9,1,2,0,-1]
print("The optimal value is :",minmax(0,0,True,values,MIN,MAX))