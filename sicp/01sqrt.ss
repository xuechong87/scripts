#lang scheme
(define (abs x)
  (if ( > x 0) x (- x)))

(define (square x)
  (* x x))

(define (avg x y)
  (/ (+ x y) 2))

(define (improve guess x)
  (avg guess (/ x guess)))

(define (goodsqrt guess x)
  (<
   (abs (- (square guess) x))
        0.0001))

(define (sqrtinner guess x)
  (if (goodsqrt guess x)
      guess
      (sqrtinner (improve guess x) x) )
  )

(define (sqrt x)
  (sqrtinner 1.0 x))

(sqrt 2)