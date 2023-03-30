from swap import swap_arr


class Heap():
    def __init__(self, arr: list) -> None:
        assert arr is not None
        self.heap = arr
        self.size = len(arr)
        self.creat_heap()

    def is_empty(self):
        return len(self.heap) == 0

    def get_size(self):
        return self.size

    def add(self, num):
        self.heap.append(num)
        self.size += 1
        idx = self.size
        parent = int((idx - 1) / 2)
        while self.heap[idx] > self.heap[parent]:
            swap_arr(self.heap, idx, parent)
            idx = parent

    def poll(self):
        if self.is_empty():
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.heap.pop()
        self.size -= 1
        self.heapify(0)
        return root

    def heapify(self, idx):
        """
        保证从idx向下的堆偏序
        """
        left = (idx << 1) + 1

        while left < self.size:
            largest = left
            if (left + 1) < self.size:
                largest = left if self.heap[left] > self.heap[left+1] else left+1

            largest = idx if self.heap[idx] > self.heap[largest] else largest

            if largest == idx:
                break

            swap_arr(self.heap, idx, largest)

            idx = largest
            left = (idx << 1) + 1

    def creat_heap(self):
        i = (self.size - 1) >> 1
        while i >= 0:
            self.heapify(i)
            i -= 1


if __name__ == '__main__':
    nums = [0, 123, 24, 23, 45, 51]
    heap = Heap(nums)
    while not heap.is_empty():
        print(heap.poll())
