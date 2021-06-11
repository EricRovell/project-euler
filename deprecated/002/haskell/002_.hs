fib :: Int -> Int
fib 0 = 0
fib 1 = 1
fib n = fib (n - 1) + fib (n - 2)

fibList :: Int -> [Int]
fibList n = map fib [0..n]