"""
1115. Print FooBar Alternately
Medium

Suppose you are given the following code:

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}

The same instance of FooBar will be passed to two different threads. Thread A will call foo() while thread B will call bar(). Modify the given program to output "foobar" n times.



Example 1:

Input: n = 1
Output: "foobar"
Explanation: There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar(). "foobar" is being output 1 time.

Example 2:

Input: n = 2
Output: "foobarfoobar"
Explanation: "foobar" is being output 2 times.
"""

import threading
class FooBar:
    def __init__(self, n):
        self.n = n
        self.cl1 = threading.Lock()
        self.cl2 = threading.Lock()
        self.cl1.acquire()
        self.cl2.acquire()
        self.cl2.release()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.cl2.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.cl1.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.cl1.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.cl2.release()