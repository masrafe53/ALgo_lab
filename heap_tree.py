max_heap = [5, 7, 3, 2]
def heapify_down(heap, index):
    largest = index
    left_child_index = 2 * index + 1
    right_child_index = 2 * index + 2
    heap_size = len(heap)

    if left_child_index < heap_size and heap[left_child_index] > heap[largest]:
        largest = left_child_index

    if right_child_index < heap_size and heap[right_child_index] > heap[largest]:
        largest = right_child_index

    if largest != index:
        heap[index], heap[largest] = heap[largest], heap[index]
        heapify_down(heap, largest)
if len(max_heap) == 0:
    print("Heap is empty")
else:
    root = max_heap[0]
    max_heap[0] = max_heap[-1]  
    max_heap.pop()  
    heapify_down(max_heap, 0)

    print("Deleted:", root)
    print("Max Heap after deletion:", max_heap)
