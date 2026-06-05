class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st =[]
        fleets = [(position[i],speed[i]) for i in range(len(position))]
        #sort the fleets to get the relative order
        fleets.sort()
        for i in range(len(position)-1,-1,-1):
            if not st:
                st.append(fleets[i])
                continue
            #check if the current fleet would meet the car in front of it
            current_time_to_reach = (target-fleets[i][0])/fleets[i][1]
            prev_time_to_reach = (target-st[-1][0])/st[-1][1]
            if current_time_to_reach <=prev_time_to_reach:
                #the prev and current would become fleet
                continue
            st.append(fleets[i])
        return len(st)
        