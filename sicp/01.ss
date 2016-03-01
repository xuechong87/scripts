#lang scheme

(define 
  (double x) 
  (* 2 x) 
  )

(double 4)

(define (abs x)
  (cond ((> x 0) x)
        ((= x 0) 0)
        ((< x 0) (- x)))
  )

(define (abs2 x)
  (cond ((< x 0) (- x))
        (else x)))

(define (abs3 x)
  (if (< x 0) (- x) x))

(abs -123)
(abs2 -234)
(abs3 -345)


(define x 5)
(define (between x)
  (and (> x 0) (< x 10)))
(if (between x) "yes" "no" )

(define (test m x y)
  (if (m x y)
      "y"
      "n"))

(define (>= a b)
  (or (> a b) (= a b )))

(test >= 3 5)

(define (>=2 a b)
  (not (< a b)))
(test >=2 7 6 )

(define (max_sum a b c)
  (if (and (>= a b ) (>= b c)) (+ a b)
      (if (>= b c) (max_sum b a c)
          (max_sum c a b)
          )
  ))

(max_sum 3 7 9)



(/ (+ 5 (+ 4 (- 2 (- 3 (+ 6 (/ 4 5))))))
   (* 3 (* (- 6 2) (- 2 7))))


(define (factor x)
  (if (= x 1)
      1
      (* x (factor (- x 1) ))
  ))

(factor 2)

(define (fact x )
  (define (iter product counter)
    (if (> counter x)
        product
        (iter (* counter product)
              (+ counter 1)
              )
        )
    )
  
  (iter 1 1)
 )
(fact 6)

