# IEEE 754 is a standard for representing floating-point numbers (i.e. numbers that can have 
# a fractional part and emulate real numbers).

# Its use is currently ubiquitous in both software (programming languages implementations) 
# and hardware (Floating Point Units (FPU) chips embedded in processors).

# The 2 most widely used IEEE 754 formats are called the single precision (SP, encoded on 
# 32 bits) and double precision (DP, encoded on 64 bits) formats.

# In C/C++, these correspond respectively to the types float and double, in virtually every 
# implementation that supports floating-point numbers
# The default Python implementation, CPython, is written in C and represents Python floats 
# internally as C doubles, and thus as IEEE 754 DP
# In JavaScript, all Numbers are IEEE 754 DP values.
# In Rust, these correspond respectively to the types f32 and f64.
# In Java, these correspond respectively to the types float and double.
# Before Lua 5.3, all numbers were IEEE 754 DP. Since Lua 5.3, numbers can be either 
# IEEE 754 DP or 2's complement integers.
# The Haskell 2010 Language Report defines the Float and Double types for single/double 
# precision floating point numbers. Most, if not all, implementations of Haskell (including 
# GHC) represent Float/Double internally in IEEE 754 SP/DP format.
# As you can see on the images below, IEEE 754 numbers are divided into 3 fields :
# - a sign bit;
# - an exponent encoded on 8 (SP) or 11 (DP) bits;
# - a mantissa (also called significand) encoded on 23 (SP) or 52 (DP) bits.
# The IEEE 754 single-precision encoding scheme
# 
# 
# Your task is to write a function that takes as input a floating point number, and returns 
# the binary IEEE 754 encoding of this number as a string, with fields separated by spaces 
# for readability. If your programming language supports both SP and DP, you will have 2 
# functions to write, one for each type.