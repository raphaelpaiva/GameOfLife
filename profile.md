
Profile parameters: 
board file: scenarios/testboard_100_emptyq.bmp
board size: (100, 100)

# Max Depth: 1
```
         10222005 function calls (10192005 primitive calls) in 47.915 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     4000    0.002    0.000    0.048    0.000 _methods.py:45(_sum)
        1    0.000    0.000    0.000    0.000 cProfile.py:117(__exit__)
31000/1000    0.037    0.000    0.101    0.000 copy.py:128(deepcopy)
    22000    0.002    0.000    0.002    0.000 copy.py:182(_deepcopy_atomic)
     1000    0.003    0.000    0.039    0.000 copy.py:200(_deepcopy_list)
     5000    0.008    0.000    0.036    0.000 copy.py:209(_deepcopy_tuple)
     5000    0.005    0.000    0.027    0.000 copy.py:210(<listcomp>)
     1000    0.004    0.000    0.071    0.000 copy.py:226(_deepcopy_dict)
     4000    0.004    0.000    0.005    0.000 copy.py:242(_keep_alive)
     1000    0.007    0.000    0.087    0.000 copy.py:258(_reconstruct)
     2000    0.001    0.000    0.003    0.000 copy.py:263(<genexpr>)
        1    0.000    0.000    0.000    0.000 copyreg.py:103(_slotnames)
     1000    0.001    0.000    0.002    0.000 copyreg.py:94(__newobj__)
     4000    6.436    0.002   47.738    0.012 gol.py:100(_analyze_range)
 10000000   41.302    0.000   41.302    0.000 gol.py:117(_count_neighbours)
     1000    0.002    0.000    0.002    0.000 gol.py:30(partition)
     1000    0.009    0.000   47.915    0.048 gol.py:71(update_board)
     4000    0.013    0.000   47.802    0.012 gol.py:85(_analyze_quadrant)
     1000    0.001    0.000    0.001    0.000 {built-in method __new__ of type object at 0x00007FFA1AE55C60}
     3000    0.001    0.000    0.001    0.000 {built-in method builtins.getattr}
     1001    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
    44000    0.005    0.000    0.005    0.000 {built-in method builtins.id}
     2000    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
     2000    0.001    0.000    0.001    0.000 {built-in method builtins.issubclass}
     1000    0.008    0.000    0.008    0.000 {method '__deepcopy__' of 'numpy.ndarray' objects}
     1000    0.004    0.000    0.004    0.000 {method '__reduce_ex__' of 'object' objects}
     7000    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    63000    0.007    0.000    0.007    0.000 {method 'get' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'get' of 'mappingproxy' objects}
     1000    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
     4000    0.046    0.000    0.046    0.000 {method 'reduce' of 'numpy.ufunc' objects}
     4000    0.004    0.000    0.052    0.000 {method 'sum' of 'numpy.ndarray' objects}
     1000    0.001    0.000    0.001    0.000 {method 'update' of 'dict' objects}


```
# Max Depth: 2
```
         7198294 function calls (7152294 primitive calls) in 33.190 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    20000    0.006    0.000    0.111    0.000 _methods.py:45(_sum)
        1    0.000    0.000    0.000    0.000 cProfile.py:117(__exit__)
31000/1000    0.036    0.000    0.096    0.000 copy.py:128(deepcopy)
    22000    0.002    0.000    0.002    0.000 copy.py:182(_deepcopy_atomic)
     1000    0.003    0.000    0.039    0.000 copy.py:200(_deepcopy_list)
     5000    0.008    0.000    0.036    0.000 copy.py:209(_deepcopy_tuple)
     5000    0.005    0.000    0.028    0.000 copy.py:210(<listcomp>)
     1000    0.004    0.000    0.069    0.000 copy.py:226(_deepcopy_dict)
     4000    0.003    0.000    0.004    0.000 copy.py:242(_keep_alive)
     1000    0.006    0.000    0.084    0.000 copy.py:258(_reconstruct)
     2000    0.001    0.000    0.003    0.000 copy.py:263(<genexpr>)
     1000    0.001    0.000    0.001    0.000 copyreg.py:94(__newobj__)
    11042    4.498    0.000   32.910    0.003 gol.py:100(_analyze_range)
  6901250   28.412    0.000   28.412    0.000 gol.py:117(_count_neighbours)
     5000    0.007    0.000    0.007    0.000 gol.py:30(partition)
     1000    0.007    0.000   33.190    0.033 gol.py:71(update_board)
20000/4000    0.048    0.000   33.086    0.008 gol.py:85(_analyze_quadrant)
     1000    0.001    0.000    0.001    0.000 {built-in method __new__ of type object at 0x00007FFA1AE55C60}
     3000    0.001    0.000    0.001    0.000 {built-in method builtins.getattr}
     1000    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
    44000    0.005    0.000    0.005    0.000 {built-in method builtins.id}
     2000    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
     2000    0.000    0.000    0.000    0.000 {built-in method builtins.issubclass}
     1000    0.006    0.000    0.006    0.000 {method '__deepcopy__' of 'numpy.ndarray' objects}
     1000    0.003    0.000    0.003    0.000 {method '__reduce_ex__' of 'object' objects}
     7000    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    63000    0.007    0.000    0.007    0.000 {method 'get' of 'dict' objects}
     1000    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
    20000    0.105    0.000    0.105    0.000 {method 'reduce' of 'numpy.ufunc' objects}
    20000    0.011    0.000    0.122    0.000 {method 'sum' of 'numpy.ndarray' objects}
     1000    0.001    0.000    0.001    0.000 {method 'update' of 'dict' objects}


```
# Max Depth: 3
```
         3089520 function calls (2999412 primitive calls) in 13.166 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    64108    0.018    0.000    0.248    0.000 _methods.py:45(_sum)
        1    0.000    0.000    0.000    0.000 cProfile.py:117(__exit__)
31000/1000    0.036    0.000    0.090    0.000 copy.py:128(deepcopy)
    22000    0.002    0.000    0.002    0.000 copy.py:182(_deepcopy_atomic)
     1000    0.003    0.000    0.039    0.000 copy.py:200(_deepcopy_list)
     5000    0.008    0.000    0.036    0.000 copy.py:209(_deepcopy_tuple)
     5000    0.005    0.000    0.028    0.000 copy.py:210(<listcomp>)
     1000    0.003    0.000    0.067    0.000 copy.py:226(_deepcopy_dict)
     4000    0.003    0.000    0.004    0.000 copy.py:242(_keep_alive)
     1000    0.005    0.000    0.080    0.000 copy.py:258(_reconstruct)
     2000    0.001    0.000    0.003    0.000 copy.py:263(<genexpr>)
     1000    0.001    0.000    0.001    0.000 copyreg.py:94(__newobj__)
    16788    1.800    0.000   12.646    0.001 gol.py:100(_analyze_range)
  2599271   10.847    0.000   10.847    0.000 gol.py:117(_count_neighbours)
    16027    0.017    0.000    0.017    0.000 gol.py:30(partition)
     1000    0.006    0.000   13.166    0.013 gol.py:71(update_board)
64108/4000    0.130    0.000   13.069    0.003 gol.py:85(_analyze_quadrant)
     1000    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x00007FFA1AE55C60}
     3000    0.001    0.000    0.001    0.000 {built-in method builtins.getattr}
     1000    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
    44000    0.005    0.000    0.005    0.000 {built-in method builtins.id}
     2000    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
     2000    0.000    0.000    0.000    0.000 {built-in method builtins.issubclass}
     1000    0.005    0.000    0.005    0.000 {method '__deepcopy__' of 'numpy.ndarray' objects}
     1000    0.002    0.000    0.002    0.000 {method '__reduce_ex__' of 'object' objects}
     7000    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    63000    0.007    0.000    0.007    0.000 {method 'get' of 'dict' objects}
     1000    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
    64108    0.229    0.000    0.229    0.000 {method 'reduce' of 'numpy.ufunc' objects}
    64108    0.029    0.000    0.276    0.000 {method 'sum' of 'numpy.ndarray' objects}
     1000    0.001    0.000    0.001    0.000 {method 'update' of 'dict' objects}


```
