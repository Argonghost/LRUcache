#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 00:37:55 2023

@author: mac
"""
'''
This is a simple LRU cache system implementation using doubly linked lists.  Feel free to use, copy, or modify :)
'''

class DLinkedNode:
    def __init__(self, key, val, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next


class LRU_Cache:
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity
        self.cache = {}
        self.head = DLinkedNode(0, 0)
        self.tail = DLinkedNode(0, 0)
        self.head.pre = None
        self.head.next = self.tail
        self.tail.pre = self.head
        self.tail.next = None

    def get(self, key):
        if not key in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.val

    def put(self, key, value):
        if self.capacity == 0:
            print("Can't perform operations on 0 capacity cache")
            return
        
        if not key in self.cache:
            newNode = DLinkedNode(key, value)
            self.cache[key] = newNode
            self.addNode(newNode)
            self.count += 1
            if self.count > self.capacity:
                tail = self.popTail()
                del self.cache[tail.key]
                self.count -= 1
        else:
            node = self.cache[key]
            node.val = value
            self.addNode(node)

    def addNode(self, node):
        node.next = self.head.next
        node.pre = self.head
        self.head.next.pre = node
        self.head.next = node

    def removeNode(self, node):
        pre = node.pre
        next = node.next
        pre.next = next
        next.pre = pre

    def moveToHead(self, node):
        self.removeNode(node)
        self.addNode(node)

    def popTail(self):
        pre = self.tail.pre
        self.removeNode(pre)
        return pre

# Normal Case:
our_cache = LRU_Cache(5)
our_cache.put(1, 1)
our_cache.put(2, 2)
our_cache.put(3, 3)
our_cache.put(4, 4)

print(our_cache.get(1))

print(our_cache.get(2))

print(our_cache.get(9))


our_cache.put(5, 5)
our_cache.put(6, 6)

print(our_cache.get(3))

'''
Now lets investigate test cases 
'''

# Edge Case:
our_cache = LRU_Cache(2)
our_cache.put(1, 1)
our_cache.put(2, 2)
our_cache.put(1, 10)
print(our_cache.get(1))
# Will return 10
print(our_cache.get(2))
# Willreturn 2

our_cache = LRU_Cache(0)
our_cache.put(1, 1)
# sWill print "Can't perform operations on 0 capacity cache"
print(our_cache.get(1))
# should return -1