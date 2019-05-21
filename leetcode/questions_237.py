#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-21 21:55
# @Author  : Allen


class Solution:

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node_next = node.next
        after_node_next = node_next.next
        node.val = node_next.val
        node.next = after_node_next
