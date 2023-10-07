#lang racket
(define (precio x y)
  (* x y)
  )
(precio 15002 1.3)

(define (tiempo tl tm tv)
  (exact->inexact(/(+ tl tm tv)3))
  )
(tiempo 56 89 15)

(define (area x)
  (* x x)
  )
(area 87)

(define (conversion m p pu)
  (*(* m p)pu)
  )
(conversion 5 39.37 12)

(define (salario h d s m)
  (*(*(* h d)s)m)
  )
(salario 8000 8 6 4)

(define (peso l kg)
  (* l kg)
  )
(peso 150 0.453592)