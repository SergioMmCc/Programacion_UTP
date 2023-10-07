#lang racket
;Parcial #3
;Sergio Moncada Muñoz
;1089380570


;1. Desarrollar un programa que a partir de una escuela determine cuántos profesores
;diferentes enseñan en ella

(define-struct profesor (nombre curso escuela))

(define profesor1 (make-profesor "Javier" "Programacion y Informatica" "Guadalupe"))
(define profesor2 (make-profesor "Juan" "Matematicas y Fisica" "Guadalupe"))
(define profesor3 (make-profesor "Luisa" "Artes" "Guadalupe"))
(define profesor4 (make-profesor "Valeria" "Ingles" "Maria Auxiliadora"))

(define lista_profesores (list profesor1 profesor2 profesor3 profesor4))

(define (buscar_colegio escuela profesores cont)
  (cond
    [(empty? profesores) cont]
    [(string=? escuela (profesor-escuela (first profesores))) (buscar_colegio escuela (rest profesores) (+ 1 cont))]
    [else (buscar_colegio escuela (rest profesores) cont)]))

(print "Ejercicio #1")
(newline)
(buscar_colegio "Guadalupe" lista_profesores 0)
(buscar_colegio "Maria Auxiliadora" lista_profesores 0)


;2. Crear una función llamada ElevarPrecios que tome una lista de artículos (el artículo tiene
;los campos nombre del artículo, precio y código del producto) y produzca la lista con
;todos los precios de los artículos incrementados en un 10%

(define-struct articulo (nombre precio codigo))

(define articulo1 (make-articulo "Jet" 500 1234))
(define articulo2 (make-articulo "Jumbo" 3000 91011))
(define articulo3 (make-articulo "Hershey" 4000 5678))

(define colombina (list articulo1 articulo2 articulo3))

  (define (elevarprecios lista)
    (cond
      [(empty? lista)empty]
      [(cons (* (articulo-precio (first lista)) 1.10) (elevarprecios (rest lista)))]))


(print "Ejercicio #2")
(newline)
(elevarprecios colombina)


;3. Construir un programa que reciba un vector de enteros e indique si está ordenado de
;forma ascendente, si no lo está que lo ordene de forma descendente.

(define vect1 (vector 4 68 9 3 24 68))
(define vect2 (vector 34 88 5 1 6 983))
(define vect3 (vector 8 2 5 9 3 1 6))

(define (orden vect)
  (cond
    [(vector-empty? vect) "error"]
    [(equal? vect (vector-sort vect <)) "Esta ordenado de forma ascendente"]
    [else (vector-sort vect >)]))

(print "Ejercicio #3")
(newline)
(orden vect2)
(orden vect3)


;4. Construir un programa que reciba un vector de enteros y un número X. Se requiere que
;el programa busque el número X en el vector y devuelva la posición donde se encuentra
;por última vez en el vector. En caso de no estar debe devolver #f.

(define vect6 (vector 1 2 3 4 7 5 3 4))
(define vect7 (vector 3 5 9 0 5 2 46 8 0))

(define (posicion vect x)
  (vector-member x vect))

(print "Ejercicio #4")
(newline)
(print "No fui capaz")
(newline)


;5. Construir un programa que reciba un vector de enteros y un número X. La función debe
;borrar el número si lo encuentra y debe (mover a la derecha) todos los elementos
;siguientes y dejando el valor -1 en la primera posición. Considerar que todos los números
;son diferentes.

(define vector4 (vector 1 2 3 4 5 6 7 8 9))
(define vector5 (vector 6 3 8 2 9 7 10 16))
(define vector-1 (vector -1))

(define (buscar V X)
  (vector-append vector-1(vector-append(vector-take V (vector-member X V))(vector-take-right V (- (vector-length V) (+ 1(vector-member X V)))))))

(print "Ejercicio #5")
(newline)
(buscar vector4 6)
(buscar vector5 9)