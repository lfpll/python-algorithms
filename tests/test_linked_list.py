from linked_list.linked_list import Double_Side_Linked_List as Linked_List

class Test_Deque:

    vals = [1,2,3,4,5,6]
    def fill_vals_for_test(self,link):
        for val in self.vals:
            yield link.addFirst(val)

    def test_add_first(self):
        linked_list = Linked_List()
        generator = self.fill_vals_for_test(linked_list)
        next(generator)
        assert(linked_list.head.value == 1)
        assert(linked_list.tail.value == 1)

    def test_add_last(self):
        linked_list = Linked_List()
        generator = self.fill_vals_for_test(linked_list)
        next(generator)
        assert(linked_list.head.value == 1)
        assert(linked_list.tail.value == 1)

        linked_list.addLast(2)
        assert(linked_list.tail.value == 2)
        pass

    def test_fill_and_empty(self):
        linked_list = Linked_List()
        generator = self.fill_vals_for_test(linked_list)
        next(generator)
        next(generator)
        next(generator)
        
        linked_list.getFirst()
        linked_list.getFirst()
        linked_list.getFirst()

        assert(linked_list.size == 0)
        assert(linked_list.head is None and linked_list.tail is None)

    def test_size_four(self):
        linked_list = Linked_List()
        generator = self.fill_vals_for_test(linked_list)
        next(generator)
        next(generator)
        next(generator)
        next(generator)
        assert(linked_list.size == 4)
        

    def test_sequence_cmds(self):
        linked_list = Linked_List()
        generator = self.fill_vals_for_test(linked_list)
        linked_list.addFirst(1)
        linked_list.addLast(2)
        linked_list.addLast(3)
        fst_val = linked_list.getFirst()
        sec_val = linked_list.getLast()

        # Testing head and tail change when add and removing
        assert(linked_list.tail == linked_list.head)
        assert(fst_val == 1 and sec_val == 3)

    def test_find_by_index(self):
        linked_list = Linked_List()
        generator = self.fill_vals_for_test(linked_list)
        next(generator)
        next(generator)
        next(generator)
        assert(linked_list.getByIndex(2) == 1)
        assert(linked_list.getByIndex(0) == 3)
        assert(linked_list.tail == linked_list.head)
        assert(linked_list.getByIndex(0) == 2)
        assert(linked_list.tail is None and linked_list.head is None)

    def test_get_last(self):
        linked_list = Linked_List()
        generator = self.fill_vals_for_test(linked_list)
        next(generator)
        next(generator)
        next(generator)
        assert(linked_list.getLast() == 1)
        assert(linked_list.getLast() == 2)
        assert(linked_list.getLast() == 3)

    def test_get_first(self):
        linked_list = Linked_List()
        generator = self.fill_vals_for_test(linked_list)
        next(generator)
        next(generator)
        next(generator)
        assert(linked_list.getFirst() == 3)
        assert(linked_list.getFirst() == 2)
        assert(linked_list.getFirst() == 1)

