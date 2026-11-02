height=[0,1,0,2,1,0,1,3,2,1,2,1]
def trap(height):
        l,r=0,len(height)-1
        leftmax,rightmax,water=0,0,0
        while l<r:
            if height[l]<height[r]:
                leftmax=max(leftmax,height[l])
                water+=leftmax-height[l]
                l+=1
            else:
                rightmax=max(rightmax,height[r])
                water+=rightmax-height[r]
                r-=1
        return water

print(trap(height))