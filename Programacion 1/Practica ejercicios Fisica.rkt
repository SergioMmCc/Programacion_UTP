#lang racket
(define (promedio a b c d e)
  (exact->inexact(/(+ a b c d e)5))
  )
(promedio 1 4 6 15 10)

(define (distancia x1 y1 x2 y2)
  (sqrt(+(expt(- x2 x1)2)(expt(- y2 y1)2)))
  )
(distancia 3 6 9 10)

(define (area_c r)
  (*(expt r 2)pi)
  )
(area_c 4)

(define (caida v0 t x g)
  (+(* v0 t)(* x g (expt t 2)))
  )
(caida 2 4 1/2 5)