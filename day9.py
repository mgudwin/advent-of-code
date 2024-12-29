import copy
import time

start = time.time()
example_text = "2333133121414131402"
with open('Inputs/day9_input.txt', 'r') as file:
    input_text = file.read().rstrip()


class Disk():
    def __init__(self):
        self.block_list = None
        self.id_list = None
        self.orig_id_list = None

    def read_block_list(self, text):
        self.block_list = list(text)

    def convert_block_list_to_id(self):
        id_list = []
        id = 0
        for ix, c in enumerate(self.block_list):
            if not (ix % 2):
                for t in range(int(c)):
                    id_list.append(str(id))
                id += 1
            else:
                for t in range(int(c)):
                    id_list.append('.')
        self.id_list = id_list
        self.orig_id_list = copy.deepcopy(self.id_list)
        # print("Disk format now\n{}".format(self.orig_id_list))

    def find_last_index(self, search_item):
        i = len(self.id_list) - 1
        while i >= 0:
            if self.id_list[i] == search_item:
                return i
            else:
                i -= 1

    def disk_defragged(self, disk):
        # find leftmost '.', then look at string to the right
        l_freespace_ix = disk.index(".")
        r_disk_contents = disk[l_freespace_ix:]
        # if there are non-'.' to the right, not defragged
        r_disk_contents_ids = [i for i in r_disk_contents if i != '.']
        return bool(len(r_disk_contents_ids) == 0)

    def defrag(self):
        while not self.disk_defragged(self.id_list):
            l_freespace_ix = self.id_list.index(".")
            r_disk_contents = self.id_list[l_freespace_ix:]
            last_id = [i for i in r_disk_contents if i != '.'][-1]
            last_ix = self.find_last_index(last_id)
            temp_id = self.id_list[last_ix]
            temp_fspace = self.id_list[l_freespace_ix]
            self.id_list[l_freespace_ix] = temp_id
            self.id_list[last_ix] = temp_fspace
            # print("Disk is now\n{}".format(self.id_list))

    def index_disk(self):
        loc_dict = {}
        for ix, item in enumerate(self.id_list):
            if item in loc_dict.keys():
                loc_dict[item].append(ix)
            else:
                loc_dict[item] = [ix]
        start_index = None
        prev_index = None
        freespace_num = 0
        loc_dict['freespace'] = {}
        for ix in loc_dict["."]:
            size = None
            if start_index is None:
                start_index = ix
            else:
                if ix - prev_index != 1:
                    # break in sequence
                    # {'freespace' : 0: { start: , size: }, 1: {}...}
                    size = prev_index - start_index + 1
                    loc_dict['freespace'][str(freespace_num)] = {
                        'start': start_index,
                        'size': size}
                    start_index = ix
                    freespace_num += 1
            if ix == loc_dict["."][-1]:
                loc_dict['freespace'][str(freespace_num)] = {
                    'start': ix,
                    'size': 1}
            prev_index = ix
        loc_dict.pop(".")
        return loc_dict

    def better_defrag(self):
        loc_dict = self.index_disk()
        # print("Dict is\n{}".format(loc_dict))
        list_of_ids = sorted(list([i for i in loc_dict.keys() if i != '.']))
        # print("List of ID's are\n{}".format(list_of_ids))
        for id in list_of_ids[::-1]:
            _indicies = loc_dict[id]
            # print("indicies", _indicies)
            num_blocks = len(_indicies)
            for fs in loc_dict['freespace'].keys():
                _fs_start = loc_dict['freespace'][fs]['start']
                _fs_size = loc_dict['freespace'][fs]['size']
                _fd_indecies = range(_fs_start, _fs_start + _fs_size, 1)
                if _fs_size >= num_blocks:
                    if _fs_start >= _indicies[0]:
                        loc_dict = self.index_disk()
                        break
                    # print("Freespace found in ",
                    #       loc_dict['freespace'][fs], _fd_indecies)
                    # print(self.id_list)
                    # Swap positions
                    for ix, index in enumerate(_indicies):
                        temp = self.id_list[index]
                        self.id_list[index] = '.'
                        self.id_list[_fd_indecies[ix]] = temp
                    # print(self.id_list)
                    loc_dict = self.index_disk()
                    break
                loc_dict = self.index_disk()
        # print("After better defrag, disk is now\n{}".format(self.id_list))

    def calculate_checksum(self):
        running_sum = 0
        for ix, char in enumerate(self.id_list):
            if char == '.':
                continue
            running_sum += ix * int(char)
        # print("{} * {} = {}".format(ix, char, ix * int(char)))
        print("Checksum is {}".format(running_sum))


d = Disk()
print("Reading disk blocks...")
# d.read_block_list(example_text)
d.read_block_list(input_text)
print("Converting blocks to ids...")
d.convert_block_list_to_id()
# d.defrag()
print("Defragging disk, but better...")
d.better_defrag()
print("Complete, calculating checksum...")
d.calculate_checksum()
end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")
