#lang racket
;Parcial 2
;Sergio Moncada Muñoz
;1089380570


;1. Escriba un programa que calcule la suma de los numeros que existen entre dos numeros dados.
;Debe considerar ambos numeros.

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
(print "Ejercicio 1")
(newline)
(sumaentre2 4 9)
(sumaentre2 8 3)
(newline)


;2. Escriba una función que calcule cuántos números naturales hay entre 2 números dados.

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
(print "Ejercicio 2")
(newline)
(cuantosn 2 16)
(cuantosn 22 9)
(newline)


;3. Desarrollar una función que toma una lista de números y calcula el promedio

(define lista1 (list 1 2 3 4 5 6 7 8 9))
(define lista2 (list 3 5 7 9 3 5))
(define (longitud lista)
  (cond
    [(empty? lista) 0]
    [else (+ 1 (longitud (rest lista)))]
    ))

(define (suma lista)
  (cond
    [(empty? lista) 0]
    [else (+ (first lista) (suma (rest lista)))]
    ))
    
(define (promedio lista)
 (exact->inexact(/ (suma lista)
     (longitud lista))))

(print "Ejercicio 3")
(newline)
(promedio lista1)
(promedio lista2)


;4. Desarrollar una función que tome un elemento y una lista de elementos y determine
;cuántas veces aparece el símbolo en la lista. Utilizando recursividad.

(define lista3 (list 1 2 1 1 "a" 5 "b" 1  68 "g" "w" 7 "e" "h" "d" "r"))
(define lista4 (list "g" "k" "c" "f" "j" "b" "d" "r" "h" "u" "y" "f" "e" "y" "b" 7 "d" "f" "h" 7 "d"))

(define (veces_elemento lista e contador)
  (cond
    [(empty? lista) contador]
    [(equal? e (first lista)) (begin
                                (+ contador 1)
                                (veces_elemento (rest lista) e (+ 1 contador)))]
    [else (veces_elemento (rest lista) e contador)]))
(print "Ejercicio 4")
(newline)
(veces_elemento lista3 1 0)
(veces_elemento lista4 "f" 0)


;5. A partir de dos fechas, cada fecha tiene como información: el día, mes y año, hacer:

(define-struct fecha (dia mes año))

(define fecha1 (make-fecha 11 1 2015))
(define fecha2 (make-fecha 6 7 2004))

;A. Un programa que determine si la primera fecha es anterior a la segunda.

(define (fm d1 d2)
  (cond
    [(> (fecha-año d1)(fecha-año d2))
     #f]
    [(< (fecha-año d1)(fecha-año d2))
     #t]
    [(= (fecha-año d1)(fecha-año d2))
     (cond
       [(> (fecha-mes d1)(fecha-mes d2))
     #f]
    [(< (fecha-mes d1)(fecha-mes d2))
     #t]
    [(= (fecha-mes d1)(fecha-mes d2))
     (cond
       [(> (fecha-dia d1)(fecha-dia d2))
     #f]
    [(< (fecha-dia d1)(fecha-dia d2))
     #t]
    [else "Ambas fechas son iguales"])])]
    ))
(print "Ejercicio 5-A")
(newline)
(fm fecha1 fecha2)

;B. Un programa que determine cuántos años hay entre las dos fechas

(define (años_diferencia f1 f2)
  (cond
  [(>(fecha-año f2) (fecha-año f1)) (- (fecha-año f2) (fecha-año f1))]
  [(<(fecha-año f2) (fecha-año f1)) (- (fecha-año f1) (fecha-año f2))]
  [else 0]))
(print "Ejercicio 5-B")
(newline)
(años_diferencia fecha1 fecha2)
(años_diferencia fecha2 fecha1)