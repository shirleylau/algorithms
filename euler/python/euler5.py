# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

num = 20

while num
for divisor in range(1, 20):
(->> (range 1000
            )
     (filter (fn [x]
               (or (= (mod x 3) 0)
                   (= (mod x 5) 0))))
     (reduce +))

 (reduce + (filter (fn [x] 
      (or (= (mod x 3) 0)
          (= (mod x 5) 0)) )
    (range 10)))
