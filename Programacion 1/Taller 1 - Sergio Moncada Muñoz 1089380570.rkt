#lang racket
;Sergio Moncada Muñoz
;1089380570

;1. Sumar 2 numeros recursivamente. No usar el operador "+".
(define (suma a b)
  (cond
    [(> a b)
      (if (> a b)
      (+ 1 (suma (- a 1) b))
      (* 2 b))]
    [else
      (if (> b a)
      (+ 1 (suma a (- b 1)))
      (* 2 a))]
  ))

(print "Ejercicio 1")
(suma 67 45)
(suma 33 60)


;2. Multiplicar 2 numeros recursivamente. No usar el operador "*".
(define (multiplicar x y)
  (if (and(not (= x 0))(not(= y 0)))
      (if (> y 1) (+ x (multiplicar x(- y 1))) x)
      0))

(print "Ejercicio 2")
(multiplicar 120 98)
(multiplicar 23 45)


; 3. Implementar la serie (Fibonacci n): 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
(define (fibonacci n)
  (if (not (= n 0))
      (if (not (= n 1))
          (+(fibonacci (- n 1))(fibonacci (- n 2)))
          1)0))

(print "Ejercicio 3")
(fibonacci 8)
(fibonacci 10)


; 4. Sumar los numeros desde 1 hasta n.
(define (suma2 n)
  (if (not (= n 0))
      (if (not (= n 1))
          (+ n (suma2 (- n 1)))
          1)0))

(print "Ejercicio 4")
(suma2 20)
(suma2 8)


;5. Escriba un programa que calcule la suma de los numeros que
;existen entre dos numeros dados. Debe considerar ambos numeros.
(define (sumaentre2 a b)
  (cond
    [(> a b)
     (if (> a b)
           (+ a (sumaentre2 (- a 1)b))
           b)]
    [else
     (if (> b a)
           (+ b (sumaentre2 a (- b 1)))
           a)]
    ))

(print "Ejercicio 5")
(sumaentre2 4 9)
(sumaentre2 8 4)


; 6. Escriba una función que calcule cuantos números naturales hay entre 2 números
;dados.

(define (cuantosn a b)
  (cond
    [(> a b)
     (if (> a b)
           (+ 1 (cuantosn (- a 1)b))
           1)]
    [else
     (if (> b a)
           (+ 1 (cuantosn a (- b 1)))
           1)]
    ))

(print "Ejercicio 6")
(cuantosn 4 16)
(cuantosn 22 3)


; 7. Escriba un programa que calcule el valor promedio de los números naturales que
;existen entre dos números dados. Debe considerar ambos números. (Use las
;dos funciones anteriores)

(define (promedio a b)
  (exact->inexact(/(sumaentre2 a b)
    (cuantosn a b))))

(print "Ejercicio 7")
(promedio 56 61)
(promedio 23 15)