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
