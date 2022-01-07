
heap = [x*0 for x in range(20)]
size = 0
def insert_max_heap(val):
    global size, heap
    size += 1
    
    heap.insert(size,val)

    i = size

    while i > 1 :
        parent = (i // 2)
        if heap[parent] < heap[i]:
            heap[parent],heap[i] = heap[i],heap[parent]
            i = parent
        else:
            return
def insert_min_heap(val):
    global size, heap
    size += 1
    
    heap.insert(size,val)

    i = size

    while i > 1 :
        parent = (i // 2)
        if heap[parent] > heap[i]:
            heap[parent],heap[i] = heap[i],heap[parent]
            i = parent
        else:
            return

def left(i):
    return 2 * i

def right(i):
    return (2 * i )  + 1

def delete_max_heap():
    global heap,size
    val = heap[1]
    temp = heap[size]
    size -= 1
    i = 1
    heap[i] = temp
    
    while i < size:
        l = left(i)
        r = right(i)
        
        if heap[l] > heap[i]:
            heap[l],heap[i] = heap[i],heap[l]
            i = l
        elif heap[r] > heap[i]:
            heap[r],heap[i] = heap[i],heap[r]
            i = r
        else:
            break
    return val

def print_heap():
    global size
    for i in range(1,size+1):
        print(heap[i],end=" ")
        # print(heap[i])
insert_max_heap(1)
insert_max_heap(3)
insert_max_heap(5)
insert_max_heap(4)
insert_max_heap(6)
print_heap()
print()
# print(heap)
print(delete_max_heap())
print(delete_max_heap())
# print(delete_max_heap())
# print_heap()
# print()
# print("d",heap[size],heap[1],size)
# print(heap)
