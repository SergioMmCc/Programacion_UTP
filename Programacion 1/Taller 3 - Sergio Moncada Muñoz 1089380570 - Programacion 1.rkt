#lang racket
;Taller 3
;Sergio Moncada Muñoz
;1089380570


;1. Dado un directorio telefonico de amigos donde cada amigo tiene nombre, direccion y
;telefono, crear una funcion que dado el nombre devuelva el numero telefonico del amigo.

(define-struct amigo (nombre direccion telefono))

(define amigo1 (make-amigo "Julian" "Mz 15 Casa 13 Bosques" 3223457086))
(define amigo2 (make-amigo "Thiago" "Mz 6 Casa 24 Bombay" 3113486372))
(define amigo3 (make-amigo "Jeronimo" "Mz 23 Casa 5 Playa Rica" 3202519932))

(define directorio (list amigo1 amigo2 amigo3))

(define (numero nombre directorio)
  (cond
    [(empty? directorio) "Este amigo no esta en el directorio"]
    [(string=? nombre (amigo-nombre (first directorio)))
     (amigo-telefono (first directorio))]
    [else (numero nombre (rest directorio))]))

(print "Ejercicio #1")
(newline)
(numero "Jeronimo" directorio)
(numero "Julian" directorio)


;2. Dada una lista de estudiantes de la universidad con los campos nombre, codigo y curso,
;realizar una funcion que dado un codigo determine si el estudiante se encuentra
;matriculado en la universidad.

(define-struct estudiante (nombre codigo curso))

(define estudiante1 (make-estudiante "Santiago" 1088547341 "Ingenieria en Sistemas"))
(define estudiante2 (make-estudiante "Miguel" 1090826284 "Ciencias del Deporte"))
(define estudiante3 (make-estudiante "Valeria" 1089735189 "Licenciatura en Español"))

(define lista_estudiantes (list estudiante1 estudiante2 estudiante3))

(define (matricula codigo lista)
  (cond
    [(empty? lista) "El estudiante no se encuentra matriculado en la Universidad"]
    [(equal? codigo (estudiante-codigo (first lista)))
     "El estudiante si esta matriculado en la Universidad"]
    [else (matricula codigo (rest lista))]))

(print "Ejercicio #2")
(newline)
(matricula 1090826284 lista_estudiantes)
(matricula 1089735189 lista_estudiantes)


;3. Dado un vector V de enteros y un numero X, devolver el valor que corresponde al
;numero de veces que esta el valor X en el vector.

(define vector1 (vector 4 1 6 9 4 37 2 6 13 5 1 6))
(define vector2 (vector 4 7 2 8 4 22 5 4 8 3 8 0 8 6 5 43))

(define (cuantas_veces V X pos cont)
  (cond
    [(> pos (- (vector-length V) 1)) cont]
    [else
     (cond
       [(equal? (vector-ref V pos) X) (cuantas_veces V X (add1 pos)(add1 cont))]
       [else (cuantas_veces V X (add1 pos) cont)])]))

(print "Ejercicio #3")
(newline)
(cuantas_veces vector1 6 0 0)
(cuantas_veces vector2 5 0 0)


;4. Construir un programa que reciba un vector de numeros. Se deben modificar cada uno
;de los datos, dividiendo su valor por 100.

(define vector3 (vector 4 7 3 2 865 35 643 23 877))
(define vector4 (vector 2 7 3 235 42 4678 213 74 12))

(define (div100 n)
  (exact->inexact(/ n 100)))

(define (divV V)
  (vector-map div100 V))

(print "Ejercicio #4")
(newline)
(divV vector3)
(divV vector4)


;5. Construir un programa que reciba un vector de enteros y un número X. La función debe
;borrar el número si lo encuentra y debe mover a la izquierda todos los elementos
;siguientes y dejando el valor -1 en la última posición. Considerar que todos los números
;son diferentes.

(define vector5 (vector 1 2 3 4 5 6 7 8 9))
(define vector6 (vector 6 3 8 2 9 7 10 16))
(define vector-1 (vector -1))

(define (buscar V X)
  (vector-append (vector-append(vector-take V (vector-member X V))(vector-take-right V (- (vector-length V) (+ 1(vector-member X V))))) vector-1))

(print "Ejercicio #5")
(newline)
(buscar vector6 7)
(buscar vector5 4)