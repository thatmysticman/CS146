## Bonus Questions: "An assortment of sorting techniques, part deux"

### Can we use heaps as priority queues? How so? Write an explanation, with the help of pseudocode/diagrams to support your explanation.

We can use heaps as priority queues as they are closely linked in implementation. The way priority queues prioritize aligns with how ranking works in heaps.

Below is pseudocode for inserting an element in both a heap and a priority queue:

#### Heap (Max)
`function insert_heap(heap, element):`      
`  // Add element to the end of the heap`     
`  heap.append(element)`    
`  current_index = len(heap) - 1`    

`  // While element is bigger than its parent, swap and move up`    
`  while current_index > 0 and element > heap[parent(current_index)]:`    
`    swap(heap, current_index, parent(current_index))`    
`    current_index = parent(current_index)`    

#### Priority Queue (Max-Heap Implementation)
`function insert_priority_queue(pq, item, priority):`   
`  // Create a tuple (priority, item) for the queue`   
`  new_node = (priority, item)`   
`  pq.heap.append(new_node)`   
`  current_index = len(pq.heap) - 1`   

`  // While new_node has lower priority (higher number) than parent, swap and move up`   
`  while current_index > 0 and new_node[0] > pq.heap[parent(current_index)][0]:`   
`    swap(pq.heap, current_index, parent(current_index))`   
`    current_index = parent(current_index)`   

They both:
- add an element to the end
- use a "bubbling up" process to maintain the order
- involve comparing with the parent and swapping if needed

### Given a max heap, is there a way to use the max heap as a min heap, without writing a whole min heap implementation? Is the opposite also true? Justify your answer with pseudocode, and/or python OR java code, and explain your answer.  

Yes, you can use a max heap as a min heap, and vice versa, with a simple change.
The key is to invert the sign of the values when inserting and extracting elements from the heap. This way, the largest elements in a max heap become the smallest elements in a min heap, and vice versa.

Below is Python pseudocode showing how you can use a max heap as a min heap and vice versa:

Function to insert an element into a heap (max or min)   
`def insert(heap, value):`   
`    # Invert the sign of the value`   
`    inverted_value = -value`   
`    # Insert the inverted value into the heap`   
`    heap.insert(inverted_value)`   

Function to extract the minimum or maximum element from the heap   
`def extract(heap):`   
`    # Extract the inverted value from the heap`   
`    inverted_value = heap.extract()`   
`    # Invert the sign again to get the original value`   
`    original_value = -inverted_value`   
`    return original_value`   

The pseudocode above allows you to use the same heap structure for both max and min heaps by only modifying how values are inserted and extracted. 
By inverting the signs, you switch between max and min heap behaviors without having to implement separate data structures. 
