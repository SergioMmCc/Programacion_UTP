#lang racket
(define centenas (list 100 200 300 400 500 600 700 800 900))

(define (div n)
  (/ n 100))

(define (elevar n)
  (expt n 2))

(define (multiplos_200 n)
  (=(modulo n 200)0))

(define mixto (list "Hola" 4 5 6 #t #t #f "Casa" #f 7 #t))
  