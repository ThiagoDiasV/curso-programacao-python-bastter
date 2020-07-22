my_list = [x for x in range(100) if x % 11 == 0]
from pdb import set_trace

set_trace()
string_list = [str(x) for x in my_list]

print("".join(string_list))