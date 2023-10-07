#lang racket
(define (factorial n)
  (if (> n 0)
      (* n (factorial (- n 1)))
      1))

(define (potencia num exp)
  (if (> num 0)
    (if(> exp 0) (* num(potencia num(- exp 1)))1)
    0))

(define (secuencia num exp)
  (if (> num 0)
      (if (> exp 0)(+(potencia num exp)(secuencia num(- exp 1)))1)
      0))

(define (suma a b)
  (*(- (* a -1) b)-1))

(define (multiplicar x y)
  (if (and(not (= x 0))(not(= y 0)))
      (if (> y 1) (+ x (multiplicar x(- y 1))) x)
      0))

(define (fibonacci n)
  (if (not (= n 0))
      (if (not (= n 1))
          (+(fibonacci (- n 1))(fibonacci (- n 2)))
          1)0))

(define (suma2 n)
  (if (not (= n 0))
      (if (not (= n 1))
          (+ n (suma2 (- n 1)))
          1)0))
