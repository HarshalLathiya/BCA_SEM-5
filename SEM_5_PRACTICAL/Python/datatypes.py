#write a python code to demonstrate the use of all the data types

# 1. Numeric types
integer_value = 10            
float_value = 3.14          
complex_value = 2 + 3j

print("Integer:", integer_value)
print("Float:", float_value)
print("Complex:", complex_value)

# 2. Sequence types
string_value = "Hello, Python!" 
list_value = [1, 2, 3, 4]
tuple_value = (10, 20, 30)
range_value = range(5)

print("String:", string_value)
print("List:", list_value)
print("Tuple:", tuple_value)
print("Range:", list(range_value))

# 3. Set types
set_value = {1, 2, 3, 4, 4}       # set (duplicates are removed)
frozenset_value = frozenset([5, 6, 7])  # frozenset (immutable set)

print("Set:", set_value)
print("Frozenset:", frozenset_value)

# 4. Mapping type
dict_value = {"name": "Harshal", "age": 20}  # dict

print("Dictionary:", dict_value)

# 5. Boolean type
bool_value = True

print("Boolean:", bool_value)

# 6. Binary types
bytes_value = b"Hello"           # bytes (immutable)
bytearray_value = bytearray(b"World")  # bytearray (mutable)
memoryview_value = memoryview(bytes_value)

print("Bytes:", bytes_value)
print("Bytearray:", bytearray_value)
print("Memoryview:", memoryview_value.tolist())  # Convert to list for display

# 7. NoneType
none_value = None                # NoneType

print("NoneType:", none_value)
