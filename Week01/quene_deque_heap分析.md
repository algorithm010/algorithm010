 1. 谷歌搜索[python quene](https://docs.python.org/3/library/queue.html) 
 2. 点开第一个连接[A synchronized queue class](https://docs.python.org/3/library/queue.html)
 3. 能看到关于quene的代码都被保存在**Lib/queue.py**,可以下载python源码进行查阅。

这个模块中实现了三种类型的队列

```
class queue.Queue(maxsize=0)#FIFO队列
class queue.LifoQueue(maxsize=0)#LIFO队列
class queue.PriorityQueue(maxsize=0)#优先级队列，通常需要借助heapq模块
```
>队列模块实现了多生产者、多使用者队列。当信息必须在多个线程之间安全地交换时，它在线程编程中特别有用。这个模块中的Queue类实现了所有所需的锁定语义。
除此之外，还实现了名为`class queue.SimpleQueue`，它是最基本的FIFO队列，缺少任务追踪等功能。


### `Quene()`

#### __init__()
实例方法，定义了队列相关操作需要的锁、标识符等

```
def __init__(self, maxsize=0):
        self.maxsize = maxsize
        self._init(maxsize)

        # mutex must be held whenever the queue is mutating.  All methods
        # that acquire mutex must release it before returning.  mutex
        # is shared between the three conditions, so acquiring and
        # releasing the conditions also acquires and releases mutex.
        self.mutex = threading.Lock()

        # Notify not_empty whenever an item is added to the queue; a
        # thread waiting to get is notified then.
        self.not_empty = threading.Condition(self.mutex)

        # Notify not_full whenever an item is removed from the queue;
        # a thread waiting to put is notified then.
        self.not_full = threading.Condition(self.mutex)

        # Notify all_tasks_done whenever the number of unfinished tasks
        # drops to zero; thread waiting to join() is notified to resume
        self.all_tasks_done = threading.Condition(self.mutex)
        self.unfinished_tasks = 0
```


#### task_done 标识前面的入队任务已完成
由队列使用者线程使用。对于用于获取任务的每个`get（）`，后续调用`task_done()`告诉队列任务的处理已完成。

```
    def task_done(self):
        '''Indicate that a formerly enqueued task is complete.

        Used by Queue consumer threads.  For each get() used to fetch a task,
        a subsequent call to task_done() tells the queue that the processing
        on the task is complete.

        If a join() is currently blocking, it will resume when all items
        have been processed (meaning that a task_done() call was received
        for every item that had been put() into the queue).

        Raises a ValueError if called more times than there were items
        placed in the queue.
        '''
        with self.all_tasks_done:
            unfinished = self.unfinished_tasks - 1
            if unfinished <= 0:
                if unfinished < 0:
                    raise ValueError('task_done() called too many times')
                self.all_tasks_done.notify_all()
            self.unfinished_tasks = unfinished
```

#### join 阻塞直到队列中所有元素被处理

每当有任务添加到队列中时，未完成的任务count计数增加；当消费者进程调用`task_done()`标识任务已被释放所有工作已完成时，任务计数减少。
```
    def join(self):
        '''Blocks until all items in the Queue have been gotten and processed.

        The count of unfinished tasks goes up whenever an item is added to the
        queue. The count goes down whenever a consumer thread calls task_done()
        to indicate the item was retrieved and all work on it is complete.

        When the count of unfinished tasks drops to zero, join() unblocks.
        '''
        with self.all_tasks_done:
            while self.unfinished_tasks:
                self.all_tasks_done.wait()
```

#### qsize 返回队列的大致大小
```
def qsize(self):
        '''Return the approximate size of the queue (not reliable!).'''
        with self.mutex:
            return self._qsize()
```
#### empty 判断队列是否为空
```
def empty(self):
        '''Return True if the queue is empty, False otherwise (not reliable!).

        This method is likely to be removed at some point.  Use qsize() == 0
        as a direct substitute, but be aware that either approach risks a race
        condition where a queue can grow before the result of empty() or
        qsize() can be used.

        To create code that needs to wait for all queued tasks to be
        completed, the preferred technique is to use the join() method.
        '''
        with self.mutex:
            return not self._qsize()
```

#### full 判断队列是否已满
```
def full(self):
        '''Return True if the queue is full, False otherwise (not reliable!).

        This method is likely to be removed at some point.  Use qsize() >= n
        as a direct substitute, but be aware that either approach risks a race
        condition where a queue can shrink before the result of full() or
        qsize() can be used.
        '''
        with self.mutex:
            return 0 < self.maxsize <= self._qsize()
```

#### put 入队列
```
def put(self, item, block=True, timeout=None):
        '''Put an item into the queue.

        If optional args 'block' is true and 'timeout' is None (the default),
        block if necessary until a free slot is available. If 'timeout' is
        a non-negative number, it blocks at most 'timeout' seconds and raises
        the Full exception if no free slot was available within that time.
        Otherwise ('block' is false), put an item on the queue if a free slot
        is immediately available, else raise the Full exception ('timeout'
        is ignored in that case).
        '''
        with self.not_full:
            if self.maxsize > 0:
                if not block:
                    if self._qsize() >= self.maxsize:
                        raise Full
                elif timeout is None:
                    while self._qsize() >= self.maxsize:
                        self.not_full.wait()
                elif timeout < 0:
                    raise ValueError("'timeout' must be a non-negative number")
                else:
                    endtime = time() + timeout
                    while self._qsize() >= self.maxsize:
                        remaining = endtime - time()
                        if remaining <= 0.0:
                            raise Full
                        self.not_full.wait(remaining)
            self._put(item)
            self.unfinished_tasks += 1
            self.not_empty.notify()
```

#### get 从队列中取出元素
```
def get(self, block=True, timeout=None):
        '''Remove and return an item from the queue.

        If optional args 'block' is true and 'timeout' is None (the default),
        block if necessary until an item is available. If 'timeout' is
        a non-negative number, it blocks at most 'timeout' seconds and raises
        the Empty exception if no item was available within that time.
        Otherwise ('block' is false), return an item if one is immediately
        available, else raise the Empty exception ('timeout' is ignored
        in that case).
        '''
        with self.not_empty:
            if not block:
                if not self._qsize():
                    raise Empty
            elif timeout is None:
                while not self._qsize():
                    self.not_empty.wait()
            elif timeout < 0:
                raise ValueError("'timeout' must be a non-negative number")
            else:
                endtime = time() + timeout
                while not self._qsize():
                    remaining = endtime - time()
                    if remaining <= 0.0:
                        raise Empty
                    self.not_empty.wait(remaining)
            item = self._get()
            self.not_full.notify()
            return item

    def put_nowait(self, item):
        '''Put an item into the queue without blocking.

        Only enqueue the item if a free slot is immediately available.
        Otherwise raise the Full exception.
        '''
        return self.put(item, block=False)
```
#### put_nowait 在不阻塞的情况下入队列
```
    def put_nowait(self, item):
        '''Put an item into the queue without blocking.

        Only enqueue the item if a free slot is immediately available.
        Otherwise raise the Full exception.
        '''
        return self.put(item, block=False)
```
#### get_nowait 不阻塞的情况下出队列
```
    def get_nowait(self):
        '''Remove and return an item from the queue without blocking.

        Only get an item if one is immediately available. Otherwise
        raise the Empty exception.
        '''
        return self.get(block=False)
```
#### 被继承时，必须重写的方法
`_init()`方法中默认使用`deque`实现队列

```
# Initialize the queue representation
    def _init(self, maxsize):
        self.queue = deque()

    def _qsize(self):
        return len(self.queue)

    # Put a new item in the queue
    def _put(self, item):
        self.queue.append(item)

    # Get an item from the queue
    def _get(self):
        return self.queue.popleft()
```

### PriorityQueue(Queue)
继承自`Quene`,`deque`使用`[]`实现；但是注意到入队和出队操作实际调用的是`heappush`和`heappop `,显然内部实现优先级队列的时候是采用的`heapq`实现的


```
class PriorityQueue(Queue):
    '''Variant of Queue that retrieves open entries in priority order (lowest first).

    Entries are typically tuples of the form:  (priority number, data).
    '''

    def _init(self, maxsize):
        self.queue = []

    def _qsize(self):
        return len(self.queue)

    def _put(self, item):
        heappush(self.queue, item)

    def _get(self):
        return heappop(self.queue)
```

### LifoQueue(Queue)
继承自`Quene`,`deque`使用`[]`实现；内部入队出队操作调用的是`List`的`append`和`pop`方法。

```
class LifoQueue(Queue):
    '''Variant of Queue that retrieves most recently added entries first.'''

    def _init(self, maxsize):
        self.queue = []

    def _qsize(self):
        return len(self.queue)

    def _put(self, item):
        self.queue.append(item)

    def _get(self):
        return self.queue.pop()
```

### heapq
链接在此[heapq](https://docs.python.org/2/library/heapq.html)，可以看到对应的源码在`Lib/heapq.py`文件下

>python中的优先级队列是使用`heapq`(默认小根堆)来实现的，而`堆`的实现方式多种多样，这里是用数组存储的`二叉树`实现的。

堆是二叉树，每个父节点的值小于或等于其子节点的值。使用数组`List`实现`heap[k] <= heap[2*k+1] `和 `heap[k] <= heap[2*k+2]`(k从0计数)以满足堆的结构
其内部实现的方法较多，这里捡几个常用的说

#### heappush 往堆里插入元素
```
def heappush(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1)
```

#### heappop 从堆顶出元素
```
def heappop(heap):
    """Pop the smallest item off the heap, maintaining the heap invariant."""
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt
```

#### heapreplace 替换元素
等价于`heappop`+`heappush`，更推荐使用。
```
def heapreplace(heap, item):
    """Pop and return the current smallest value, and add the new item.

    This is more efficient than heappop() followed by heappush(), and can be
    more appropriate when using a fixed-size heap.  Note that the value
    returned may be larger than item!  That constrains reasonable uses of
    this routine unless written as part of a conditional replacement:

        if item > heap[0]:
            item = heapreplace(heap, item)
    """
    returnitem = heap[0]    # raises appropriate IndexError if heap is empty
    heap[0] = item
    _siftup(heap, 0)
    return returnitem
```

#### heappushpop
等价于`heappush` + `heappop`
```
def heappushpop(heap, item):
    """Fast version of a heappush followed by a heappop."""
    if heap and heap[0] < item:
        item, heap[0] = heap[0], item
        _siftup(heap, 0)
    return item
```

#### heapify 堆化
原地将List转化为堆，内部调用`_siftup`和`_siftdown`实现，建堆时，无需考虑叶子节点，所以只用考察数组头、中部之间的元素
```
def heapify(x):
    """Transform list into a heap, in-place, in O(len(x)) time."""
    n = len(x)
    # Transform bottom-up.  The largest index there's any point to looking at
    # is the largest with a child index in-range, so must have 2*i + 1 < n,
    # or i < (n-1)/2.  If n is even = 2*j, this is (2*j-1)/2 = j-1/2 so
    # j-1 is the largest, which is n//2 - 1.  If n is odd = 2*j+1, this is
    # (2*j+1-1)/2 = j so j-1 is the largest, and that's again n//2-1.
    for i in reversed(range(n//2)):
        _siftup(x, i)
```

#### _siftup
```
def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)
```

#### _siftdown
```
def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem
```



### deque 双端队列
连接在此[deque](https://docs.python.org/2/library/collections.html),支持从两端插入和删除元素。源代码在`Lib/collections/__init__.py`。
`deque`是线程安全且内存搞笑的插入和删除操作，从两端插入删除的时间复杂度可视作O(1)

常见的操作有：

`append、appendleft、clear、copy、count、extend、extendleft`
`pop、popleft、remove、reverse、rotate`




