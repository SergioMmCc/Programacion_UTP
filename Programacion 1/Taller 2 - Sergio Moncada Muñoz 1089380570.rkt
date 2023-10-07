#lang racket
;Taller #2
;Sergio Moncada Muñoz
;1089380570


;1. Construir una función que reciba como parámetro un número N y calcule la suma de
;todos los enteros comprendidos entre 1 y número recibido utilizando recursión.

(define (suma_n n)
  (cond
    [(= n 1) 1]
    [(> n 0) (+ n (suma_n (- n 1)))]
    [else 0]
    ))
(print "Ejercicio 1")
(newline)
(print (suma_n 6))
(newline)
(print (suma_n 9))
(newline)


;2. Hallar la suma de los N primeros números pares utilizando recursión.

(define (suma_pares n)
  (cond
    [(<= n 0) 0]
    [else
     (cond
       [(= n 1) (* n 2)]
       [(> n 1) (+ (* 2 n) (suma_pares (- n 1)))]
       )]
    ))
(print "Ejercicio 2")
(newline)
(print (suma_pares 4))
(newline)
(print (suma_pares 10))
(newline)


;3. Lea un número y determine si es primo o no, utilizando recursión.

(define (primo n div)
  (cond
    [(< n 1) "Indique un numero mayor"]
    [(or (= n 1)(= div 2)) "Es primo"]
    [(> div 2)
     (cond
       [(= (modulo n (- div 1))0) "No es primo"]
       [else (primo n (- div 1))]
       )]))
(print "Ejercicio 3")
(newline)
(print (primo 34 34))
(newline)
(print (primo 19 19))
(newline)


;4. Realizar una función que toma un elemento y una lista de números y retorna la lista sin
;el elemento. Sin utilizar recursión.

(define lista1 (list 0 1 2 3 4 5 6 7 8 9))
(define lista2 (list "a" "b" "c" "d" "e" "f" "g" "h"))

(define (eliminar_n n lista)
  (remove n lista))
(print "Ejercicio 4")
(newline)
(print (eliminar_n 7 lista1))
(newline)
(print (eliminar_n "e" lista2))
(newline)


;5.  Realizar una función que toma un elemento y una lista de números y retorna la lista sin
;el elemento. Utilizando recursión.

(define (lista_recursion n lista)
  (cond
    [(empty? lista) empty]
    [(not(equal? n (first lista))) (cons (first lista) (lista_recursion n (rest lista)))]
    [else (lista_recursion n (rest lista))]
    ))
(print "Ejercicio 5")
(newline)
(print (lista_recursion "g" lista2))
(newline)
(print (eliminar_n 4 lista1))
(newline)


;6. Desarrolle a partir de dos artículos diferentes, donde cada articulo tiene la siguiente
;información: nombre del artículo, nombre del almacén, costo de producción unitario,
;valor venta unitario, numero de ventas al año:

(define-struct articulos (articulo almacen costo_produccion valor_venta ventas_anuales))
(define articulo1 (make-articulos "fifa" "EA" 100000 260000 100000000))
(define articulo2 (make-articulos "PES" "konami" 60000 150000 30000000))

;a) Un programa que determine si todos los artículos se venden en el mismo almacén

(define (same_almacen a1 a2)
  (if
   (equal?(articulos-almacen a1)(articulos-almacen a2))
   "Los articulos se venden en el mismo almacen" "Los articulos no se venden en el mismo almacen"))
(print "Ejercicio 6-A")
(newline)
(print (same_almacen articulo1 articulo2))
(newline)

;b) Un programa que retorne el articulo que mas ganancia ha dejado en el año.

(define (ganancias a1 a2)
  (cond
    [(>(* (articulos-ventas_anuales a1) (- (articulos-valor_venta a1) (articulos-costo_produccion a1)))
       (* (articulos-ventas_anuales a2) (- (articulos-valor_venta a2) (articulos-costo_produccion a2))))
     (print (articulos-articulo a1)) "ha dejado mas ganancias"]
    [(<(* (articulos-ventas_anuales a1) (- (articulos-valor_venta a1) (articulos-costo_produccion a1)))
       (* (articulos-ventas_anuales a2) (- (articulos-valor_venta a2) (articulos-costo_produccion a2))))
     (print (articulos-articulo a2)) "ha dejado mas ganancias"]
    [else "Ambos articulos han dejado las mismas ganancias"]
    ))
(print "Ejercicio 6-B")
(newline)
(print (ganancias articulo1 articulo2))
(newline)
(print (ganancias articulo2 articulo1))
(newline)

;c) Un programa que retorne el nombre del almacén que menos ventas en total ha tenido

(define (menos_ventas a1 a2)
  (cond
    [(>(articulos-ventas_anuales a1)(articulos-ventas_anuales a2))
     (print (articulos-almacen a2)) "ha tenido menos ventas"]
     [(<(articulos-ventas_anuales a1)(articulos-ventas_anuales a2))
     (print (articulos-almacen a1)) "ha tenido menos ventas"]
     [else "Ambos articulos han tenido las mismas ventas"]))
(print "Ejercicio 6-C")
(newline)
(print (menos_ventas articulo1 articulo2))
(newline)
(print (menos_ventas articulo2 articulo1))
(newline)

;d) Un programa que retorne el valor de venta unitario del articulo que menos se ha
;vendido en el año

(define (menos_vendido a1 a2)
  (cond
    [(>(articulos-ventas_anuales a1)(articulos-ventas_anuales a2))
     (print (articulos-valor_venta a2))]
     [(<(articulos-ventas_anuales a1)(articulos-ventas_anuales a2))
     (print (articulos-valor_venta a1))]
     [else "Ambos articulos han tenido las mismas ventas"]))
(print "Ejercicio 6-D")
(newline)
(print (menos_vendido articulo1 articulo2))
(newline)
(print (menos_vendido articulo2 articulo1))
(newline)

;e) Un programa que retorne el promedio total de las ganancias dejadas en el año por los
;dos artículos

(define (promedio_ganancias a1 a2)
  (/(+(* (articulos-ventas_anuales a1) (- (articulos-valor_venta a1) (articulos-costo_produccion a1)))
  (* (articulos-ventas_anuales a2) (- (articulos-valor_venta a2) (articulos-costo_produccion a2))))2))
(print "Ejercicio 6-E")
(newline)
(print (promedio_ganancias articulo1 articulo2))
(newline)
(print (promedio_ganancias articulo2 articulo1))
(newline)