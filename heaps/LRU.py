import heapq
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity=capacity
        self.my_key_hash={}
        self.my_count_hash={}
        self.my_min_heap=[]
        heapq.heapify(self.my_min_heap)

    # @return an integer
    def get(self, key):
        #update count of key by one
        if key in self.my_count_hash:
            count=self.my_count_hash[key]
            self.my_count_hash[key]+=1
            self.my_min_heap[self.my_min_heap.index((key,count))]=(key,count+1)
            return self.my_key_hash[key]
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        #add key to hash
        self.my_key_hash[key]=value
        self.my_count_hash[key]=1
        count= len(self.my_min_heap)
        #get count
        if count < self.capacity:
            heapq.heappush(self.my_min_heap, (key,1))
        else:
            tupe=heapq.heapreplace(self.my_min_heap, (key,1))
            #print(self.my_key_hash, self.my_count_hash)
            del self.my_key_hash[tupe[0]]
            del self.my_count_hash[tupe[0]]
        #check if count heap > capacity
            #pop minimum
            #heapify