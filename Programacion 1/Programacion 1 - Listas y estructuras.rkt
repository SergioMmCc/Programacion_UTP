#lang racket
(define-struct empleado (nombre cedula salario))

(define empleado1 (make-empleado "Juan" 1234 1000))
(define empleado2 (make-empleado "Santiago" 5678 2000))
(define empleado3 (make-empleado "Maria" 1122 3000))

(define empresa (list empleado1 empleado2 empleado3))

(define (buscar nombre empresa)
  (cond
    [(empty? empresa) #f]
    [(string=? nombre (empleado-nombre (first empresa))) #t]
    [else (buscar nombre (rest empresa))]
    ))


(define-struct articulos (nombre codigo precio))

(define articulo1 (make-articulos "Jet" 1234 500))
(define articulo2 (make-articulos "Jumbo" 91011 3000))
(define articulo3 (make-articulos "Hershey" 5678 4000))

(define colombina (list articulo1 articulo2 articulo3))

(define (encontrar_nombre precio tienda)
  (cond
    [(empty? tienda) "No existe un producto de este precio"]
    [(equal? precio (articulos-precio (first tienda))) (articulos-nombre (first tienda))]
    [else (encontrar_nombre precio (rest tienda))]))

(define (encontrar_precio nombre tienda)
  (cond
    [(empty? tienda) "No existe un producto con este nombre"]
    [(equal? nombre (articulos-nombre (first tienda))) (articulos-precio (first tienda))]
    [else (encontrar_precio nombre (rest tienda))]))


(define-struct palabras (palabra definicion))
(define palabra1 (make-palabras "silla" "Lugar para sentarse"))
(define palabra2 (make-palabras "puerta" "Entrada a algun lugar"))
(define palabra3 (make-palabras "auriculares" "Artefacto para escuchar musica"))

(define Chicago (list palabra1 palabra2 palabra3))

(define (significados palabra diccionario)
  (cond
    [(empty? diccionario) "La palabra no esta en el diccionario"]
    [(equal? palabra (palabras-palabra (first diccionario))) (palabras-definicion (first diccionario))]
    [else (significados palabra (rest diccionario))]
    ))