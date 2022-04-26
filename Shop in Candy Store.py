def candyStore(self, candies,N,K):
        
        candies.sort()
        
        t = math.ceil(N/(K + 1))
        
        return [sum(candies[:t]), sum(candies[N - t:])]
