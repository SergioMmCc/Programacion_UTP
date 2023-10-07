#lang racket

#| Parcial Final
Sergio Moncada Muñoz
1089380570 |#


(require (lib "graphics.ss" "graphics"))
(open-graphics)


#| 1. Dibujar 500 círculos pequeños de diferentes colores de forma recursiva en distintas
partes de una ventana. Cada círculo debe aparecer cada 0.1 segundos. |#


(print "Ejercicio 1")

(define Ventana1 (open-viewport "Cuadro Ejercicio 1" 800 600))

(define (circulos help)
  (cond
    [(= 500 help) ((draw-solid-ellipse Ventana1) (make-posn (* (random) 800) (* (random) 600)) 100 100 (make-rgb (random) (random) (random)))]
    [else ((draw-solid-ellipse Ventana1) (make-posn (* (random) 1000) (* (random) 1000)) 100 100 (make-rgb (random) (random) (random)))
          (sleep 0.1)
          (circulos (+ 1 help))]))

(circulos 1)


#| 2. Construya un programa en donde en una ventana de 800*600 se dibuje un pixel en la
posición (0,50), luego debe dibujarse otro pixel del mismo color cada 0.1 segundos en la
posición (1,50), (2,50), (3,50) hasta llegar a la posición (800,50). Use recursividad |#


(print "Ejercicio 2")

(define Ventana2 (open-viewport "Cuadro Ejercicio 2" 800 600))


(define (pixel posx posy)
  (cond
    [(= posx 800) ((draw-pixel Ventana2) (make-posn posx posy) "blue")]
    [else ((draw-pixel Ventana2) (make-posn posx posy) "blue")
          (sleep 0.1)
          (pixel (+ 1 posx) posy)]
    ))

(pixel 0 50)


#| 3. Dibujar 5 cuadrados concentricos que cambien de color cada segundo. Usar la función
(sleep 1) para observar el cambio de color y la función random para que cambie de color.
Todos los cuadrados deben tomar un color diferente. |#


(print "Ejercicio 3")

(define Ventana3 (open-viewport "Cuadro Ejercicio 3" 800 600))

(define (cuadrados centrox centroy medidas cont)
  (cond
    [(= cont 5) ((draw-solid-rectangle Ventana3) (make-posn centrox centroy) medidas medidas
                                (make-rgb (random) (random) (random)))]
    [else ((draw-solid-rectangle Ventana3) (make-posn centrox centroy) medidas medidas
                                (make-rgb (random) (random) (random)))
          (cuadrados (+ 35 centrox) (+ 35 centroy) (- medidas 70) (+ 1 cont))])
  (sleep 1)
  (cuadrados 200 150 400 1))

(cuadrados 200 150 400 1)