#lang racket


;1. Dado un vector con n números calcular el promedio de los elementos del vector.

(define vect1 (vector 1 2 3 4 5 6 76 87 9 90))

(define (suma vector pos)
  (cond
    [(> pos (- (vector-length vector) 1)) 0]
    [else (+ (vector-ref vector pos)(suma vector (add1 pos)))]))

(define (promedio vector pos)
  (exact->inexact(/(suma vector pos) (vector-length vector))))


;2. Dados dos vectores con elementos ya incluidos, devolver un tercer vector con la
;concatenación de los dos vectores dados.

(define vect2 (vector 284 "fhds" 5 "uyv" 39))
(define vect3 (vector "df" "f4" 5 7 "vg" "ee" 56))

(define (juntar vector1 vector2)
  (vector-append vector1 vector2)
  )


;3. Construir un programa que reciba un vector de números. Se deben modificar cada uno
;de los datos, multiplicando su valor por 100. Ej: si el vector es: # (3 5 8 2), debe quedar
;así: # (300 500 800 200)

(define vect4 (vector 55 67 3 5 7 4))

(define (multi100 n)
  (* n 100))

(define (vector100 vector)
  (vector-map multi100 vector))


;4. Construir un programa que reciba un vector de enteros y lo ordene ascendentemente.

(define vect5 (vector 4 7 32 7 0))

(define (orden vector)
  (vector-sort vector <))

;5. Construir un programa que reciba un vector de enteros e indique si está ordenado
;ascendentemente.

(define vect6 (vector 1 3 4 6 7))

(define (orden2 vector pos1 pos2)
  (cond
    [(> pos2 (- (vector-length vector) 1)) #t]
    [(> (vector-ref vector pos1) (vector-ref vector pos2)) #f]
    [else (orden2 vector (add1 pos1) (add1 pos2))]))