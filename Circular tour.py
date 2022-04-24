'''Suppose there is a circle. There are N petrol pumps on that circle. You will be given two sets of data.
1. The amount of petrol that every petrol pump has.
2. Distance from that petrol pump to the next petrol pump.
Find a starting point where the truck can start to get through the complete circle without exhausting its petrol in between.
Note :  Assume for 1 litre petrol, the truck can go 1 unit of distance.'''

'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''

        def tour(self,lis, n):
        #Code here
            trip_tank,cur_tank,start=0,0,0

            for i in range(n):
                trip_tank+=(lis[i][0]-lis[i][1])
                cur_tank+=(lis[i][0]-lis[i][1])

                if cur_tank<0:
                    cur_tank=0
                    start=i+1

            if trip_tank>=0:
                return start
        return -1
