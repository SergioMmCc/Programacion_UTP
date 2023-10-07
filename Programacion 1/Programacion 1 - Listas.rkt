#lang racket
(define lista1 (list 0 1 2 3 4 5 6))
(define (producto lista)
  (cond
    [(empty? lista) 1]
    [else (* (first lista) (producto (rest lista)))]
    ))

(define (elemento_n lista n)
  (cond
    [(empty? lista) "El elemento no esta en la lista"]
    [(equal? n 1) (first lista)]
    [else (elemento_n (rest lista) (- n 1))]
    ))

(define (longitud lista)
  (cond
    [(empty? lista) 0]
    [else (+ 1 (longitud (rest lista)))]
    )
  )

(define (suma lista)
  (cond
    [(empty? lista) 0]
    [else (+ (first lista) (suma (rest lista)))]
    ))
    

(define (promedio lista)
  (/ (suma lista)
     (longitud lista)))