class TimeMap:

    def __init__(self):
        self.store={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=[]
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        values=self.store[key]
        l=0
        r=len(values)-1
        result=""
        while l<=r:
            mid=(l+r)//2
            time=values[mid][0]
            value=values[mid][1]
            if time<=timestamp:
                result=value
                l=mid+1
            else:
                r=mid-1
        return result 

        # result=""
        # for time,value in self.store[key]:
        #     if time<=timestamp:
        #         result=value
        #     else:
        #         break
        # return result 
